from manim import *
import numpy as np


class Equation():
    def construct(self):

        #Making the equation
        def equation():
            def cos_fun():
                cos_function = FunctionGraph(
                    lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
                    color=RED,
                )

            def sin_fun1():
                sin_function = FunctionGraph(
                    lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
                    color=BLUE,
                )
            def sin_fun2():
                sin_function2 = FunctionGraph(
                    lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
                    x_range=[-4, 4],
                    color=GREEN,
                )
            return cos_fun(), sin_fun1(), sin_fun2()
