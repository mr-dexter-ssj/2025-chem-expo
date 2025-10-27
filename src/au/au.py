from manim import *

class auAtom(Scene):
    def construct(self):
        proton = Circle()
        proton.set_fill(RED, opacity=0.5)

        self.play(Create(proton))

        self.interactive_embed()