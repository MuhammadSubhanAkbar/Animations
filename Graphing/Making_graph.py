from manim import *
import numpy as np


class Graph(Scene):
    def construct(self):
        # We define the main logic here
        self.create_plane()
        self.graphing_equations()
        self.moving_value_animation()

    def create_plane(self):
        self.number_plane = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": "Teal",
                "stroke_width": 1,
                "stroke_opacity": 0.6
            },
            axis_config={
                "include_numbers": True,
                "font_size": 20,
            }
        )
        self.play(Create(self.number_plane), run_time=5)
        self.wait()

    def graphing_equations(self):
        # Define the functions
        def cos_fun(t):
            return np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t)

        def sin_fun1(t):
            return np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t)

        def sin_fun2(t):
            return (np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t) +
                    np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t))

        # Create the Graphs
        cos_graph = FunctionGraph(cos_fun, x_range=[-10, 10], color=RED)
        sin_graph1 = FunctionGraph(sin_fun1, x_range=[-10, 10], color=BLUE)
        sin_graph2 = FunctionGraph(sin_fun2, x_range=[-10, 10], color=GREEN)

        # Create Labels
        cos_label = MathTex(r"\cos(t) + \frac{1}{2}\cos(7t) + \frac{1}{7}\cos(14t)", color=RED)
        sin_label1 = MathTex(r"\sin(t) + \frac{1}{2}\sin(7t) + \frac{1}{7}\sin(14t)", color=BLUE)
        sin_label2 = MathTex(
            r"\sin(t) + \dots + \cos(t) + \dots",  # Shortened for layout
            color=GREEN)

        # Layout for labels
        labels = VGroup(cos_label, sin_label1, sin_label2).scale(0.5).arrange(DOWN, aligned_edge=LEFT)
        labels.to_corner(UL, buff=0.5)

        # Animate Graphs
        self.play(Create(cos_graph), Write(cos_label))
        self.wait(0.5)
        self.play(Create(sin_graph1), Write(sin_label1))
        self.wait(0.5)
        self.play(Create(sin_graph2), Write(sin_label2))
        self.wait(1)

    def moving_value_animation(self):
        # 1. Create the Tracker starting at -10
        tracker = ValueTracker(-10)

        # 2. Create a Dot and a DecimalNumber that stay linked to the tracker
        # always_redraw ensures they update every frame
        dot = always_redraw(lambda: Dot(
            point=self.number_plane.coords_to_point(tracker.get_value(), 0),
            color=YELLOW
        ))

        number_display = always_redraw(lambda: DecimalNumber(
            tracker.get_value(),
            num_decimal_places=1,
            color=YELLOW
        ).next_to(dot, UP))

        self.add(dot, number_display)

        # 3. The 5-second transition
        self.play(
            tracker.animate.set_value(10),
            run_time=5,
            rate_func=linear  # This keeps the speed constant
        )
        self.wait(2)