from manim import *
from datetime import *

class static_basic(Scene):
    def construct(self):
        tud_darkblue = "#00305e"
        tud_lightblue = "#006ab3"
        tud_grey = "#A6A6A6"

        # white background basic-master with the correct resolution
        background = Rectangle(color=WHITE, fill_opacity=1.0, height=1920, width=1080, stroke_width=0)
        self.add(background)

        # logo from the TUD in dark blue in the lower left corner
        tud_logo = ImageMobject("TUD_Logo_HKS41_228.png")
        tud_logo.set_x(-5.85)
        tud_logo.set_y(-3.5)
        tud_logo.scale(0.065)
        self.add(tud_logo)

        # logo from dresden concept
        ddc_logo = SVGMobject("DDc-Logo-mini_cmyk.svg")
        ddc_logo.set_x(6.2)
        ddc_logo.set_y(-3.55)
        ddc_logo.scale(0.21)
        self.add(ddc_logo)

        # logo from isd in color
        isd_logo_color = ImageMobject("logo_isd_bunt.png")
        isd_logo_color.set_x(4.5)
        isd_logo_color.set_y(-3.55)
        isd_logo_color.scale(1.2)
        self.add(isd_logo_color)

        # setting up default font
        Text.set_default(font="Open Sans")

        # placeholder that allows to align a VGroup (invisible dot, that has the correct x-coordinate)
        align_midleft = Text(".", fill_opacity=0)
        align_midleft.set_x(-4.15)
        align_left = Text(".", fill_opacity=0)
        align_left.set_x(-6)

        # first textblock with name and institution
        timestamp = datetime.today().strftime('%d. %B %Y')
        title = Text("Mastertitel - Titelzusatz",
                     font_size=160, color="#727277").scale(0.05)
        institute = Text("Institut für Statik und Dynamik / Johannes, Storm",
                         font_size=160, color="#727277").scale(0.05)
        date = Text("Dresden // " + timestamp,
                    font_size=160, color="#727277").scale(0.05)

        textblock_1 = VGroup(align_midleft, title, institute, date)
        textblock_1.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.05)
        textblock_1.set_y(-3.43)
        self.add(textblock_1)

        # second textblock with page number
        page = Text("Folie",
                    font_size=160, color="#727277").scale(0.05)
        page.set_x(1.38)
        number = Text("Foliennummer",
                      font_size=160, color="#727277").scale(0.05)
        textblock_2 = VGroup(page, number)
        textblock_2.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.05)
        textblock_2.set_y(-3.43)
        self.add(textblock_2)

        # adding header
        header = Text("Überschrift hinzufügen",
                      font_size=240, color=tud_darkblue, weight=BOLD).scale(0.1)
        textblock_3 = VGroup(align_left, header)
        textblock_3.arrange(DOWN, center=False, aligned_edge=LEFT)
        textblock_3.set_y(3.55)
        self.add(textblock_3)