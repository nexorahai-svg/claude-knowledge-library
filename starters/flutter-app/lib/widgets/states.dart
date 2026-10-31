import 'package:flutter/material.dart';

import '../design/tokens.dart';

/// Every data screen has five states: loading, content, empty, error, offline.
/// These widgets make the four non-content states consistent across an app.

class EmptyState extends StatelessWidget {
  const EmptyState({super.key, required this.icon, required this.title, required this.message, this.action});

  final IconData icon;
  final String title;
  final String message;

  /// Primary next step (e.g. "Explore stays"). Empty screens should never be a dead end.
  final Widget? action;

  @override
  Widget build(BuildContext context) {
    final t = context.tokens;
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(AppTokens.s8),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              width: 72,
              height: 72,
              decoration: BoxDecoration(color: t.surfaceAlt, shape: BoxShape.circle),
              child: Icon(icon, size: 32, color: t.accent),
            ),
            const SizedBox(height: AppTokens.s4),
            Text(title, textAlign: TextAlign.center, style: Theme.of(context).textTheme.titleMedium),
            const SizedBox(height: AppTokens.s2),
            Text(message, textAlign: TextAlign.center, style: TextStyle(color: t.muted)),
            if (action != null) ...[const SizedBox(height: AppTokens.s5), action!],
          ],
        ),
      ),
    );
  }
}

class ErrorState extends StatelessWidget {
  const ErrorState({
    super.key,
    required this.title,
    required this.message,
    required this.onRetry,
    this.retryLabel = 'Try again',
  });

  /// Say what happened and what to do, in plain words. No codes or stack traces.
  final String title;
  final String message;
  final VoidCallback onRetry;
  final String retryLabel;

  @override
  Widget build(BuildContext context) {
    final t = context.tokens;
    return EmptyState(
      icon: Icons.error_outline_rounded,
      title: title,
      message: message,
      action: OutlinedButton.icon(
        onPressed: onRetry,
        icon: Icon(Icons.refresh_rounded, color: t.ink),
        label: Text(retryLabel),
      ),
    );
  }
}

class OfflineBanner extends StatelessWidget {
  const OfflineBanner({super.key, required this.text});

  final String text;

  @override
  Widget build(BuildContext context) {
    final t = context.tokens;
    return Semantics(
      liveRegion: true,
      child: Container(
        width: double.infinity,
        padding: const EdgeInsets.symmetric(horizontal: AppTokens.s4, vertical: AppTokens.s3),
        color: t.ink,
        child: Row(
          children: [
            Icon(Icons.cloud_off_rounded, size: 18, color: t.canvas),
            const SizedBox(width: AppTokens.s2),
            Expanded(child: Text(text, style: TextStyle(color: t.canvas, fontWeight: FontWeight.w600))),
          ],
        ),
      ),
    );
  }
}

/// Placeholder block with a moving sheen. Respects "reduce motion".
class Skeleton extends StatefulWidget {
  const Skeleton({super.key, this.width, required this.height, this.radius});

  final double? width;
  final double height;
  final double? radius;

  @override
  State<Skeleton> createState() => _SkeletonState();
}

class _SkeletonState extends State<Skeleton> with SingleTickerProviderStateMixin {
  late final AnimationController _c = AnimationController(vsync: this, duration: const Duration(milliseconds: 1300));

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (MediaQuery.of(context).disableAnimations) {
      _c.stop();
    } else if (!_c.isAnimating) {
      _c.repeat();
    }
  }

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final t = context.tokens;
    final base = t.surfaceAlt;
    final shine = Color.lerp(base, t.canvas, 0.6)!;
    return ExcludeSemantics(
      child: AnimatedBuilder(
        animation: _c,
        builder: (context, _) {
          final x = _c.value * 3 - 1.5;
          return Container(
            width: widget.width ?? double.infinity,
            height: widget.height,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(widget.radius ?? t.radiusMd),
              gradient: LinearGradient(
                begin: Alignment(x - 1, 0),
                end: Alignment(x + 1, 0),
                colors: [base, shine, base],
              ),
            ),
          );
        },
      ),
    );
  }
}
