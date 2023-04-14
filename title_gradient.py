from manim import *
from datetime import *

class static_title(Scene):
    def construct(self):
        # background with blue gradient on the title-master
        background_gradient = ImageMobject("background_gradient.png")
        self.add(background_gradient)

        # logo from the TUD in dark blue in the upper left corner
        tud_logo = ImageMobject("TUD_Logo_HKS41_57.png")
        tud_logo.set_y(3.275)
        tud_logo.set_x(-5.7)
        tud_logo.scale(0.42)
        self.add(tud_logo)

        Text.set_default(font="Open Sans")

        # placeholder that allows to left align a VGroup (invisible dot, that has the correct x-coordinate)
        align_left = Text(".", fill_opacity=0)
        align_left.set_x(-6)

        # first textblock with name and institution
        name = Text("Johannes, Storm",
                    font_size=160, weight=BOLD, fill_opacity=0.6).scale(0.1)
        institute = Text("Institut für Statik und Dynamik",
                         font_size=160, fill_opacity=0.6).scale(0.1)

        # align text to the desired x-offset
        textblock_1 = VGroup(align_left, name, institute)
        textblock_1.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.1)
        textblock_1.set_y(0.45)
        self.add(textblock_1)

        # second textblock with title and subtitle
        title = Text("Titelmaster",
                     font_size=320, weight=BOLD).scale(0.1)
        subtitle = Text("Titelzusatz hinzufügen",
                        font_size=320).scale(0.1)

        textblock_2 = VGroup(align_left, title, subtitle)
        textblock_2.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)
        textblock_2.set_y(-0.925)
        self.add(textblock_2)

        # third textblock with date, location
        timestamp = datetime.today().strftime('%d. %B %Y')
        date = Text("Dresden // " + timestamp,
                    font_size=160, fill_opacity=0.6).scale(0.1)

        textblock_3 = VGroup(align_left, date)
        textblock_3.arrange(DOWN, center=False, aligned_edge=LEFT)
        textblock_3.set_y(-2.18)
        self.add(textblock_3)
