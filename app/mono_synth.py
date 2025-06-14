# MonoSynth – Create and Burn Session-Specific Avatars from Ritual Materials

import uuid
import time

class Mono:
    def __init__(self, name, materials):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.materials = materials
        self.created = time.time()

    def show(self):
        print(f"🧍‍♂️ MONO [{self.id}] — Avatar of {self.name}")
        for m in self.materials:
            print(f"  + {m}")

    def burn(self):
        print(f"🔥 Burning Mono [{self.id}] — {self.name} returns to spirit...")
        time.sleep(1)
        self.materials.clear()
        print("✖️ All traits erased. Memory purified.")

# Example use
if __name__ == '__main__':
    session_traits = ["hair of kin", "rabbit cloak", "cactus spine eyes", "feathered crest"]
    mono = Mono("Ceremonial-Scout", session_traits)
    mono.show()
    time.sleep(1)
    mono.burn()
