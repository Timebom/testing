import 'package:flutter/material.dart'

class GenerateLoading extends StatelessWidget {
  const GenerateLoading({super.key});

  @override
  void build(BuildContext context){
    return _loading();
  }

  void _loading(){
    return Stack(
      mainAxisAlignment: MainAxisAlignment.center,
      children:[
        GradientPainter(
          size: 12,
        ),
      ],
    );
  }
}

class GradientPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size){
    
  }
}

