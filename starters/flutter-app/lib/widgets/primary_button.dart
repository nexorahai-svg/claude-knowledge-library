import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../design/tokens.dart';

/// The one prominent action of a screen (keep one or two per view).
/// Has the states every custom button needs: pressed (scale), loading, disabled.
class PrimaryButton extends StatefulWidget {
  const PrimaryButton({super.key, required this.label, required this.onPressed, this.loading = false, this.icon});

  final String label;
  final VoidCallback? onPressed;
  final bool loading;
  final IconData? icon;

  @override
  State<PrimaryButton> createState() => _PrimaryButtonState();
}

class _PrimaryButtonState extends State<PrimaryButton> {
  bool _down = false;

  @override
  Widget build(BuildContext context) {
    final t = context.tokens;
    final enabled = widget.onPressed != null && !widget.loading;
    return AnimatedScale(
      scale: _down ? 0.97 : 1,
      duration: t.fast,
      curve: t.easeOut,
      child: Listener(
        onPointerDown: enabled ? (_) => setState(() => _down = true) : null,
        onPointerUp: (_) => setState(() => _down = false),
        onPointerCancel: (_) => setState(() => _down = false),
        child: SizedBox(
          width: double.infinity,
          child: FilledButton(
            onPressed: enabled
                ? () {
                    HapticFeedback.lightImpact();
                    widget.onPressed!();
                  }
                : null,
            child: AnimatedSwitcher(
              duration: t.fast,
              child: widget.loading
                  ? SizedBox(
                      key: const ValueKey('loading'),
                      width: 22,
                      height: 22,
                      child: CircularProgressIndicator.adaptive(strokeWidth: 2.4, valueColor: AlwaysStoppedAnimation(t.onAccent)),
                    )
                  : Row(
                      key: const ValueKey('label'),
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        if (widget.icon != null) ...[Icon(widget.icon, size: 20), const SizedBox(width: 8)],
                        Text(widget.label),
                      ],
                    ),
            ),
          ),
        ),
      ),
    );
  }
}
