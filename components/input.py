from kivymd.uix.dropdownitem import MDDropDownItem, MDDropDownItemText
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard

from config import getDebugColor
import utils.storage as storage


class inputGroupWithCard(MDCard):
    def __init__(self, label, inputWidget, **kwargs):
        super().__init__(**kwargs)

        self.ripple_behavior = True
        self.size_hint = (1, None)
        self.height = "46dp"
        self.padding = "0dp"
        self.style = "outlined"
        self.md_bg_color = "#00000000"

        boxLayout = MDBoxLayout()

        boxLayout.orientation = "horizontal"
        boxLayout.padding = "8dp"
        boxLayout.spacing = "0dp"

        labelWidget = MDLabel(
            text=label,
            font_style="Label",
            size_hint=(1, None),
            height="20dp",
            padding=["8dp", 0, 0, 0],
            bold=True,
        )
        inputWidget.size_hint = (1, None)
        labelWidget.text_color = "#000000"
        boxLayout.add_widget(labelWidget)
        boxLayout.add_widget(inputWidget)
        self.add_widget(boxLayout)


class inputGroup(MDBoxLayout):
    def __init__(self, label, inputWidget, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.padding = "8dp"
        self.spacing = "0dp"
        self.height = "36dp"

        labelWidget = MDLabel(
            text=label,
            font_style="Label",
            size_hint=(1, None),
            height="20dp",
            padding=["8dp", 0, 0, 0],
            bold=True,
        )
        inputWidget.size_hint = (1, None)
        labelWidget.text_color = "#000000"
        self.md_bg_color = getDebugColor()
        self.add_widget(labelWidget)
        self.add_widget(inputWidget)


class dropdownInput(MDDropDownItem):
    def __init__(self, items, storageKey, callback, **kwargs):
        super().__init__(**kwargs)
        self._md_bg_color = getDebugColor()
        self.on_release = lambda: self.open_menu(self)

        self.callback = callback
        self.storageKey = storageKey

        self.text = MDDropDownItemText(
            id="drop_text",
            text="Item",
        )
        self.add_widget(self.text)
        self.items = items

        value = storage.get(storageKey)
        self.setValue(value)

        storage.registerCallback(storageKey, self.setValue)

    def open_menu(self, item):
        menu_items = []

        for baseItem in self.items:
            menu_items.append(
                {
                    "value": baseItem["value"],
                    "text": baseItem["text"],
                    "on_release": lambda x=baseItem: self.menu_callback(x),
                }
            )

        self.menu = MDDropdownMenu(caller=item, items=menu_items)
        self.menu.open()

    def menu_callback(self, baseItem):
        self.text.text = baseItem["text"]
        self.menu.dismiss()
        if self.callback:
            self.callback(baseItem["value"])
        storage.set(self.storageKey, baseItem["value"])

    def setValue(self, value):
        valueText = next(
            (item["text"] for item in self.items if item["value"] == value),
            "Sélectionnez une option",
        )
        self.text.text = valueText
