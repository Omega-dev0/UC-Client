"""Utility for simulating a simple API request."""

from urllib.request import urlopen


def request() -> str:
    try:
        with urlopen("https://jsonplaceholder.typicode.com/todos/1") as response:
            return response.read().decode("utf-8")
    except Exception as e:
        return f"Error: {e}"
