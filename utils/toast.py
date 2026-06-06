import kivy
from kivy.metrics import dp
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.snackbar import MDSnackbarActionButton
from kivymd.uix.snackbar import MDSnackbarButtonContainer
from kivymd.uix.snackbar import MDSnackbarCloseButton
from kivymd.uix.snackbar import MDSnackbarSupportingText
from kivymd.uix.snackbar import MDSnackbarActionButtonText


def toast(message):
    snackbar = MDSnackbar(
        MDSnackbarSupportingText(
            text=message,
        ),
        MDSnackbarButtonContainer(
            MDSnackbarCloseButton(
                icon="close",
            ),
            pos_hint={"center_y": 0.5},
        ),
        y=dp(24),
        orientation="horizontal",
        pos_hint={"center_x": 0.5},
        size_hint_x=0.5,
    )
    snackbar.open()
