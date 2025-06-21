import os
import json
import csv
import random

# === CONFIG ===
PROFILE_PATH = "profiles/stake_profile.json"
TEMPLATE_PATH = "input/notecard_template.txt"
DATA_PATH = "input/notecard_data.csv"
OUTPUT_DIR = "output_gcode/"
START_X = 10
START_Y = 10
LINE_SPACING = 15
LETTER_WIDTH = 10
LETTER_HEIGHT = 10
SPACING = 5

def load_profile(path):
    with open(path, 'r') as f:
        return json.load(f)

def read_template(path):
    with open(path, 'r') as f:
        return f.read()

def read_data(path):
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def generate_gcode(lines, profile):
    gcode = [
        "G21 ; mm",
        "G90 ; absolute positioning",
    ]
    x = START_X
    y = START_Y

    for line in lines:
        for char in line:
            tilt = random.uniform(*profile["variation"]["tilt"])
            height = random.uniform(*profile["variation"]["height"])
            jitter = random.uniform(*profile["variation"]["baseline_jitter"])
            char_height = LETTER_HEIGHT * height

            # Move to char start
            gcode.append(f"G0 X{x:.2f} Y{y + jitter:.2f}")
            gcode.append("G1 Z0 ; pen down")
            gcode.append(f"G1 X{x + LETTER_WIDTH:.2f} Y{y + jitter + char_height:.2f} ; draw")
            gcode.append("G1 Z5 ; pen up")

            x += LETTER_WIDTH + SPACING
        x = START_X
        y += LINE_SPACING

    return gcode

if __name__ == "__main__":
    profile = load_profile(PROFILE_PATH)
    template = read_template(TEMPLATE_PATH)
    data_rows = read_data(DATA_PATH)

    for row in data_rows:
        personalized_text = template
        for key, value in row.items():
            personalized_text = personalized_text.replace(f"{{{key}}}", value.strip())

        lines = personalized_text.strip().splitlines()
        gcode = generate_gcode(lines, profile)
        output_path = os.path.join(OUTPUT_DIR, f"{row['CODE'].strip()}.gcode")
        with open(output_path, 'w') as f:
            f.write("\n".join(gcode))
        print(f"✅ Notecard G-code saved: {output_path}")
