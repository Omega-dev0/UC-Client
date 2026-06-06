from kivy.config import Config

Config.set("graphics", "width", "360")
Config.set("graphics", "height", "740")
Config.set("graphics", "resizable", False)


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel

from kivy.utils import platform

from components.navbar import FloatingNavbar
from components.gradient import GradientBackground

from pages.home import HomeScreen
from pages.settings import SettingsScreen
from pages.creation import CreationScreen

from utils.gps import startGPS
from utils.debug import log

log("Platform:", platform)


class NavigationApp(MDApp):
    def build(self):
        root_layout = MDFloatLayout()

        background = GradientBackground(size_hint=(1, 1), pos_hint={"x": 0, "y": 0})
        root_layout.add_widget(background)

        sm = MDScreenManager()

        sm.add_widget(HomeScreen())
        sm.add_widget(SettingsScreen())
        sm.add_widget(CreationScreen())

        root_layout.add_widget(sm)
        # 1
        navbar = FloatingNavbar(screen_manager=sm)
        root_layout.add_widget(navbar)

        return root_layout


if __name__ == "__main__":
    NavigationApp().run()
