from manim import *
from datetime import *


class static_basic(Scene):
    def construct(self):
        tud_darkblue = "#00305e"
        tud_lightblue = "#006ab3"
        tud_grey = "#A6A6A6"

        background = Rectangle(color=WHITE, fill_opacity=1.0, height=1920, width=1080, stroke_width=0)
        self.add(background)

        # logo from the TUD in dark blue in the lower left corner
        tud_logo = ImageMobject("TUD_Logo_HKS41_228.png")
        tud_logo.set_x(-5.85)
        tud_logo.set_y(-3.5)
        tud_logo.scale(0.065)
        self.add(tud_logo)

        # setting up default font
        Text.set_default(font="Open Sans")

        # placeholder that allows to align a VGroup (invisible dot, that has the correct x-coordinate)
        align_left = Text(".", fill_opacity=0)
        align_left.set_x(-4.15)


        # first textblock with name and institution
        timestamp = datetime.today().strftime('%d. %B %Y')
        title = Text("Mastertitel - Titelzusatz",
                     font_size=160, color="#727277").scale(0.05)
        institute = Text("Institut für Statik und Dynamik / Johannes, Storm",
                         font_size=160, color="#727277").scale(0.05)
        date = Text("Dresden // " + timestamp,
                    font_size=160, color="#727277").scale(0.05)

        textblock_1 = VGroup(align_left, title, institute, date)
        textblock_1.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.05)
        textblock_1.set_y(-3.43)
        self.add(textblock_1)
