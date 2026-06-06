from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from config import COLORS


class PageKicker(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_style = "Title"
        self.role = "large"
        self.font_size = "15sp"
        self.bold = True
        self.padding = ["8dp", 0, 0, "8dp"]

        self.text_color = COLORS["primary-strong"]

        title = self.text.upper()
        spaced_title = "\u200a".join(title)
        self.text = spaced_title
