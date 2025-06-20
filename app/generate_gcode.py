import os
import json
import random

# === CONFIG ===
PROFILE_PATH = "profiles/stake_profile.json"
CODES_FILE = "input/codes.txt"
OUTPUT_DIR = "output_gcode/"

# Simulated letter width and height
LETTER_WIDTH = 10
LETTER_HEIGHT = 15
SPACING = 5

def load_profile(profile_path):
    with open(profile_path, 'r') as f:
        return json.load(f)

def read_codes(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def generate_gcode_for_code(code, profile):
    lines = []
    x = 0
    y = 0

    lines.append("G21 ; set units to mm")
    lines.append("G90 ; use absolute positioning")

    for char in code:
        # Randomize variation
        tilt = random.uniform(*profile["variation"]["tilt"])
        height = random.uniform(*profile["variation"]["height"])
        jitter = random.uniform(*profile["variation"]["baseline_jitter"])

        char_width = LETTER_WIDTH
        char_height = LETTER_HEIGHT * height

        # Simulate: move to char start
        lines.append(f"G0 X{x:.2f} Y{y + jitter:.2f} ; move to start of {char}")
        lines.append("M3 ; pen down")
        lines.append(f"G1 X{x + char_width:.2f} Y{y + jitter + char_height:.2f} ; draw {char}")
        lines.append("M5 ; pen up")

        x += char_width + SPACING

    return "\n".join(lines)

if __name__ == "__main__":
    profile = load_profile(PROFILE_PATH)
    codes = read_codes(CODES_FILE)

    for code in codes:
        gcode = generate_gcode_for_code(code, profile)
        filename = os.path.join(OUTPUT_DIR, f"{code}.gcode")
        with open(filename, 'w') as f:
            f.write(gcode)
        print(f"✅ G-code saved to {filename}")
