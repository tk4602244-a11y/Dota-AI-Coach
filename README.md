# Dota AI Coach

A Windows desktop companion prototype for Dota 2. The long-term goal is to provide timely, explainable coaching recommendations while leaving every in-game action under the player's control.

## Current status

**Stage 0 — project scaffold.** This repository currently contains a local desktop prototype with example recommendations. It does not connect to Dota 2, inspect game memory, automate input, or provide live match advice yet.

## Principles

- **Player stays in control:** no automated movement, clicks, abilities, item use, or other gameplay actions.
- **Use documented interfaces only:** any future game-data integration must use documented, permitted interfaces and be reviewed against current Valve rules before release.
- **Be honest about uncertainty:** recommendations should explain their basis and avoid pretending to know information the app cannot access.
- **Protect privacy:** do not collect or upload match, account, or personal data without a clear user choice.
- **Keep secrets out of Git:** API keys, tokens, and credentials must never be committed.

## Run

Python 3.10 or newer is recommended.

```bash
python -m src.dota_ai_coach.main
```

The current prototype uses Python's built-in Tkinter library, so no third-party packages are required. On some Linux installations, Tkinter may need to be installed separately.

## Roadmap

1. Desktop shell and settings.
2. Read-only data-source investigation (documented interfaces only).
3. Situation model and confidence-aware recommendation rules.
4. Optional AI provider integration, with clear consent and cost controls.
5. Overlay only after compatibility and game-policy review.
6. Tests, packaging, accessibility, and privacy review.

## AI integration note

ChatGPT sign-in, ChatGPT subscription access, and OpenAI API access are different products with different eligibility and terms. Do not assume that a normal desktop app can use a ChatGPT account as a general-purpose API. Any provider integration must use an officially supported authorization flow and must not ask users to paste their ChatGPT password or session cookies into this app.

## License

No license has been selected yet. Until one is added, the repository is not granting general permission to reuse or redistribute its code.
