# Upload this profile README bundle

1. Extract the ZIP. **Do not upload the ZIP itself**; GitHub does not unpack it automatically.
2. Upload/replace its contents in the root of `Sarcasticzain/Sarcasticzain`, preserving folders. Important files include `README.md`, `.github/workflows/profile-views.yml`, `assets/flower-transparent.png`, `assets/flower-animation.png`, `scripts/render_peony_animation.py`, `scripts/peony_live.py`, `flower.jpg`, and `requirements.txt`.
3. Commit everything to the `main` branch.
4. Open **Actions → Profile Flower Animation → Run workflow** once if the animated flower does not show immediately.

The README uses an animated PNG (APNG) with true transparency, blue glow, rising petal particles, and twinkling sparkles—there is no black background box. Its profile-visits badge uses Komarev's GitHub profile-hit counter, and the followers badge reads the live GitHub follower count through Shields.io. Profile visits count page hits, not unique people. Counter documentation: https://github.com/antonkomarev/github-profile-views-counter

The supplied interactive Python source is included. From the repository root, install dependencies with `python -m pip install -r requirements.txt`, then run `python scripts/peony_live.py`.
