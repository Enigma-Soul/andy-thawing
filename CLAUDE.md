# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Andy Lau Thawing Countdown (刘德华解冻倒计时) — generates daily countdown images in light/dark themes with a "Wandering Earth 2" style UI. A GitHub Actions cron pushes fresh images to an `output` branch for embedding in READMEs.

## Commands

```bash
uv sync                                    # Install dependencies
uv run python -m andy_thawing              # Run locally (outputs light.png + dark.png)
uv run pyinstaller --onefile --name andy-thawing --add-data "resources:resources" --hidden-import=PIL src/andy_thawing/__main__.py  # Build exe
```

No tests or linter configured.

## Architecture

Single-entry pipeline: `__main__.py` → `counting.py` + `ice.py` → composites final images.

- **`config.py`** — Single source of truth for target date (`SPRING_FESTIVAL`), image dimensions, ice margins. All modules import from here.
- **`resources.py`** — Resolves paths to `resources/fonts/` and `resources/img/`. Handles PyInstaller's `sys._MEIPASS` for frozen builds; falls back to project-root-relative paths in dev. Use `font_path(name)` / `img_path(name)` instead of raw string concatenation.
- **`counting.py`** (`GetCountingPhoto`) — Calculates time remaining, auto-selects the largest unit (months/days/hours/minutes), delegates rendering to `EW2Count`, produces light+dark variants.
- **`ew2_count.py`** (`EW2Count`) — Low-level text layout renderer (Chinese title, red number, English subtitle, red divider line). Pure rendering logic, no filesystem access.
- **`ice.py`** (`GetIce`) — Calculates thaw percentage based on `SPRING_FESTIVAL`, composites ice overlay layers onto the Andy Lau photo.

## GitHub Actions

- **`build.yml`** — On push to `main`: builds PyInstaller `--onefile` executable, pushes to `build` branch.
- **`daily.yml`** — Daily cron: fetches executable from `build` branch, runs it, pushes output images to `output` branch. No Python runtime needed.

## Git 规范

- 默认 push 到 `develop` 分支，不直接 push 到 `main`
- commit 不加 `Co-Authored-By`、`Signed-off-by` 等附加行

## Key Conventions

- All resource paths go through `resources.py` — never hardcode font/image paths.
- Date and dimension constants live in `config.py` only.
- Package uses `src` layout (`src/andy_thawing/`); build backend is `hatchling`.
- UI text is bilingual (Chinese + English).
