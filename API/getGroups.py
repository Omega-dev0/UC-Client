from utils.simulateAPIRequests import request


def getGroups():
    request()
    return [
        {"id": 1, "nom": "Groupe A"},
        {"id": 2, "nom": "Groupe B"},
        {"id": 3, "nom": "Groupe C"},
        {"id": 4, "nom": "Groupe D"},
    ]
