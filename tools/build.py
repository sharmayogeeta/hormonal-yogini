"""Generates the static HTML pages for The Hormonal Yogini site."""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])
BASE = 'https://sharmayogeeta.github.io/hormonal-yogini/'
YT = 'https://www.youtube.com/@thehormonalyogini'
YT_SUB = YT + '?sub_confirmation=1'
IG = 'https://www.instagram.com/thehormonalyogini/'
PORTFOLIO = 'https://sharmayogeeta.github.io/portfolio/'

LOTUS = '''<svg viewBox="0 0 64 64" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.6"><path d="M32 14c6 6 8 13 8 20s-3 13-8 16c-5-3-8-9-8-16s2-14 8-20z" stroke="#5c3352" fill="#f8e6e1"/><path d="M24 30c-6-2-12-1-16 2 2 9 9 16 24 18" stroke="#c7776a"/><path d="M40 30c6-2 12-1 16 2-2 9-9 16-24 18" stroke="#c7776a"/><path d="M14 52h36" stroke="#6f8f72"/></g></svg>'''

NAV = [('index.html', 'Home'), ('yoga.html', 'Yoga videos'), ('recipes.html', 'Recipes'), ('learn.html', 'Hormone guides'), ('links.html', 'Links')]

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Nunito+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="assets/css/style.css">'''


def head(page, title, desc, image='assets/img/hero.webp', extra=''):
    url = BASE + ('' if page == 'index.html' else page)
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{url}">
    <meta name="theme-color" content="#5c3352">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="The Hormonal Yogini">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{BASE}{image}">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
    {FONTS}{extra}
</head>'''


def nav(active):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ''
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    items.append(f'<li><a class="nav-cta" href="{YT_SUB}" target="_blank" rel="noopener"><i class="fab fa-youtube" aria-hidden="true"></i> Subscribe</a></li>')
    return f'''<body>
    <a class="sr-only" href="#main">Skip to content</a>
    <nav class="site-nav" aria-label="Main">
        <div class="container nav-inner">
            <a class="brand" href="index.html">{LOTUS} The Hormonal Yogini</a>
            <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-menu"><span></span><span></span><span></span></button>
            <ul class="nav-menu" id="nav-menu">
                {chr(10).join('                ' + i for i in items).strip()}
            </ul>
        </div>
    </nav>
'''


FOLLOW = f'''
        <section class="section">
            <div class="container">
                <div class="follow-band reveal">
                    <div>
                        <p class="eyebrow" style="color:#f3c9bf">Join the community</p>
                        <h2>Practise with me every week</h2>
                        <p>New gentle yoga classes, 60-second Shorts and Reels, and honest hormone talk for real women and busy mums. No crash diets, no pressure, no guilt.</p>
                    </div>
                    <div class="social-list">
                        <a class="social" href="{YT_SUB}" target="_blank" rel="noopener"><i class="fab fa-youtube" aria-hidden="true"></i><div><strong>YouTube</strong><span>@thehormonalyogini · full classes &amp; Shorts</span></div></a>
                        <a class="social" href="{IG}" target="_blank" rel="noopener"><i class="fab fa-instagram" aria-hidden="true"></i><div><strong>Instagram</strong><span>@thehormonalyogini · daily Reels</span></div></a>
                    </div>
                </div>
            </div>
        </section>'''

DISCLAIMER = '''<p class="disclaimer"><i class="fas fa-circle-info" aria-hidden="true"></i> The content on this site is for general wellbeing and education only and is not medical advice. Please speak to your GP or midwife before starting a new exercise or diet routine, especially if you are pregnant, postpartum, or have a health condition.</p>'''


def footer():
    return f'''
    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <h3>The Hormonal Yogini</h3>
                    <p>Gentle yoga, nourishing food and simple hormone education for women and mums, by Yogeeta Sharma in Brighton, UK.</p>
                    <div class="footer-social">
                        <a href="{YT}" target="_blank" rel="noopener" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
                        <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="{PORTFOLIO}" target="_blank" rel="noopener" aria-label="Yogeeta Sharma's portfolio"><i class="fas fa-feather-pointed"></i></a>
                    </div>
                </div>
                <div>
                    <h3>Explore</h3>
                    <ul>
                        <li><a href="yoga.html">Yoga videos</a></li>
                        <li><a href="recipes.html">Hormone-friendly recipes</a></li>
                        <li><a href="learn.html">Hormone guides</a></li>
                        <li><a href="links.html">All links</a></li>
                    </ul>
                </div>
                <div>
                    <h3>About Yogeeta</h3>
                    <ul>
                        <li><a href="{PORTFOLIO}" target="_blank" rel="noopener">Writing portfolio</a></li>
                        <li><a href="https://sharmayogeeta.github.io/cv/" target="_blank" rel="noopener">Online CV</a></li>
                        <li><a href="{PORTFOLIO}books.html" target="_blank" rel="noopener">Books</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; <span data-year>2026</span> Yogeeta Sharma · The Hormonal Yogini</p>
                <p>Wellbeing content, not medical advice.</p>
            </div>
        </div>
    </footer>
'''


def scripts():
    return '''
    <script src="assets/js/data.js"></script>
    <script src="assets/js/main.js"></script>
</body>
</html>
'''


def page(fname, title, desc, body, extra_head=''):
    html = head(fname, title, desc, extra=extra_head) + '\n' + nav(fname) + '\n    <main id="main">' + body + '\n    </main>\n' + footer() + scripts()
    (OUT / fname).write_text(html, encoding='utf-8')


# ---------------------------------------------------------------- HOME
ORG_LD = f'''
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebSite","name":"The Hormonal Yogini","url":"{BASE}","author":{{"@type":"Person","name":"Yogeeta Sharma","url":"{PORTFOLIO}","sameAs":["{YT}","{IG}","{PORTFOLIO}"]}}}}</script>'''

home = f'''
        <section class="hero">
            <div class="container hero-grid">
                <div>
                    <p class="eyebrow">Yoga · Food · Hormone health</p>
                    <h1>Feel at home in your body <em>again</em>.</h1>
                    <p class="lead">I'm Yogeeta, The Hormonal Yogini. Gentle yoga, simple hormone-friendly food and honest education for women and mums who are tired of crash diets and exhausting workouts.</p>
                    <div class="hero-cta">
                        <a href="yoga.html" class="btn btn-primary"><i class="fas fa-play" aria-hidden="true"></i> Start practising</a>
                        <a href="recipes.html" class="btn btn-ghost">Browse recipes</a>
                    </div>
                    <div class="trust">
                        <span><i class="fas fa-check" aria-hidden="true"></i> Free classes on YouTube</span>
                        <span><i class="fas fa-check" aria-hidden="true"></i> Beginner &amp; mum friendly</span>
                        <span><i class="fas fa-check" aria-hidden="true"></i> 5 to 20 minutes a day</span>
                    </div>
                </div>
                <div class="hero-photo">
                    <img src="assets/img/hero.webp" alt="Yogeeta in a supported garland squat with hands in prayer" width="520" height="496">
                    <a class="hero-badge" href="{YT_SUB}" target="_blank" rel="noopener">
                        <i class="fab fa-youtube" aria-hidden="true"></i>
                        <div><strong>4,000+</strong><span>women practising on YouTube</span></div>
                    </a>
                </div>
            </div>
        </section>

        <section class="section white">
            <div class="container">
                <div class="section-head">
                    <p class="eyebrow">Start here</p>
                    <h2>Three gentle ways to rebalance</h2>
                    <span class="leaf"></span>
                </div>
                <div class="grid-3">
                    <a class="card reveal" href="yoga.html">
                        <div class="card-icon"><i class="fas fa-play" aria-hidden="true"></i></div>
                        <div class="body">
                            <h3>Yoga videos</h3>
                            <p>Full classes and one-minute Shorts for hormone balance, period cramps, stress and back pain.</p>
                            <span class="card-link">Watch now <i class="fas fa-arrow-right" aria-hidden="true"></i></span>
                        </div>
                    </a>
                    <a class="card reveal" href="recipes.html">
                        <div class="card-icon sage"><i class="fas fa-bowl-food" aria-hidden="true"></i></div>
                        <div class="body">
                            <h3>Hormone-friendly recipes</h3>
                            <p>Seed-cycling bites, iron-rich dal, period tea and calming moon milk. Simple, Indian-inspired and family friendly.</p>
                            <span class="card-link">Get cooking <i class="fas fa-arrow-right" aria-hidden="true"></i></span>
                        </div>
                    </a>
                    <a class="card reveal" href="learn.html">
                        <div class="card-icon plum"><i class="fas fa-moon" aria-hidden="true"></i></div>
                        <div class="body">
                            <h3>Hormone guides</h3>
                            <p>Your cycle in four phases, easing cramps, calming cortisol and rebuilding gently after birth.</p>
                            <span class="card-link">Learn more <i class="fas fa-arrow-right" aria-hidden="true"></i></span>
                        </div>
                    </a>
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container split">
                <div class="split-media reveal"><img src="assets/img/toddler.webp" alt="Yogeeta in cat pose while her toddler plays beside the mat" loading="lazy" width="600" height="329"></div>
                <div class="reveal">
                    <p class="eyebrow">Real life, real practice</p>
                    <h2>Yoga that fits around mum life</h2>
                    <p style="margin-top:14px">My mat is in the living room, and my toddler usually joins in. Every class is designed for real homes and real energy levels.</p>
                    <ul>
                        <li><i class="fas fa-leaf" aria-hidden="true"></i> Understand your hormones in a simple way</li>
                        <li><i class="fas fa-leaf" aria-hidden="true"></i> Rebuild strength gently after pregnancy</li>
                        <li><i class="fas fa-leaf" aria-hidden="true"></i> Ease fatigue, bloating, cramps and stress</li>
                        <li><i class="fas fa-leaf" aria-hidden="true"></i> Build routines you can actually keep</li>
                    </ul>
                    <a class="btn btn-primary" href="yoga.html">See all classes <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
                </div>
            </div>
        </section>

        <section class="section white">
            <div class="container">
                <div class="section-head">
                    <p class="eyebrow">One minute at a time</p>
                    <h2>Popular Shorts</h2>
                    <span class="leaf"></span>
                </div>
                <div class="shorts-grid" id="featured-shorts" data-ids="bHVmZ7n9TSI,DMq4INEO4S8,8H5cFCLwDrE,oipHKnup7a8"></div>
                <p style="text-align:center;margin-top:36px"><a class="btn btn-ghost" href="yoga.html">More videos <i class="fas fa-arrow-right" aria-hidden="true"></i></a></p>
            </div>
        </section>
{FOLLOW}
        {DISCLAIMER}
        <div style="height:60px"></div>'''

page('index.html', 'The Hormonal Yogini | Yoga for Hormone Balance, Periods & Mums',
     'Gentle yoga for hormone balance, period cramps and postpartum recovery, plus hormone-friendly recipes and simple guides for women and mums. By Yogeeta Sharma.',
     home, ORG_LD)

# ---------------------------------------------------------------- YOGA
yoga = f'''
        <section class="page-hero">
            <div class="container">
                <p class="eyebrow">Free yoga classes</p>
                <h1>Yoga videos</h1>
                <p>Gentle classes and quick Shorts for hormone balance, period pain, stress and back care. Press play on any video, or pick a focus below.</p>
            </div>
        </section>

        <section class="section" style="padding-top:40px">
            <div class="container">
                <div class="video-tabs" id="video-filters" role="group" aria-label="Filter videos by focus"></div>
                <h2 style="margin-bottom:24px">Full classes</h2>
                <div class="long-grid" id="long-videos" data-append="soon-tpl"></div>
                <template id="soon-tpl">
                    <article class="video long coming-soon" data-cat="hormones">
                        <div class="video-frame"><div><strong>Yoga for Period Cramps</strong>Full 20-minute class · coming soon to YouTube</div></div>
                        <div class="video-body"><h3>Yoga for Period Cramps: 20-Minute Gentle Flow</h3><p>18 soothing poses to ease cramps, lower back ache and bloating. Subscribe so you don't miss it.</p>
                        <div class="video-meta"><a href="{YT_SUB}" target="_blank" rel="noopener">Subscribe on YouTube <i class="fas fa-arrow-up-right-from-square" aria-hidden="true"></i></a></div></div>
                    </article>
                </template>

                <h2 style="margin:64px 0 24px">Shorts</h2>
                <div class="shorts-grid" id="short-videos"></div>
                <p style="text-align:center;margin-top:40px"><a class="btn btn-yt" href="{YT_SUB}" target="_blank" rel="noopener"><i class="fab fa-youtube" aria-hidden="true"></i> Subscribe for new classes</a></p>
            </div>
        </section>
{FOLLOW}
        {DISCLAIMER}
        <div style="height:60px"></div>'''

page('yoga.html', 'Free Yoga Videos for Hormone Balance & Period Cramps | The Hormonal Yogini',
     'Watch free gentle yoga classes and Shorts for hormone balance, period cramps, stress, the nervous system and back pain. Beginner and mum friendly.',
     yoga)

# ---------------------------------------------------------------- RECIPES
recipes = f'''
        <section class="page-hero">
            <div class="container">
                <p class="eyebrow">Nourish, don't restrict</p>
                <h1>Hormone-friendly recipes</h1>
                <p>Simple, satisfying food built on protein, fibre, healthy fats and colour. Many are Indian-inspired family favourites. Tap a recipe to see the method.</p>
            </div>
        </section>

        <section class="section" style="padding-top:40px">
            <div class="container">
                <div class="filters" id="recipe-filters" role="group" aria-label="Filter recipes by goal"></div>
                <div class="recipe-grid" id="recipe-grid"></div>
            </div>
        </section>
{FOLLOW}
        {DISCLAIMER}
        <div style="height:60px"></div>'''

page('recipes.html', 'Hormone-Friendly Recipes for Periods, PMS & Postpartum | The Hormonal Yogini',
     'Easy hormone-friendly recipes: seed-cycling energy balls, iron-rich spinach dal, ginger period tea, golden moon milk and more. Simple food for women and mums.',
     recipes)

# ---------------------------------------------------------------- LEARN
learn = f'''
        <section class="page-hero">
            <div class="container">
                <p class="eyebrow">Hormones, made simple</p>
                <h1>Hormone guides</h1>
                <p>Short, plain-English guides to how your hormones work and the small daily habits that help.</p>
            </div>
        </section>

        <section class="section" style="padding-top:40px">
            <div class="container" style="max-width:920px">
                <nav class="toc" aria-label="Guides">
                    <a class="chip" href="#cycle">Your cycle</a>
                    <a class="chip" href="#cramps">Period cramps</a>
                    <a class="chip" href="#stress">Stress &amp; cortisol</a>
                    <a class="chip" href="#postpartum">After birth</a>
                    <a class="chip" href="#habits">Daily habits</a>
                </nav>

                <article class="guide reveal" id="cycle">
                    <div class="guide-head"><div class="card-icon"><i class="fas fa-moon" aria-hidden="true"></i></div><h2>Your cycle in four phases</h2></div>
                    <p>Your energy, mood and appetite naturally change across the month as oestrogen and progesterone rise and fall. Working with these shifts, rather than against them, can make movement and food feel easier.</p>
                    <div class="phase-grid">
                        <div class="phase"><small>Days 1–5 (approx.)</small><h4>Menstrual</h4><p>Energy is lowest. Choose rest, restorative yoga, walks, warm meals and iron-rich food.</p></div>
                        <div class="phase"><small>Days 6–13</small><h4>Follicular</h4><p>Oestrogen rises and energy returns. A good time for stronger flows and trying new things.</p></div>
                        <div class="phase"><small>Days 14–16</small><h4>Ovulation</h4><p>Often your most energetic, social days. Enjoy dynamic practice and plenty of fibre and veg.</p></div>
                        <div class="phase"><small>Days 17–28</small><h4>Luteal</h4><p>Progesterone rises; cravings and PMS may appear. Slow down, add magnesium-rich foods and prioritise sleep.</p></div>
                    </div>
                    <p style="margin-top:16px">Every cycle is different, so treat these days as a rough guide and notice your own patterns. A simple cycle-tracking app helps.</p>
                </article>

                <article class="guide reveal" id="cramps">
                    <div class="guide-head"><div class="card-icon sage"><i class="fas fa-hand-holding-heart" aria-hidden="true"></i></div><h2>Easing period cramps naturally</h2></div>
                    <p>Cramps happen when the uterus contracts to shed its lining. Gentle movement, warmth and breathing can help tight muscles release.</p>
                    <ul>
                        <li><strong>Four poses to try:</strong> supported garland squat, butterfly, reclined butterfly and legs up the wall. Hold each for 1–3 minutes with slow belly breathing.</li>
                        <li><strong>Warmth:</strong> a hot water bottle on the lower belly or back, and warm drinks like <a href="recipes.html" style="color:var(--plum);font-weight:700">ginger and fennel tea</a>.</li>
                        <li><strong>Food:</strong> iron-rich meals (dal, leafy greens) to replace what you lose, and magnesium from seeds, nuts and dark chocolate.</li>
                        <li><strong>See your GP</strong> if pain stops you from doing daily activities, is getting worse, or comes with very heavy bleeding. Conditions like endometriosis deserve proper care.</li>
                    </ul>
                </article>

                <article class="guide reveal" id="stress">
                    <div class="guide-head"><div class="card-icon plum"><i class="fas fa-spa" aria-hidden="true"></i></div><h2>Stress, cortisol and your nervous system</h2></div>
                    <p>Cortisol is your main stress hormone. It is helpful in short bursts, but when stress never switches off it can affect sleep, cravings, belly fat, energy and even your cycle.</p>
                    <ul>
                        <li><strong>Breathe low and slow:</strong> one minute of belly breathing with a longer out-breath tells your body it is safe.</li>
                        <li><strong>Calming poses:</strong> reclined bound angle, cat-cow, child's pose, legs up the wall.</li>
                        <li><strong>Morning light:</strong> 10 minutes outside soon after waking supports a healthy cortisol rhythm.</li>
                        <li><strong>Eat a proper breakfast</strong> with protein, and go easy on caffeine on an empty stomach.</li>
                    </ul>
                </article>

                <article class="guide reveal" id="postpartum">
                    <div class="guide-head"><div class="card-icon"><i class="fas fa-baby" aria-hidden="true"></i></div><h2>After birth: rebuilding gently</h2></div>
                    <p>Hormones shift dramatically after pregnancy, and broken sleep makes everything harder. Your body has done something huge, so recovery is not a race.</p>
                    <ul>
                        <li>Wait for your 6–8 week postnatal check before returning to exercise, and longer after a caesarean.</li>
                        <li>Start with breathing, pelvic floor work and gentle mobility before building strength.</li>
                        <li>Watch for doming in your tummy during exercise; a women's health physio can check for diastasis recti.</li>
                        <li>Warm, easy meals like <a href="recipes.html" style="color:var(--plum);font-weight:700">khichdi and ragi porridge</a> are traditional for a reason.</li>
                        <li>Low mood that lasts more than two weeks is common and treatable. Please talk to your GP or health visitor.</li>
                    </ul>
                </article>

                <article class="guide reveal" id="habits">
                    <div class="guide-head"><div class="card-icon sage"><i class="fas fa-seedling" aria-hidden="true"></i></div><h2>Five daily habits for happier hormones</h2></div>
                    <ul>
                        <li><strong>Move a little every day:</strong> 10 minutes of yoga beats one exhausting session a week.</li>
                        <li><strong>Build balanced plates:</strong> protein, fibre and healthy fat at each meal help steady blood sugar.</li>
                        <li><strong>Protect your sleep:</strong> a regular wind-down routine and screens off before bed.</li>
                        <li><strong>Get outside:</strong> daylight and fresh air support mood and your body clock.</li>
                        <li><strong>Be kind to yourself:</strong> chronic self-criticism is stress too. Progress, not perfection.</li>
                    </ul>
                </article>
            </div>
        </section>
{FOLLOW}
        {DISCLAIMER}
        <div style="height:60px"></div>'''

page('learn.html', 'Hormone Health Guides: Cycle, Cramps, Cortisol & Postpartum | The Hormonal Yogini',
     'Simple guides to the four phases of your menstrual cycle, easing period cramps naturally, lowering stress and cortisol, and gentle postpartum recovery.',
     learn)

# ---------------------------------------------------------------- LINKS (link-in-bio)
links = head('links.html', 'Links | The Hormonal Yogini', 'All links for The Hormonal Yogini: YouTube, Instagram, free yoga classes, recipes and hormone guides.') + f'''
<body>
    <main class="links-page" id="main">
        <div class="links-card">
            <img class="avatar" src="assets/img/avatar.webp" alt="Yogeeta Sharma" width="160" height="160">
            <h1>The Hormonal Yogini</h1>
            <p>Gentle yoga &amp; hormone health for women and mums · by Yogeeta Sharma</p>
            <a class="link-btn featured" href="{YT_SUB}" target="_blank" rel="noopener"><i class="fab fa-youtube" aria-hidden="true"></i><div>Subscribe on YouTube<small>Full classes &amp; Shorts</small></div><span class="arrow"><i class="fas fa-arrow-up-right-from-square"></i></span></a>
            <a class="link-btn" href="{IG}" target="_blank" rel="noopener"><i class="fab fa-instagram" aria-hidden="true"></i><div>Instagram<small>@thehormonalyogini</small></div><span class="arrow"><i class="fas fa-arrow-up-right-from-square"></i></span></a>
            <a class="link-btn" href="yoga.html"><i class="fas fa-play" aria-hidden="true"></i><div>Free yoga classes<small>Hormones, cramps, stress, back pain</small></div><span class="arrow"><i class="fas fa-arrow-right"></i></span></a>
            <a class="link-btn" href="recipes.html"><i class="fas fa-bowl-food" aria-hidden="true"></i><div>Hormone-friendly recipes<small>Seed-cycling bites, period tea &amp; more</small></div><span class="arrow"><i class="fas fa-arrow-right"></i></span></a>
            <a class="link-btn" href="learn.html"><i class="fas fa-book-open" aria-hidden="true"></i><div>Hormone guides<small>Your cycle, cramps, cortisol, postpartum</small></div><span class="arrow"><i class="fas fa-arrow-right"></i></span></a>
            <a class="link-btn" href="{PORTFOLIO}books.html" target="_blank" rel="noopener"><i class="fas fa-book" aria-hidden="true"></i><div>My books<small>The Battlefield Within · Arjun &amp; The Magic Chariot</small></div><span class="arrow"><i class="fas fa-arrow-up-right-from-square"></i></span></a>
            <a class="link-btn" href="{PORTFOLIO}" target="_blank" rel="noopener"><i class="fas fa-feather-pointed" aria-hidden="true"></i><div>Writing portfolio<small>Articles, research &amp; CV</small></div><span class="arrow"><i class="fas fa-arrow-up-right-from-square"></i></span></a>
            <p style="margin-top:24px;font-size:.85rem"><a href="index.html" style="color:var(--plum);font-weight:800">Visit the website</a></p>
        </div>
    </main>
</body>
</html>
'''
(OUT / 'links.html').write_text(links, encoding='utf-8')

# ---------------------------------------------------------------- 404
nf = head('404.html', 'Page not found | The Hormonal Yogini', 'This page could not be found.') + '''
<body>
    <main class="links-page" id="main">
        <div class="links-card">
            <h1>Take a deep breath…</h1>
            <p>This page doesn't exist, but your next practice does.</p>
            <a class="link-btn featured" href="/hormonal-yogini/"><i class="fas fa-house" aria-hidden="true"></i><div>Back to the homepage</div><span class="arrow"><i class="fas fa-arrow-right"></i></span></a>
        </div>
    </main>
</body>
</html>
'''
(OUT / '404.html').write_text(nf, encoding='utf-8')

(OUT / 'assets/img/favicon.svg').write_text(LOTUS.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'), encoding='utf-8')
(OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
urls = ''.join(f'  <url><loc>{BASE}{p}</loc></url>\n' for p in ['', 'yoga.html', 'recipes.html', 'learn.html', 'links.html'])
(OUT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
(OUT / '.nojekyll').write_text('')
print('built')
