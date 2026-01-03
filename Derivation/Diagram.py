from manim import *

def creating_circles(self):
    circle1 = Circle(
        radius=2,
        fill_color=WHITE,
        fill_opacity=1,
        stroke_color=WHITE
    )

    circle2 = circle1.copy()

    # Draw circles first - ADD WAIT
    self.play(
        DrawBorderThenFill(circle1),
        DrawBorderThenFill(circle2),
        run_time=1.5
    )
    self.wait(0.5)  # ADDED: Pause to see circles

    # Scale down and bring closer
    self.play(
        circle1.animate.scale(0.2).shift(UR * 3),
        circle2.animate.scale(0.2).shift(UL * 3),
        run_time=1.5
    )
    self.wait(0.5)  # ADDED: Pause after movement

    arrow = Arrow(
        start=circle1.get_center(),
        end=circle2.get_center(),
    )

    # Create labels
    label1 = MathTex("q_1", font_size=40, color=BLACK)
    label2 = MathTex("q_2", font_size=40, color=BLACK)

    label1.move_to(circle1.get_center())
    label2.move_to(circle2.get_center())

    # Create arrow between circles
    arrow = Arrow(
        start=circle1.get_center(),
        end=circle2.get_center(),
        color=YELLOW,
        stroke_width=6,
        buff=0.3,  # Add buffer so arrow doesn't touch circles
        max_tip_length_to_length_ratio=0.15  # Control tip size
    )

    # Alternatively, use DoubleArrow for both directions
    # arrow = DoubleArrow(
    #     start=circle1.get_center(),
    #     end=circle2.get_center(),
    #     color=YELLOW,
    #     stroke_width=6,
    #     buff=0.3
    # )

    # Add arrow animation
    self.play(
        Create(arrow),
        run_time=1
    )
    self.wait(0.5)

    # Then add labels
    self.play(
        Write(label1),
        Write(label2),
        run_time=1
    )
    self.wait(1)  # ADDED: Pause to see labels

    # Create explanation text
    Explanation = Text(
        "Two charged particles with charges q₁ and q₂",
        font_size=36
    )

    # Add explanation text
    self.play(
        Write(Explanation),
        run_time=1.5
    )
    self.wait(2)  # Final pause


# Keep the class for standalone use
class CircleAnimation(Scene):
    def construct(self):
        creating_circles(self)  # Use the function