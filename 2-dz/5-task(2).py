def getRootProperty(collection, value):
    if isinstance(collection, dict):
        for key in collection:
            if getRootProperty(collection[key], value):
                return key
    elif isinstance(collection, list):
        for i in collection:
            if i == value:
                return True
        return False
    return None


object = {
    "r1n": {
        "mkg": {
            "zma": [21, 45, 66, 111],
            "mii": {
                "ltf": [2, 5, 3, 9, 21]
            },
            "fv": [1, 3, 6, 9]
        },
        "rmk": {
            "amr": [50, 50, 100, 150, 250]
        }
    },
    "fik": {
        "er": [592, 92, 32, 13],
        "gp": [12, 34, 116, 29]
    }
}

print(getRootProperty(object, 250))
print(getRootProperty(object, 116))
print(getRootProperty(object, 111))
print(getRootProperty(object, 999))