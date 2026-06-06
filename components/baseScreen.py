from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.anchorlayout import MDAnchorLayout


from components.labels import PageKicker


from config import COLORS, getDebugColor


class BaseScreen(MDScreen):
    """Classe de base pour afficher le contenu d'une page."""

    def __init__(self, title, subtitle, **kwargs):
        super().__init__(**kwargs)

        self.md_bg_color = [0, 0, 0, 0]

        self.root = MDBoxLayout(
            orientation="vertical", size_hint=(1, 1), pos_hint={"top": 1}
        )
        self.root.md_bg_color = getDebugColor()

        topBanner = MDBoxLayout(
            orientation="vertical",
            size_hint=(1, None),
            height="60dp",
            pos_hint={"top": 1},
        )
        topBanner.md_bg_color = COLORS["primary"]
        self.root.add_widget(topBanner)

        header = MDBoxLayout(
            orientation="vertical",
            size_hint=(1, None),
            height="60dp",
            pos_hint={"top": 1},
        )
        header._md_bg_color = getDebugColor()
        self.root.add_widget(header)

        self.content = MDAnchorLayout(
            anchor_y="top", pos_hint={"top": 1}, padding="8dp"
        )
        self.content._md_bg_color = getDebugColor()
        label = PageKicker(text=title)
        label.pos_hint = {"top": 1}

        subtitle = MDLabel(
            text=subtitle,
            font_style="Title",
            size_hint=(1, None),
            role="medium",
            height="20dp",
            padding=["8dp", 0, 0, "8dp"],
            bold=True,
        )
        subtitle.text_color = "#000000"

        label.size_hint = (1, None)
        label.adaptive_height = True

        header.add_widget(label)
        header.add_widget(subtitle)
        self.root.add_widget(self.content)
        self.add_widget(self.root)
