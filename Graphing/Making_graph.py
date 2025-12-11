from manim import *


class Graph(Scene):
    def construct(self):
        def main():
            adding()

        def create_plane():
            number_plane = NumberPlane(
                x_range=[-10, 10, 1],
                y_range=[-10, 10, 1],
                background_line_style={
                    "stroke_color": "Teal",
                    "stroke_width": 1,
                    "stroke_opacity": 0.6
                },
                # Add this to show coordinates automatically
                axis_config={
                    "include_numbers": True,  # This adds numbers to axes
                    "font_size": 20,  # Adjust font size
                }
            )
            return number_plane

        def adding():
            plane = create_plane()
            self.play(Create(plane), run_time=4)
            self.wait()



        main()