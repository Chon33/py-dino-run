import json
from os import walk

def load():
    """
        Loads translated strings from json files. \n
        Returns settings and lang json files as dictionaries.
    """
    global settings, lang, available_langs

    available_langs = []
    for (_,_,files) in walk("assets/misc/lang/"):
        for file in files:
            available_langs.append(file[:-5])

    with open("assets/misc/settings.json") as s:
        settings = json.load(s)
        with open(f"assets/misc/lang/{available_langs[settings['lang']]}.json") as l:
            lang = json.load(l)
    s.close()
    l.close()
    return (settings, lang, available_langs)

def reload():
    """
        Reloads strings
    """
    global settings, lang, available_langs
    settings, lang, available_langs = load()

def save(option: str, value):
    """
        Saves values to config settings
    """
    settings[option] = value
    with open("assets/misc/settings.json", "w") as s:
        json.dump(settings, s)
    s.close()
    print(f"Saved {value} to {option}")
    reload()


settings, lang, available_langs = load()
