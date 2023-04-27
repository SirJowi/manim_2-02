from manim import *

class static_title(Scene):
    def construct(self):
        tud_darkblue = "#00305e"
        tud_lightblue = "#006ab3"

        background = Rectangle(color=tud_darkblue, fill_opacity=1.0, height=1920, width=1080, stroke_width=0, sheen_factor=0.2, sheen_direction=np.array([1., 1, 0.]))
        self.add(background)

        header = Rectangle(color=WHITE, fill_opacity=1.0, width=768, height=2.8)
        header.set_y(4)
        self.add(header)

        header_stripe = Rectangle(color=tud_lightblue, fill_opacity=0.4, stroke_opacity=0, width=768, height=0.23)
        header_stripe.set_y(2.68)
        self.add(header_stripe)

        tud_logo = ImageMobject("TUD_Logo_HKS41_228.png")
        tud_logo.set_y(3.3)
        tud_logo.set_x(-5.8)
        tud_logo.scale(0.1)
        self.add(tud_logo)

        isd_logo = ImageMobject("logo_isd_weiss.png")
        isd_logo.set_y(-2.8)
        isd_logo.set_x(-4.88)
        isd_logo.scale(0.17)
        self.add(isd_logo)

        institute_text = Text("Institut für Statik und Dynamik", font_size=11, font="OpenSans", color=tud_darkblue)
        institute_text.set_y(2.68)
        institute_text.set_x(-4.95)
        self.add(institute_text)

        text = Text("Vorname, Name", font_size=16, font="OpenSans", color="#FFFFFF")
        text.set_y(1.0)
        self.add(text)

        title = Text("Titel der Präsentation", font_size=32, font="OpenSans", color="#FFFFFF", weight=BOLD)

        textblock = VGroup(institute_text, text, title)
        textblock.arrange(DOWN, buff=1.5, center=False, aligned_edge=LEFT)
        self.add(textblock)