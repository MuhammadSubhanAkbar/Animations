from manim import *

class Diagram(Scene):
    def construct(self):
        def creating_circles():
            circle = Circle(
                radius= 2,
                fill_color= WHITE,
                fill_opacity= 1,
            )


            self.play(DrawBorderThenFill(circle), run_time=2)
            self.wait()