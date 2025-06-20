import os
import json
import random
from PIL import Image, ImageDraw, ImageFont

# === CONFIG ===
PROFILE_PATH = "profiles/stake_profile.json"
CODES_FILE = "input/codes.txt"
FONT_SIZE = 80  # You can adjust this if too small or large

# === FUNCTIONS ===

def load_profile(profile_path):
    with open(profile_path, 'r') as f:
        return json.load(f)

def read_codes(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def apply_variation(x, y, variation):
    tilt = random.uniform(*variation["tilt"])
    height = random.uniform(*variation["height"])
    baseline_jitter = random.uniform(*variation["baseline_jitter"])
    return x, y + baseline_jitter, tilt, height

def render_code(code, font, variation, draw, start_y, img):
    x = 50  # left margin
    y = start_y
    for char in code:
        char_x, char_y, tilt, height = apply_variation(x, y, variation)

        # Create a separate image for this character
        char_img = Image.new("L", (100, 100), 0)
        char_draw = ImageDraw.Draw(char_img)
        char_draw.text((10, 10), char, font=font, fill=255)

        # Scale + rotate
        char_img = char_img.resize((int(100), int(100 * height)))
        char_img = char_img.rotate(tilt, expand=True, fillcolor=0)

        # Paste onto main image
        img.paste(char_img, (int(char_x), int(char_y)), char_img)

        x += 60  # Move x over for next character

# === MAIN ===

if __name__ == "__main__":
    profile = load_profile(PROFILE_PATH)
    codes = read_codes(CODES_FILE)

    font_path = os.path.join("profiles", profile["handwriting_style_file"])
    font = ImageFont.truetype(font_path, FONT_SIZE)

    variation = profile["variation"]

    # Estimate canvas size
    canvas_width = 1000
    canvas_height = 150 * len(codes)
    img = Image.new("L", (canvas_width, canvas_height), color=255)
    draw = ImageDraw.Draw(img)

    # Draw each code line
    for idx, code in enumerate(codes):
        y_offset = idx * 120
        render_code(code, font, variation, draw, y_offset, img)

    # Save result
    preview_path = "output_gcode/preview.png"
    img.save(preview_path)
    print(f"✅ Preview saved to {preview_path}")
