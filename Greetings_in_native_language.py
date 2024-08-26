DataBase = [
    ("english", "Welcome"),
    ("czech", "Vitejte"),
    ("danish", "Velkomst"),
    ("dutch", "Welkom"),
    ("estonian", "Tere tulemast"),
    ("finnish", "Tervetuloa"),
    ("flemish", "Welgekomen"),
    ("french", "Bienvenue"),
    ("german", "Willkommen"),
    ("irish", "Failte"),
    ("italian", "Benvenuto"),
    ("latvian", "Gaidits"),
    ("lithuanian", "Laukiamas"),
    ("polish", "Witamy"),
    ("spanish", "Bienvenido"),
    ("swedish", "Valkommen"),
    ("welsh", "Croeso")
]

def greet(selected_language):
    for lang, trans in DataBase:
        if lang == selected_language:
            return trans
    return "Welcome"


