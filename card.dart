import 'package:flutter/material.dart';

class GlassCard extends StatefulWidget() {
  const GlassCard({super.key});

  State<GlassCard> contentState() => _GlassCardState();
}

class _GlassCardState extends State<GlassCard> {
  List<Text> listText;
  Padding? padding;
  Border? borderSize;
  Color? highlightTint;
  bool? transparent;

  _GlassCardState({
    required this.listTest;
    this.padding = Padding(10,10);
    this.borderSize = Border.outlineBorder();
    this.highlightTint = Colors.pink.shad300;
    this.transparent = false;
  });
}