# The Hormonal Yogini

Gentle yoga, hormone-friendly recipes and simple hormone guides for women and mums, by Yogeeta Sharma.

**Live site:** https://sharmayogeeta.github.io/hormonal-yogini/
**Link-in-bio page:** https://sharmayogeeta.github.io/hormonal-yogini/links.html

- YouTube: https://www.youtube.com/@thehormonalyogini
- Instagram: https://www.instagram.com/thehormonalyogini/
- Portfolio: https://sharmayogeeta.github.io/portfolio/

## Pages

| Page | What's on it |
|---|---|
| `index.html` | Home: intro, start-here cards, popular Shorts |
| `yoga.html` | All YouTube classes and Shorts, filterable by focus |
| `recipes.html` | Hormone-friendly recipes, filterable by goal |
| `learn.html` | Guides: cycle phases, period cramps, cortisol, postpartum, daily habits |
| `links.html` | Link-in-bio page for Instagram and TikTok |

## Updating content

You don't need to touch the HTML for everyday updates. Edit `assets/js/data.js` on GitHub and commit:

- **New YouTube video or Short:** copy a line in `HY.VIDEOS` and change the `id` (the part after `v=` or `/shorts/` in the link), `title` and `cat`.
- **New recipe:** copy a block in `HY.RECIPES`.
- **TikTok:** when the account is live, add it to `HY.LINKS` and to the link lists in `tools/build.py`.

Page text and layout live in `tools/build.py`; styles in `assets/css/style.css`.

## How it's published

Every push to `main` runs `.github/workflows/pages.yml`, which builds the pages with `tools/build.py` and deploys them to GitHub Pages. It takes about a minute.

The content is general wellbeing information, not medical advice.
