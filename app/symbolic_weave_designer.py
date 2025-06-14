# SymbolicWeaveDesigner – Compose and Visualize Basket Motifs Using Cultural Design Language

import matplotlib.pyplot as plt

# Define some motif structures for symbolic composition
motif_shapes = {
    "venii-gemaa": [(0,0), (1,0.5), (2,0), (1,-0.5), (0,0)],  # flint shape
    "veniirpeLaa": [(0,0), (0.5,1), (1,0), (0,0)],           # triangle
    "qaxkwilee": [(0,0), (1,1), (2,0), (3,1)],               # sturgeon zigzag
    "okwEgetsip": [(0,0), (0,1), (1,0), (1,1)],              # spread fingers
    "vutsierau": "circle",
    "waxpoo": [(0,0), (1,1), (2,0), (1,-1), (1,0)],          # bisected trapezoid
}

# Simple motif placement logic
def draw_motif(name, base_x=0, base_y=0, color='black'):
    shape = motif_shapes.get(name)
    if shape == "circle":
        circle = plt.Circle((base_x + 1, base_y), 1, color=color, fill=False)
        plt.gca().add_patch(circle)
    elif shape:
        x_vals = [x + base_x for x, y in shape]
        y_vals = [y + base_y for x, y in shape]
        plt.plot(x_vals, y_vals, color=color)

# Composite designer
def compose_weave(sequence):
    plt.figure(figsize=(8, 4))
    for i, (motif, color) in enumerate(sequence):
        draw_motif(motif, base_x=i*3, base_y=0, color=color)
    plt.axis('equal')
    plt.axis('off')
    plt.title("Symbolic Basket Weave Design")
    plt.show()

# Example use
if __name__ == '__main__':
    sample_sequence = [
        ("venii-gemaa", "black"),
        ("veniirpeLaa", "red"),
        ("qaxkwilee", "black"),
        ("okwEgetsip", "gray"),
        ("vutsierau", "orange"),
        ("waxpoo", "purple")
    ]
    compose_weave(sample_sequence)
