from time import time

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.loadingindicator import MDLoadingIndicator
from kivymd.uix.card import MDCard
from kivymd.uix.relativelayout import MDRelativeLayout

from components.baseScreen import BaseScreen
from components.cards import Card, BorderedBoxLayout
from components.input import dropdownInput, inputGroup

from config import COLORS, getDebugColor

from API.getDevices import getDevices
from API.getGroups import getGroups

from utils.debug import log


class SettingsScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(
            title="Settings",
            subtitle="Paramètres de l'application",
            name="settings_screen",
            **kwargs,
        )

        label = MDLabel(
            text="Ceci est la page des paramètres!",
            halign="center",
            pos_hint={"top": 0.5},
        )
        # self.content.add_widget(label)

        self.loading = MDLoadingIndicator(
            shape_size="100dp",
            id="loading",
            pos_hint={"center_x": 0.5, "top": 0.7},
        )
        self.content.add_widget(self.loading)

    def on_enter(self):
        self.loading.start()
        devices = getDevices()
        groups = getGroups()

        self.loading.stop()
        self.content.clear_widgets()

        IdentifiantsGroupe = MDBoxLayout(
            orientation="vertical",
            size_hint=(1, None),
            height="108dp",
            radius=[8, 8, 8, 8],
            md_bg_color=getDebugColor(),
        )

        groupSelect = inputGroup(
            label="Groupe",
            inputWidget=dropdownInput(
                items=[
                    {"text": group["nom"], "value": group["id"]} for group in groups
                ],
                storageKey="group",
                callback=None,
            ),
        )
        groupSelect.size_hint = (1, None)
        groupSelect.pos_hint = {"center_x": 0.5}
        IdentifiantsGroupe.add_widget(groupSelect)

        deviceSelect = inputGroup(
            label="Identifiant de l'appareil",
            inputWidget=dropdownInput(
                items=[
                    {"text": str(device["id"]), "value": device["id"]}
                    for device in devices
                ],
                storageKey="device",
                callback=None,
            ),
        )
        deviceSelect.size_hint = (1, None)
        deviceSelect.pos_hint = {"center_x": 0.5}
        IdentifiantsGroupe.add_widget(deviceSelect)
        self.content.add_widget(IdentifiantsGroupe)
