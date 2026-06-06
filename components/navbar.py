from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.navigationbar import (
    MDNavigationBar,
    MDNavigationItem,
    MDNavigationItemIcon,
    MDNavigationItemLabel,
)
from kivy.uix.screenmanager import (
    ScreenManager,
    Screen,
    SlideTransition,
    WipeTransition,
    NoTransition,
)

from config import COLORS


class FloatingNavbar(MDNavigationBar):

    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        self.size_hint = (None, None)
        self.size = ("320dp", "80dp")
        self.pos_hint = {"center_x": 0.5, "y": 0.03}

        self.radius = ["28dp", "28dp", "28dp", "28dp"]

        self.bind(on_switch_tabs=self.on_tab_switch)

        item_home = MDNavigationItem(active=True)
        item_home.add_widget(MDNavigationItemIcon(icon="home"))
        # item_home.add_widget(MDNavigationItemLabel(text="Accueil"))
        # item_home.indicator_color = COLORS["primary"]
        item_home.screen_target = "home_screen"  # type: ignore

        item_search = MDNavigationItem()
        item_search.add_widget(MDNavigationItemIcon(icon="plus"))
        item_search.screen_target = "creation_screen"  # type: ignore
        item_search.indicator_color = COLORS["primary"]

        item_settings = MDNavigationItem()
        icon = MDNavigationItemIcon(
            icon="cog",
            icon_color_normal=COLORS["primary"],
            icon_color_active=COLORS["primary"],
        )
        item_settings.add_widget(icon)
        # item_settings.add_widget(MDNavigationItemLabel(text="Options"))
        item_settings.screen_target = "settings_screen"  # type: ignore

        self.add_widget(item_home)
        self.add_widget(item_search)
        self.add_widget(item_settings)

    def on_tab_switch(self, bar, item, item_icon, item_text):

        screens = [
            "home_screen",
            "creation_screen",
            "settings_screen",
        ]
        currentIndex = screens.index(self.screen_manager.current)
        requestedIndex = screens.index(item.screen_target)

        direction = "left" if requestedIndex > currentIndex else "right"

        self.screen_manager.transition = SlideTransition(duration=0.3)
        self.screen_manager.transition.direction = direction
        self.screen_manager.current = item.screen_target
