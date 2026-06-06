from kivy.storage.jsonstore import JsonStore
from utils.debug import log

store = JsonStore("data.json")

callbacks = {}


def registerCallback(key, callback):
    if not store.exists(key):
        store.put(key, value=None)
    if key not in callbacks:
        callbacks[key] = []
    callbacks[key].append(callback)


def get(key):
    return store.get(key)["value"] if store.exists(key) else None


def set(key, value):
    log(f"Setting storage key '{key}' to value:", value)
    previousValue = get(key)
    if previousValue == value:
        return
    store.put(key, value=value)
    if key in callbacks:
        for callback in callbacks[key]:
            callback(value)
