"""Loading Screen Gold entry.

Writes one loading-screen tip (65 characters) to /output/entry.txt.
Standard library only.
"""

import os

TIP = "Tip: The dragon can smell fear and also snacks. Leave the snacks."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP + "\n")
    print("wrote /output/entry.txt (%d characters)" % len(TIP))


if __name__ == "__main__":
    main()
