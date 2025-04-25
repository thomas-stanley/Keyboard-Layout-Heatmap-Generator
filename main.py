import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

class Analyse:
    def __init__(self):
        self.KEYBOARD_ROWS = 3
        self.layout_to_test = input("Enter the layout to test: ").lower()
        with open(f"layouts/{self.layout_to_test}.txt", "r") as file:
            rows = [[]]
            row_index = 0
            self.name = file.readline().strip("\n")
            for character in file.read():
                if character == "\n":
                    if row_index != self.KEYBOARD_ROWS - 1:  # Must subtract one due to zero index
                        row_index += 1
                        rows.append([])
                elif character != " ":
                    rows[row_index].append(character)
            self.layout = np.array(rows).reshape(self.KEYBOARD_ROWS, -1)
            self.character_frequencies = {
                "e": 0.1249,
                "t": 0.0928,
                "a": 0.0804,
                "o": 0.0764,
                "i": 0.0757,
                "n": 0.0723,
                "s": 0.0651,
                "r": 0.0628,
                "h": 0.0505,
                "l": 0.0407,
                "d": 0.0382,
                "c": 0.0334,
                "u": 0.0273,
                "m": 0.0251,
                "f": 0.0240,
                "p": 0.0214,
                "g": 0.0187,
                "w": 0.0168,
                "y": 0.0166,
                "b": 0.0148,
                "v": 0.0105,
                "k": 0.0054,
                "x": 0.0023,
                "j": 0.0016,
                "q": 0.0012,
                "z": 0.0009,
                ".": 0,
                ",": 0,
                "/": 0,
                ";": 0,
                "'": 0,
                '"': 0,
                "-": 0,
                "?": 0,
                "#": 0
            }
    
    def apply_to_layout(self):
        key_rows = []
        for row in self.layout:
            key_rows.append([])
            for character in row:
                key_rows[-1].append(self.character_frequencies[character])
        self.key_frequencies = np.array(key_rows).reshape(self.KEYBOARD_ROWS, -1)
    

    def show(self):
        row_names = ["Top Row", "Home Row", "Bottom Row"]
        column_names = ["Left Little", "Left Ring", "Left Middle", "Left Index", "Left Index", 
        "Right Index", "Right Index", "Right Middle", "Right Ring", "Right Little"]
        fig, ax = plt.subplots()
        im = ax.imshow(self.key_frequencies)
        
        ax.set_xticks(range(len(column_names)), labels=column_names,
        rotation=45, ha="right", rotation_mode="anchor")

        ax.set_yticks(range(len(row_names)), labels=row_names)


        cmap = im.get_cmap()
        norm = im.norm

        for i in range(len(row_names)):
            for j in range(len(column_names)):
                value = self.key_frequencies[i, j]
                rgba = cmap(norm(value))
                r, g, b, _ = rgba
                luminance = 0.299 * r + 0.587 * g + 0.114 * b
                text_color = "black" if luminance > 0.5 else "white"
                ax.text(j, i, self.layout[i, j],
                        ha="center", va="center", color=text_color)

        cbar = plt.colorbar(im, ax=ax, location="bottom", pad=0.2, label="Character Frequency", ticks=[0, 0.1249])
        cbar.ax.set_xticklabels(["Low", "High"])

        ax.set_title(self.name)
        fig.tight_layout()
        plt.savefig(f"{self.layout_to_test}.png", bbox_inches="tight", pad_inches=0.25)
        plt.show()






def main():
    test = Analyse()
    test.apply_to_layout()
    test.show()

if __name__ == "__main__":
    main()
