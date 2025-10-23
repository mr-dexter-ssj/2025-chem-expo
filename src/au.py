from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle1 = Circle(radius=0.5)
        circle1.set_fill(opacity=0.5)
        circle1.set_stroke(RED, width=4)

        circle1 = Circle(radius=0.5)
        circle1.set_fill(opacity=0.5)
        circle1.set_stroke(RED, width=4)

        circle1 = Circle(radius=0.5)
        circle1.set_fill(opacity=0.5)
        circle1.set_stroke(RED, width=4)

        circle1 = Circle(radius=0.5)
        circle1.set_fill(opacity=0.5)
        circle1.set_stroke(RED, width=4)

        circle1 = Circle(radius=0.5)
        circle1.set_fill(opacity=0.5)
        circle1.set_stroke(RED, width=4)

        self.add(circle1)