# MythicEtymologyExplorer - Traverse and Decode the Origins of Mythic Place Names

import json

# Example database of mythic etymologies from Spanish/Indigenous layers
etymology_db = {
    "California": {
        "source": "Las Sergas de Esplandián (1510)",
        "meaning": "Fictional island ruled by black Amazons, near paradise",
        "origin_language": "Spanish literary (with possible Greek/Latin mix)",
        "notes": "Name later applied by Cortés after hearing legends of a gold-rich land"
    },
    "Tamalpais": {
        "source": "Miwok language",
        "meaning": "Sleeping maiden or coast mountain",
        "origin_language": "Indigenous (Miwok)",
        "notes": "Often mythologized as a giant maiden lying in the hills"
    },
    "El Cajón": {
        "source": "Spanish",
        "meaning": "The box",
        "origin_language": "Spanish",
        "notes": "Describes canyon with box-like geological structure"
    },
    "Temecula": {
        "source": "Luiseño legend",
        "meaning": "Place of sun or where the sun breaks through mist",
        "origin_language": "Indigenous (Luiseño)",
        "notes": "First named by traveling tribal elder giving names to sacred locations"
    }
}

def explore_etymology(name):
    key = name.strip().title()
    if key in etymology_db:
        return json.dumps(etymology_db[key], indent=2)
    return f"No data for '{name}'."

# Example use
if __name__ == '__main__':
    for query in ["California", "Tamalpais", "Temecula", "Tia Juana"]:
        print(f"\nEtymology of {query}:")
        print(explore_etymology(query))
