# LanguageOSRestorer – Map Morphemes from Baskets, Chants, and Place to Restore Cognitive Schema

morpheme_db = {
    "pax": {
        "meaning": "sky or spirit",
        "domain": "chant",
        "example": "pax-mi-toy (sky-path dreaming)"
    },
    "-kwee": {
        "meaning": "motion / toward",
        "domain": "basket suffix",
        "example": "sapokwee (rising wrap)"
    },
    "yaha": {
        "meaning": "earth or center",
        "domain": "place root",
        "example": "Yahatuli (central camp in canyon)"
    },
    "tsi": {
        "meaning": "binding, weaving, closing",
        "domain": "basket & grammar",
        "example": "Tsiwanuk (she-who-binds)"
    }
}

def restore_from_morpheme(morph):
    item = morpheme_db.get(morph.lower())
    if not item:
        return "⚠️ Unknown morpheme."
    return f"🧠 Root: {morph}\n📚 Meaning: {item['meaning']}\n🌐 Domain: {item['domain']}\n🗣️ Example: {item['example']}"

# Example use
if __name__ == '__main__':
    print(restore_from_morpheme("tsi"))
