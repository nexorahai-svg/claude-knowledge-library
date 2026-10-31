#!/usr/bin/env python3
"""Stop hook: hold Claude to the user's chosen reply language (2026-10-24).

The `language` setting and the standing rule were not enough: replies kept slipping into English, mostly in the short
lines between tool calls and in the first sentence. At the end of every turn this hook reads all of Claude's text in
that turn (from the transcript), removes code blocks, inline code, URLs and paths, and measures the share of Latin
letters. Any language the user chose works:
  - another script (Persian, Arabic, Russian, Hindi, Chinese, Japanese, Korean, Greek, Hebrew, Thai, …): a block that is
    mostly Latin letters is English;
  - a Latin-script language (Spanish, French, German, Italian, Portuguese, Turkish, Dutch, Indonesian, Polish, Swedish,
    Vietnamese, …): a block full of common English words and few common words of the chosen language is English.
The turn is sent back once: "rewrite in <language>". Users who chose English are never checked; a language the guard
does not know is skipped rather than guessed.
"""
import json
import os
import re
import sys

SETTINGS = os.path.expanduser("~/.claude/settings.json")
NON_LATIN = {"persian": r"[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]", "فارسی": r"[؀-ۿ]",
             "arabic": r"[؀-ۿݐ-ݿ]", "العربية": r"[؀-ۿ]", "urdu": r"[؀-ۿ]",
             "hebrew": r"[֐-׿]", "russian": r"[Ѐ-ӿ]", "ukrainian": r"[Ѐ-ӿ]",
             "greek": r"[Ͱ-Ͽ]", "hindi": r"[ऀ-ॿ]", "chinese": r"[一-鿿]",
             "japanese": r"[぀-ヿ一-鿿]", "korean": r"[가-힯]", "thai": r"[฀-๿]"}
NON_LATIN.update({"bengali": r"[\u0980-\u09FF]", "tamil": r"[\u0B80-\u0BFF]", "pashto": r"[\u0600-\u06FF]",
                  "kurdish (sorani)": r"[\u0600-\u06FF]", "georgian": r"[\u10A0-\u10FF]", "armenian": r"[\u0530-\u058F]",
                  "русский": r"[\u0400-\u04FF]", "中文": r"[\u4E00-\u9FFF]", "日本語": r"[\u3040-\u30FF\u4E00-\u9FFF]",
                  "한국어": r"[\uAC00-\uD7AF]", "हिन्दी": r"[\u0900-\u097F]", "עברית": r"[\u0590-\u05FF]"})
EN = set("the and is are you your this that with for to of in it be was were will would can have has not on at by from "
         "we our they them what which when where how there here then than but or if so do does did just now run".split())
LATIN = {  # common words of Latin-script languages (lowercase), keyed by English and native names
    ("spanish", "español"): "el la los las de que y en un una es por para con no se su lo como más pero sus le ya o este sí",
    ("french", "français"): "le la les de des et est un une que qui dans pour pas sur au avec ce il elle nous vous je ne plus",
    ("german", "deutsch"): "der die das und ist nicht ein eine zu den mit von sie es ich auf für im dem sich auch wir ihr",
    ("italian", "italiano"): "il la di che e è un una per non con del della sono si le lo gli ma come più anche questo",
    ("portuguese", "português"): "o a os as de que e é um uma para com não do da em no na se por mais mas você",
    ("turkish", "türkçe"): "ve bir bu da de için ile çok ne ama gibi daha olarak var değil ben sen o mi mu",
    ("dutch", "nederlands"): "de het een en is van in dat niet op te zijn met voor je ik we ook maar dan",
    ("indonesian", "bahasa indonesia"): "yang dan di ini itu dengan untuk tidak ada dari ke akan saya kamu anda bisa juga",
    ("malay", "bahasa melayu"): "yang dan di ini itu dengan untuk tidak ada dari ke akan saya anda boleh juga",
    ("polish", "polski"): "i w nie na się z jest to że do jak co ale tak czy jego jej dla",
    ("swedish", "svenska"): "och i att det som en på är av för med till den inte har jag du vi",
    ("vietnamese", "tiếng việt"): "và của là có không một những được cho này trong với các người đã bạn",
    ("tagalog", "filipino"): "ang ng sa na at mga ay para hindi ko mo ito siya kami",
    ("swahili", "kiswahili"): "na ya wa kwa ni la za katika hii kama si au",
    ("romanian", "română"): "și în de la nu este un o pe cu că care să mai",
    ("czech", "čeština"): "a v se na je to že s z do ale jak tak pro",
}


def latin_words_for(lang):
    low = (lang or "").lower()
    for names, words in LATIN.items():
        if any(n in low for n in names):
            return set(words.split())
    return None


def english_heavy(text, words):
    tokens = re.findall(r"[a-zà-ÿçğışöüăâîșțđơưạ-ỹ']+", STRIP.sub(" ", text).lower())
    en = sum(t in EN for t in tokens)
    tg = sum(t in words for t in tokens)
    return en >= 6 and en > 2 * tg


STRIP = re.compile(r"```.*?```|`[^`\n]*`|https?://\S+|[\w./~-]*/[\w./-]+|\b[\w-]+\.(md|py|json|sh|dart|ts|js|html|txt)\b|"
                   r"\[[^\]]*\]\([^)]*\)", re.S)


def script_for(lang):
    low = (lang or "").lower()
    for key, rx in NON_LATIN.items():
        if key in low:
            return rx
    return None


def turn_texts(transcript):
    """Claude's text blocks since the user's last real message."""
    blocks = []
    with open(transcript, encoding="utf-8") as f:
        for line in f:
            try:
                e = json.loads(line)
            except ValueError:
                continue
            msg = e.get("message") or {}
            role, content = msg.get("role"), msg.get("content")
            if role == "user":
                if isinstance(content, str) or (isinstance(content, list) and any(
                        isinstance(b, dict) and b.get("type") == "text" for b in content)):
                    blocks = []   # a new user turn starts
            elif role == "assistant" and isinstance(content, list):
                blocks += [b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"]
    return blocks


def mostly_latin(text, rx):
    prose = STRIP.sub(" ", text)
    native = len(re.findall(rx, prose))
    latin = len(re.findall(r"[A-Za-z]", prose))
    return latin >= 40 and latin > 1.2 * native


def main():
    data = json.load(sys.stdin)
    if data.get("stop_hook_active"):
        return
    try:
        lang = json.load(open(SETTINGS)).get("language")
    except (OSError, ValueError):
        return
    if not lang or re.search(r"\benglish\b", lang, re.I):
        return
    rx, words = script_for(lang), latin_words_for(lang)
    if not (rx or words) or not os.path.exists(data.get("transcript_path") or ""):
        return
    texts = turn_texts(data["transcript_path"])
    last = data.get("last_assistant_message")
    if isinstance(last, str) and last:
        texts.append(last)
    bad = [t for t in texts if (mostly_latin(t, rx) if rx else english_heavy(t, words))]
    if not bad:
        return
    sample = re.sub(r"\s+", " ", STRIP.sub(" ", bad[0])).strip()[:140]
    print(json.dumps({"decision": "block", "reason": (
        f"Language rule: the user chose {lang} for everything Claude writes to them, and {len(bad)} text block(s) in this "
        f"turn were mostly English (e.g. \"{sample}…\"). Rewrite your final answer fully in {lang} now, including the "
        f"first sentence; keep code, commands, file names and technical terms as they are. From now on write every line "
        f"to the user in {lang}, also the short lines between tool calls.")}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass   # a hook must never break the session
