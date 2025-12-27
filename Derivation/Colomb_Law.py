from manim import *
from Diagram import creating_circles

class Derivation(Scene):
    def construct(self):

        def main():
            definition()
            self.wait(0.5)

            #Creating circles
            creating_circles(self)
            self.wait(2)

        # Text description
        def definition():
            colomb_law = MathTex(
                r"\text{The electrostatic force between two stationary charged particles,}",
                r"\text{stating it's directly proportional to the product of their charges}",
                r"\text{and inversely proportional to the square of the distance between them}"
            )

            # Equation
            colomb_eq = MathTex(r"F = k \frac{q_1 q_2}{r^2}")

            #Question
            que = Text("Where this came from?")

            # Scale both
            colomb_law.scale(0.5)
            colomb_eq.scale(0.8)  # Changed to 0.8 so equation is larger than text

            # Arrange the text lines (only for colomb_law which has multiple lines)
            colomb_law.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

            # Position them
            colomb_law.to_edge(UP, buff=1)
            colomb_eq.next_to(colomb_law, DOWN, buff=0.8)  # Position equation below text

            # Animate
            self.play(Write(colomb_law), run_time=3)
            self.wait(1)
            self.play(Write(colomb_eq))
            self.wait(2)

            #Adding question
            self.play(FadeOut(colomb_law), FadeOut(colomb_eq))
            self.wait(.5)
            self.play(FadeIn(que)) #Adding the question

            self.wait(.5)
            self.play(FadeOut(que)) #Fading out the equation

        main()