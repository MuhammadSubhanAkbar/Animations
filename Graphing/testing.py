from manim import *
import numpy as np

class testing(Scene):
    def construct(self):

        def main():
            graphing_equations()

        def graphing_equations():
            def cos_fun(t):
                return np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t)

            def sin_fun1(t):
                return np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t)

            def sin_fun2(t):
                return np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t) + np.cos(t) + 0.5 * np.cos(7 * t) + (
                            1 / 7) * np.cos(14 * t)  # Fixed: added

            cos_graph = FunctionGraph(
                cos_fun,
                x_range=[-10, 10],
                color=RED
            )

            sin_graph1 = FunctionGraph(
                sin_fun1,
                x_range=[-10, 10],
                color=BLUE
            )

            sin_graph2 = FunctionGraph(
                sin_fun2,
                x_range=[-10, 10],
                color=GREEN
            )

            # Add labels if needed
            cos_label = MathTex(r"\cos(t) + \frac{1}{2}\cos(7t) + \frac{1}{7}\cos(14t)", color=RED)
            sin_label1 = MathTex(r"\sin(t) + \frac{1}{2}\sin(7t) + \frac{1}{7}\sin(14t)", color=BLUE)
            sin_label2 = MathTex(
                r"\sin(t) + \frac{1}{2}\sin(7t) + \frac{1}{7}\sin(14t) +cos(t) + \frac{1}{2}\cos(7t) + \frac{1}{7}\cos(14t) ",
                color=GREEN)  # Fixed: quote is actually fine here

            for label in [cos_label, sin_label1, sin_label2]:
                label.scale(0.5)

            # Position labels
            cos_label.to_corner(UL)
            sin_label1.next_to(cos_label, DOWN)
            sin_label2.next_to(sin_label1, UR)

            # Animate
            self.play(Create(cos_graph), Write(cos_label))
            self.wait(1)
            self.play(Create(sin_graph1), Write(sin_label1))
            self.wait(1)
            self.play(Create(sin_graph2), Write(sin_label2))
            self.wait(2)

        main()