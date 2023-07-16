from manim import *
class PitagorasScene2(Scene):
    def construct(self):
        circle=Circle(radius=1)
        triangle=Triangle()
        circle.add(triangle)
        triangle.shift(2*RIGHT)
        square=Square().shift(2*UP)
        circle.add(square)
        self.play(
            Create(circle[1:]),
        )
        self.wait()