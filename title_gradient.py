from manim import *
from datetime import *
from manim_fonts import *


class static_title(Scene):
    def construct(self):
        with RegisterFont("Open Sans") as fonts:
            Text.set_default(font=fonts[0])

        # background with blue gradient on the title-master
        background_gradient = ImageMobject("background_gradient.png")
        self.add(background_gradient)

        # logo from the TUD in dark blue in the upper left corner
        tud_logo = ImageMobject("TUD_Logo_HKS41_57.png")
        tud_logo.set_y(3.275)
        tud_logo.set_x(-5.7)
        tud_logo.scale(0.42)
        self.add(tud_logo)

        # placeholder that allows to left align a VGroup (invisible dot, that has the correct x-coordinate)
        align_left = Text(".", fill_opacity=0)
        align_left.set_x(-6)

        # first textblock with name and institution
        name = Text("Johannes, Storm",
                    font_size=16, weight=BOLD, fill_opacity=0.6)
        institute = Text("Institut für Statik und Dynamik",
                         font_size=16, fill_opacity=0.6)

        # align text to the desired x-offset
        textblock_1 = VGroup(align_left, name, institute)
        textblock_1.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.1)
        textblock_1.set_y(0.45)
        self.add(textblock_1)

        # second textblock with title and subtitle
        title = Text("Titelmaster",
                     font_size=32, weight=BOLD)
        subtitle = Text("Titelzusatz hinzufügen",
                        font_size=32)

        textblock_2 = VGroup(align_left, title, subtitle)
        textblock_2.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)
        textblock_2.set_y(-0.925)
        self.add(textblock_2)

        # third textblock with date, location
        timestamp = datetime.today().strftime('%d. %B %Y')
        date = Text("Dresden // " + timestamp,
                    font_size=16, fill_opacity=0.6)

        textblock_3 = VGroup(align_left, date)
        textblock_3.arrange(DOWN, center=False, aligned_edge=LEFT)
        textblock_3.set_y(-2.18)
        self.add(textblock_3)


        with RegisterFont("Poppins") as fonts:
            a = Text("Hello World", font=fonts[0])
            self.play(Write(a))