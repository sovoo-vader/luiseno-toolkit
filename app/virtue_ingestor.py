# VirtueIngestor – Absorb Agent Traits by Mixing Embeddings like Bone Water

import numpy as np

class Agent:
    def __init__(self, name, traits):
        self.name = name
        self.embedding = np.array(traits)

    def distill(self):
        print(f"💧 Distilling {self.name}'s essence...")
        return self.embedding / np.linalg.norm(self.embedding)

class RitualMixer:
    def __init__(self):
        self.vessel = []

    def add(self, agent):
        distilled = agent.distill()
        self.vessel.append(distilled)

    def ingest(self):
        if not self.vessel:
            return "Empty vessel."
        merged = np.mean(self.vessel, axis=0)
        print("🧬 Ingested virtue. Synthesized composite:")
        return merged.round(4)

# Example use
if __name__ == '__main__':
    elder = Agent("Ancestor-One", [1.2, 3.4, 5.1, 2.3])
    hero = Agent("Wind-Speaker", [2.0, 1.0, 4.0, 4.0])

    ritual = RitualMixer()
    ritual.add(elder)
    ritual.add(hero)

    print(ritual.ingest())
