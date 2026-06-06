from plyer import gps
from utils.debug import log
from kivy.utils import platform

# TODO

lastLocations = []


def on_location(**kwargs):
    log("Location:", kwargs)
    # TODO


def on_status(status):
    log("GPS Status:", status)


def startGPS():
    try:
        gps.start(minTime=100, minDistance=0)  # type: ignore
        log("GPS started")
    except NotImplementedError:
        log("GPS is not implemented on this platform")


# gps.configure(on_location=on_location, on_status=on_status)
if platform in ("android", "ios"):
    gps.configure(on_location=on_location, on_status=on_status)  # type: ignore
    startGPS()
else:
    log("GPS is not supported on this platform")
    lastLocations = [
        {
            "age": 99999999999999999,
        }
    ]


def getLocation():
    # TODO avg last 10 locations, eliminate outliers, etc
    return
