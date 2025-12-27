from manim import *

class Diagram(Scene):
    def construct(self):
        def main():
            creating_circles()

        def creating_circles():
            circle = Circle(
                radius= 2,
                fill_color= WHITE,
                fill_opacity= 1,
                stroke_color=WHITE
            )

            circle2 = Circle(
                radius= 2,
                fill_color= WHITE,
                fill_opacity= 1,
                stroke_color=WHITE
            )


            self.play(DrawBorderThenFill(circle), DrawBorderThenFill(circle2), run_time=2)
            self.wait()

            #Changing the 1circle position
            self.play(circle.animate.scale(0.2), circle2.animate.scale(0.2), run_time= 1)
            self.play(circle.animate.shift(RIGHT*4), circle2.anm, run_time= 1)
            self.wait()


        main()