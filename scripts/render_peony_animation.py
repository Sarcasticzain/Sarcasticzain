#!/usr/bin/env python3
"""Render the peony as a transparent, blue-sparkle APNG for the profile README.

The motion mirrors the supplied Pygame animation: a gentle breathing pulse,
rising petal-light particles, and small twinkling blue sparkles. Alpha is kept
through every frame so the README page remains visible behind the flower.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "flower-transparent.png"
OUTPUT = ROOT / "assets" / "flower-animation.png"
FRAME_COUNT = 18
FRAME_DURATION_MS = 110
CANVAS_SIZE = (340, 360)
SUBJECT_WIDTH = 280
PARTICLE_COUNT = 100
SPARKLE_COUNT = 18


def adjust_rgb(image: Image.Image, factor: float) -> Image.Image:
    array = np.asarray(image, dtype=np.uint8).copy()
    array[..., :3] = np.clip(array[..., :3].astype(np.float32) * factor, 0, 255).astype(np.uint8)
    return Image.fromarray(array, "RGBA")


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(f"Transparent flower asset not found: {SOURCE}")

    rng = np.random.default_rng(5)
    flower = Image.open(SOURCE).convert("RGBA")
    bbox = flower.getchannel("A").getbbox()
    if not bbox:
        raise ValueError("Transparent flower image has no visible pixels.")
    flower = flower.crop(bbox)

    target_height = round(flower.height * SUBJECT_WIDTH / flower.width)
    flower = flower.resize((SUBJECT_WIDTH, target_height), Image.Resampling.LANCZOS)
    if flower.width > CANVAS_SIZE[0] - 24 or flower.height > CANVAS_SIZE[1] - 24:
        raise ValueError("Flower does not fit in the animation canvas; increase CANVAS_SIZE.")

    # Bright points on petals become a small number of rising cyan particles.
    flower_array = np.asarray(flower, dtype=np.uint8)
    luminance = flower_array[..., :3].mean(axis=2)
    candidates = np.argwhere((flower_array[..., 3] > 150) & (luminance > 155))
    if len(candidates) == 0:
        raise ValueError("No bright petal pixels found for the sparkle animation.")
    chosen = candidates[rng.integers(0, len(candidates), PARTICLE_COUNT)]
    particle_y = chosen[:, 0].astype(np.float32)
    particle_x = chosen[:, 1].astype(np.float32)
    particle_life = rng.random(PARTICLE_COUNT).astype(np.float32)
    particle_cycles = rng.integers(1, 4, PARTICLE_COUNT).astype(np.float32)
    particle_phase = rng.uniform(0, 2 * math.pi, PARTICLE_COUNT).astype(np.float32)
    particle_rise = rng.uniform(12, 38, PARTICLE_COUNT).astype(np.float32)

    # Place twinkles in the transparent breathing room around the flower.
    width, height = CANVAS_SIZE
    margin_x = (width - flower.width) // 2
    margin_y = (height - flower.height) // 2
    sparkle_positions = []
    for _ in range(SPARKLE_COUNT):
        side = int(rng.integers(0, 4))
        if side == 0:
            x, y = rng.uniform(2, width - 2), rng.uniform(2, max(4, margin_y - 2))
        elif side == 1:
            x, y = rng.uniform(2, width - 2), rng.uniform(height - margin_y + 2, height - 2)
        elif side == 2:
            x, y = rng.uniform(2, max(4, margin_x - 2)), rng.uniform(4, height - 4)
        else:
            x, y = rng.uniform(width - margin_x + 2, width - 2), rng.uniform(4, height - 4)
        sparkle_positions.append((x, y, rng.uniform(0, 2 * math.pi), rng.uniform(0.8, 2.1)))

    frames: list[Image.Image] = []
    for frame_index in range(FRAME_COUNT):
        phase = 2 * math.pi * frame_index / FRAME_COUNT
        scale = 1.0 + 0.012 * math.sin(phase)
        brightness = 1.0 + 0.035 * math.sin(phase - math.pi / 2)
        float_y = round(2 * math.sin(phase))
        size = (round(flower.width * scale), round(flower.height * scale))
        subject = adjust_rgb(flower, brightness).resize(size, Image.Resampling.LANCZOS)

        frame = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
        x0 = (width - size[0]) // 2
        y0 = (height - size[1]) // 2 + float_y

        # A restrained cyan rim-light breathes behind the petals; alpha stays soft.
        glow_alpha = subject.getchannel("A").filter(ImageFilter.GaussianBlur(8))
        glow_alpha = glow_alpha.point(lambda value: round(value * 0.045))
        glow = Image.new("RGBA", size, (66, 190, 255, 0))
        glow.putalpha(glow_alpha)
        frame.alpha_composite(glow, (x0, y0))
        frame.alpha_composite(subject, (x0, y0))

        overlay = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        # Small blue particles rise from bright petals and fade at their peaks.
        life = (particle_life + particle_cycles * frame_index / FRAME_COUNT) % 1.0
        fade = np.sin(life * math.pi)
        px = x0 + particle_x + np.sin(phase * 1.3 + particle_phase) * 3
        py = y0 + particle_y - life * particle_rise
        for x, y, alpha in zip(px, py, fade):
            if 0 <= x < width and 0 <= y < height:
                radius = 1 if alpha < 0.72 else 2
                strength = int(150 * float(alpha))
                draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(90, 210, 255, strength))

        # Blue background twinkles, inspired by the supplied script.
        for sx, sy, offset, radius in sparkle_positions:
            strength = int(185 * (0.5 + 0.5 * math.sin(phase * 3 + offset)))
            r = max(1, round(radius))
            draw.ellipse((sx - r, sy - r, sx + r, sy + r), fill=(105, 220, 255, strength))
            if strength > 120:
                draw.line((sx - r * 2, sy, sx + r * 2, sy), fill=(105, 220, 255, strength // 2), width=1)
                draw.line((sx, sy - r * 2, sx, sy + r * 2), fill=(105, 220, 255, strength // 2), width=1)

        # A tiny blur gives only the particle points a soft, blue glow.
        particle_glow = overlay.filter(ImageFilter.GaussianBlur(2))
        particle_glow.putalpha(particle_glow.getchannel("A").point(lambda value: round(value * 0.38)))
        frame.alpha_composite(particle_glow)
        frame.alpha_composite(overlay)
        frames.append(frame)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        OUTPUT,
        format="PNG",
        save_all=True,
        append_images=frames[1:],
        duration=FRAME_DURATION_MS,
        loop=0,
        disposal=2,
        blend=0,
        optimize=True,
    )
    print(f"Rendered {FRAME_COUNT} transparent APNG frames with blue sparkles to {OUTPUT}")


if __name__ == "__main__":
    main()
