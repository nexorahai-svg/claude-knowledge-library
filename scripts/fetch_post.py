#!/usr/bin/env python3
"""Read a post the user sent (X or Instagram) without logging in: text, links, author, media.

Usage:  python3 scripts/fetch_post.py URL [URL ...] [--out DIR] [--frames N]

  X / Twitter   read-only fxtwitter API: text, quoted post, expanded links, likes, media URLs
  Instagram     og: tags (author, cover), embed page (full caption, video URL); with --out the
                cover and video are saved and an N-frame contact sheet is made with FFmpeg,
                because some reel covers are just black

Prints Markdown, one block per URL. Files go to --out (default: no files). Only for reading
and learning principles; do not keep, publish or copy the media (research/x-research-plan.md).
"""
import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request

UA_BROWSER = {"User-Agent": "Mozilla/5.0"}   # a full browser string gets a different embed page without the caption
UA_PREVIEW = {"User-Agent": "facebookexternalhit/1.1"}


def get(url, headers, timeout=40):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def save(url, path):
    with open(path, "wb") as fh:
        fh.write(get(url, UA_BROWSER, 120))
    return path


def contact_sheet(video, out, frames):
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        return None
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video],
                         capture_output=True, text=True).stdout.strip()
    try:
        fps = frames / max(float(dur), 0.1)
    except ValueError:
        return None
    cols = min(frames, 4)
    rows = (frames + cols - 1) // cols
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", video, "-vf",
                    f"fps={fps:.4f},scale=320:-1,tile={cols}x{rows}", "-frames:v", "1", out], check=False)
    return out if os.path.exists(out) else None


def x_post(url, out):
    m = re.search(r"(?:x|twitter)\.com/([^/]+)/status/(\d+)", url)
    if not m:
        return f"## {url}\n\nNot an X post link.\n"
    data = json.loads(get(f"https://api.fxtwitter.com/{m.group(1)}/status/{m.group(2)}", UA_BROWSER))
    t = data.get("tweet") or {}
    lines = [f"## X — @{(t.get('author') or {}).get('screen_name', m.group(1))} ({t.get('created_at', '?')})",
             f"<{url}> · likes {t.get('likes')} · views {t.get('views')}", "", t.get("text") or "(no text)"]
    links = [f.get("replacement") for f in ((t.get("raw_text") or {}).get("facets") or [])
             if isinstance(f, dict) and f.get("type") == "url"]
    if links:
        lines += ["", "**Links:**"] + [f"- {u}" for u in links]
    if t.get("quote"):
        q = t["quote"]
        lines += ["", f"**Quoting @{(q.get('author') or {}).get('screen_name')}:**", q.get("text") or ""]
    if t.get("article"):
        lines += ["", f"**Article:** {t['article'].get('title')}"]
    media = (t.get("media") or {}).get("all") or []
    for i, md in enumerate(media):
        lines.append(f"- media {i + 1}: {md.get('type')} {md.get('url')}")
        if out and md.get("url"):
            ext = ".mp4" if md.get("type") in ("video", "gif") else ".jpg"
            save(md["url"], os.path.join(out, f"x-{m.group(2)}-{i + 1}{ext}"))
    return "\n".join(lines) + "\n"


def insta_post(url, out, frames):
    m = re.search(r"instagram\.com/(?:[^/]+/)?(reel|p|tv)/([A-Za-z0-9_-]+)", url)
    if not m:
        return f"## {url}\n\nNot an Instagram post or reel link.\n"
    code = m.group(2)
    page = get(f"https://www.instagram.com/{m.group(1)}/{code}/", UA_PREVIEW).decode("utf-8", "replace")
    meta = {k: html.unescape(v) for k, v in re.findall(r'<meta (?:property|name)="([^"]+)" content="([^"]*)"', page)}
    embed = get(f"https://www.instagram.com/p/{code}/embed/captioned/", UA_BROWSER).decode("utf-8", "replace")
    cap = re.search(r'class="Caption"(.*?)</div>', embed, re.S)
    caption = html.unescape(re.sub(r"<[^>]+>", "", re.sub(r"<br ?/?>", "\n", cap.group(1)))).strip() if cap else ""
    vid = re.search(r'video_url\\+":\\+"(.*?)\\+"', embed)
    video = vid.group(1).replace("\\", "").replace("u0026", "&") if vid else None
    lines = [f"## Instagram — {meta.get('twitter:title', code)}", f"<{url}>",
             f"{meta.get('description') or meta.get('og:description') or ''}".strip(), "", caption or "(no caption)"]
    if out:
        if meta.get("og:image"):
            lines.append(f"- cover: {save(meta['og:image'], os.path.join(out, f'ig-{code}-cover.jpg'))}")
        if video:
            mp4 = save(video, os.path.join(out, f"ig-{code}.mp4"))
            lines.append(f"- video: {mp4}")
            sheet = contact_sheet(mp4, os.path.join(out, f"ig-{code}-frames.jpg"), frames)
            if sheet:
                lines.append(f"- frames: {sheet}")
    else:
        lines.append(f"- video: {'available (use --out to save and get frames)' if video else 'none'}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--out", help="folder for cover, video and frame sheet (created if missing)")
    ap.add_argument("--frames", type=int, default=8, help="frames in the contact sheet (default 8)")
    a = ap.parse_args()
    if a.out:
        os.makedirs(a.out, exist_ok=True)
    for url in a.urls:
        try:
            if "instagram.com" in url:
                print(insta_post(url, a.out, a.frames))
            elif re.search(r"(x|twitter)\.com/", url):
                print(x_post(url, a.out))
            else:
                print(f"## {url}\n\nOnly X and Instagram links are supported.\n")
        except Exception as e:  # one bad link must not stop the rest
            print(f"## {url}\n\nCould not read: {e}\n", file=sys.stdout)


if __name__ == "__main__":
    main()
