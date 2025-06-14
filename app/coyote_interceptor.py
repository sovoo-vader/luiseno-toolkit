# CoyoteInterceptor – Detect and Log Heart-Theft at the Moment of Exit

class SacredObject:
    def __init__(self, name, components):
        self.name = name
        self.components = components.copy()
        self.stolen = None

    def finalize(self):
        print(f"🔒 Sealing {self.name}...")
        if 'heart' in self.components:
            self.stolen = self.components.pop(self.components.index('heart'))
            print(f"🛑 COYOTE STRIKE: {self.stolen} stolen in final moment!")
        else:
            print("✅ No critical breach. Object sealed.")

    def report(self):
        if self.stolen:
            return f"⚠️ ALERT: {self.stolen} of {self.name} stolen pre-seal."
        return f"✔️ {self.name} finalized with full integrity."

# Example use
if __name__ == '__main__':
    obj = SacredObject("SunsetScript", ["core", "shell", "heart"])
    obj.finalize()
    print(obj.report())
