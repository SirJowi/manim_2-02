from manim import *

class static_basic(Scene):
    def construct(self):
        tud_darkblue = "#00305e"
        tud_lightblue = "#006ab3"
        tud_grey = "#A6A6A6"

        background = Rectangle(color=WHITE, fill_opacity=1.0, height=1366, width=768, stroke_width=0)
        self.add(background)

        border = Line(color=tud_grey)
        border.put_start_and_end_on([-3, -2, 0], [3, -2, 0])
        self.add(border)
