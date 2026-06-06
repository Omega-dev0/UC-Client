from kivymd.uix.card import MDCard
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.widget import MDWidget
from kivy.graphics import Color, Line


class Card(MDCard):
    def __init__(self, title, style, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = ("240dp", "100dp")
        self.padding = "4dp"
        self.ripple_behavior = True
        self.style = style

        cardLayout = MDAnchorLayout(anchor_y="top", padding="8dp")
        cardTitle = MDLabel(text=title, halign="left")
        cardLayout.add_widget(cardTitle)
        self.add_widget(cardLayout)


class BorderedBoxLayout(MDBoxLayout):
    def __init__(self, color, width, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            self.border_color = color
            self.border_line = Line(width=width)

        self.bind(pos=self._update_border, size=self._update_border)

    def _update_border(self, *args):
        self.border_line.rectangle = (self.x, self.y, self.width, self.height)
