"""Living peony: your sharp flower image + breathing glow, rippling water,
drifting light particles and twinkling sparkles.
  pip install pygame-ce numpy pillow
  python peony_live.py        (keep flower.jpg in the same folder)
ESC quits, S saves a screenshot."""
import math, numpy as np, pygame
from PIL import Image, ImageFilter

IMG_H = 760                      # flower height on screen; lower it for a smaller window
MARGIN = 90                      # extra black space around the flower for particles
rng = np.random.default_rng(5)

# ---------- load + prepare the picture ----------
im = Image.open("flower.jpg").convert("RGB")
iw = int(im.width * IMG_H / im.height)
im = im.resize((iw, IMG_H), Image.LANCZOS)
CW, CH = iw + 2 * MARGIN, IMG_H + 2 * MARGIN
canvas = np.zeros((CH, CW, 3), np.float32)
canvas[MARGIN:MARGIN + IMG_H, MARGIN:MARGIN + iw] = np.asarray(im, np.float32)
# feather the picture's edges into the black margin so no box is visible
fx = np.clip(np.minimum(np.arange(CW) - MARGIN, CW - MARGIN - 1 - np.arange(CW)) / 45.0, 0, 1)
fy = np.clip(np.minimum(np.arange(CH) - MARGIN, CH - MARGIN - 1 - np.arange(CH)) / 45.0, 0, 1)
canvas *= (fy[:, None] * fx[None, :])[..., None]
lum = canvas.mean(2) / 255

# soft glow = blurred bright parts; pulsed on and off to make the flower "breathe"
bright = np.where(lum[..., None] > 0.55, canvas, 0).astype(np.uint8)
glow = np.asarray(Image.fromarray(bright).filter(ImageFilter.GaussianBlur(16)), np.float32)

# water ripples only affect the lower part of the picture (the reflection)
WATER_Y0 = MARGIN + int(IMG_H * 0.80)
water_rows = np.arange(WATER_Y0, CH - MARGIN)
water_depth = (water_rows - WATER_Y0) / max(1, len(water_rows) - 1)
cols = np.arange(CW)

# ---------- particles that float up off the bright petals ----------
N = 3500
ys, xs = np.nonzero(lum[:CH - MARGIN - int(IMG_H * 0.2)] > 0.6)   # not from the water
pick = rng.integers(0, len(ys), N)
SX, SY = xs[pick].astype(np.float32), ys[pick].astype(np.float32)
SCOL = canvas[ys[pick], xs[pick]]
SCOL = np.clip(SCOL * 1.3 + 40, 0, 255)
life = rng.random(N).astype(np.float32)
speed = rng.uniform(0.0015, 0.005, N).astype(np.float32)
rise = rng.uniform(30, 150, N).astype(np.float32)
sway = rng.uniform(0, 6.28, N).astype(np.float32)

# background twinkles
S = 90
TX, TY = rng.uniform(0, CW, S), rng.uniform(0, CH * 0.8, S)
TPH = rng.uniform(0, 6.28, S)

pygame.init()
screen = pygame.display.set_mode((CW, CH))
pygame.display.set_caption("Peony")
clock = pygame.time.Clock()
surf = pygame.Surface((CW, CH))
t = 0.0
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            pygame.image.save(screen, "peony_shot.png")
    t += 0.035

    frame = canvas.copy()

    # 1) rippling water: shift each row sideways by a moving sine wave
    shift = (3.2 * np.sin(water_rows * 0.13 + t * 2.2) * (0.3 + water_depth)).astype(int)
    idx = np.clip(cols[None, :] + shift[:, None], 0, CW - 1)
    frame[WATER_Y0:CH - MARGIN] = canvas[WATER_Y0:CH - MARGIN][np.arange(len(water_rows))[:, None], idx]

    # 2) breathing glow: bright parts bloom and fade
    frame += glow * (0.14 + 0.12 * math.sin(t * 1.1))

    # 3) light particles rising and fading
    life += speed
    dead = life >= 1
    life[dead] = 0
    ph = np.sin(life * math.pi)                                   # fade in then out
    px = SX + np.sin(t * 1.3 + sway) * 6 + life * 10
    py = SY - life * rise
    ok = (px > 1) & (px < CW - 2) & (py > 1) & (py < CH - 2)
    xi, yi = px[ok].astype(int), py[ok].astype(int)
    c = SCOL[ok] * (ph[ok] * 0.9)[:, None]
    for dx, dy, w in ((0, 0, 1.0), (1, 0, .4), (-1, 0, .4), (0, 1, .4), (0, -1, .4)):
        np.add.at(frame, (yi + dy, xi + dx), c * w)

    # 4) twinkling sparkles
    b = np.clip(120 + 130 * np.sin(t * 3 + TPH), 0, 255)
    sx, sy = TX.astype(int), TY.astype(int)
    for dx, dy, w in ((0, 0, 1), (1, 0, .5), (-1, 0, .5), (0, 1, .5), (0, -1, .5)):
        frame[sy + dy, sx + dx] += (b * w)[:, None]

    frame = np.clip(frame, 0, 255).astype(np.uint8)

    # 5) breathing zoom: crop a hair inward then scale back up
    m = int(2 + 5 * (0.5 + 0.5 * math.sin(t * 1.1)))              # 2..7 px
    pygame.surfarray.blit_array(surf, frame.transpose(1, 0, 2))
    crop = surf.subsurface((m, m, CW - 2 * m, CH - 2 * m)) if hasattr(surf, "subsurface") else surf
    screen.blit(pygame.transform.smoothscale(crop, (CW, CH)), (0, 0))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()