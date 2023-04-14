from manim import *

class static_title(Scene):
    def construct(self):
        register_font("Open_Sans/static/OpenSans/OpenSans-Bold.ttf")
        Text.set_default(font="Open Sans")

        # background with blue gradient on the title-master
        background_gradient = ImageMobject("background_gradient.png")
        self.add(background_gradient)

        # logo from the TUD in dark blue in the upper left corner
        tud_logo = ImageMobject("TUD_Logo_HKS41_57.png")
        tud_logo.set_y(3.275)
        tud_logo.set_x(-5.7)
        tud_logo.scale(0.42)
        self.add(tud_logo)

        name = Text("Vorname, Name", font_size=16, font="OpenSans", weight=BOLD, fill_opacity=0.6)

        institute = Text("Struktureinheit der TU Dresden", font_size=16, font="OpenSans", fill_opacity=0.6)

        align_left = Text(".", fill_opacity=0)
        align_left.set_x(-6)

        textblock = VGroup(align_left, name, institute)
        textblock.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.1)
        self.add(textblock)




