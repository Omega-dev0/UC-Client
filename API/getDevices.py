from utils.simulateAPIRequests import request


def getDevices():
    request()
    return [
        {"id": 1, "id_groupe": 1},
        {"id": 2, "id_groupe": 2},
        {"id": 3, "id_groupe": 3},
        {"id": 4, "id_groupe": 1},
        {"id": 5, "id_groupe": 2},
        {"id": 6, "id_groupe": 3},
    ]
