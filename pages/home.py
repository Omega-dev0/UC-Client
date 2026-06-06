from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel

from components.baseScreen import BaseScreen
from utils.toast import toast
from components.cards import Card


class HomeScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(
            title="Accueil",
            subtitle="Bienvenue sur la page d'accueil !",
            name="home_screen",
            **kwargs,
        )

        button = MDIconButton(icon="information", pos_hint={"center_x": 0.5})
        button.bind(on_release=lambda x: toast("Bienvenue sur la page d'accueil !"))
        self.root.add_widget(button)
