(function () {
    'use strict';
    var HY = window.HY || {};

    function esc(s) {
        return String(s).replace(/[&<>"']/g, function (c) {
            return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
        });
    }

    /* ---------- Navigation ---------- */
    var nav = document.querySelector('.site-nav');
    var toggle = document.querySelector('.nav-toggle');
    var menu = document.getElementById('nav-menu');
    if (toggle && menu) {
        toggle.addEventListener('click', function () {
            var open = menu.classList.toggle('open');
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
            toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
        });
        menu.addEventListener('click', function (e) {
            if (e.target.closest('a')) { menu.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); }
        });
    }
    if (nav) {
        var onScroll = function () { nav.classList.toggle('scrolled', window.scrollY > 8); };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

    /* ---------- Videos ---------- */
    function catLabel(c) { return (HY.VIDEO_CATS && HY.VIDEO_CATS[c]) || ''; }

    function videoCard(v) {
        var isShort = v.type === 'short';
        var watchUrl = isShort ? 'https://www.youtube.com/shorts/' + v.id : 'https://www.youtube.com/watch?v=' + v.id;
        return '<article class="video ' + (isShort ? 'short' : 'long') + ' reveal" data-cat="' + esc(v.cat) + '">' +
            '<div class="video-frame">' +
                '<span class="video-tag">' + (isShort ? 'Short' : esc(v.length || 'Video')) + '</span>' +
                '<img src="https://i.ytimg.com/vi/' + esc(v.id) + '/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">' +
                '<button class="video-play" type="button" data-id="' + esc(v.id) + '" aria-label="Play: ' + esc(v.title) + '"><span><i class="fas fa-play" aria-hidden="true"></i></span></button>' +
            '</div>' +
            '<div class="video-body">' +
                '<h3>' + esc(v.title) + '</h3>' +
                (v.text ? '<p>' + esc(v.text) + '</p>' : '') +
                '<div class="video-meta"><span>' + esc(catLabel(v.cat)) + '</span><a href="' + watchUrl + '" target="_blank" rel="noopener">Watch on YouTube <i class="fas fa-arrow-up-right-from-square" aria-hidden="true"></i></a></div>' +
            '</div>' +
        '</article>';
    }

    function renderVideos(target, list) {
        var el = document.getElementById(target);
        if (!el) return;
        el.innerHTML = list.map(videoCard).join('') + (el.dataset.append && !videos.some(function (v) { return v.replacesSoon; }) ? document.getElementById(el.dataset.append).innerHTML : '');
    }

    // Videos with a "from" date stay hidden until they go public on YouTube
    var now = Date.now();
    var videos = (HY.VIDEOS || []).filter(function (v) { return !v.from || Date.parse(v.from) <= now; });
    renderVideos('long-videos', videos.filter(function (v) { return v.type === 'long'; }));
    renderVideos('short-videos', videos.filter(function (v) { return v.type === 'short'; }));
    var featured = document.getElementById('featured-shorts');
    if (featured) {
        var pick = (featured.dataset.ids || '').split(',');
        renderVideos('featured-shorts', pick.map(function (id) {
            return videos.filter(function (v) { return v.id === id; })[0];
        }).filter(Boolean));
    }

    // Click-to-play: only load YouTube when the visitor asks (faster pages, more privacy)
    document.addEventListener('click', function (e) {
        var btn = e.target.closest('.video-play');
        if (!btn) return;
        var frame = btn.parentNode;
        var id = btn.getAttribute('data-id');
        var iframe = document.createElement('iframe');
        iframe.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1&rel=0&modestbranding=1';
        iframe.title = btn.getAttribute('aria-label').replace(/^Play: /, '');
        iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
        iframe.allowFullscreen = true;
        frame.innerHTML = '';
        frame.appendChild(iframe);
    });

    var videoFilters = document.getElementById('video-filters');
    if (videoFilters) {
        videoFilters.innerHTML = Object.keys(HY.VIDEO_CATS).map(function (k, i) {
            return '<button class="chip" type="button" data-cat="' + k + '" aria-pressed="' + (i === 0) + '">' + esc(HY.VIDEO_CATS[k]) + '</button>';
        }).join('');
        videoFilters.addEventListener('click', function (e) {
            var b = e.target.closest('.chip');
            if (!b) return;
            videoFilters.querySelectorAll('.chip').forEach(function (c) { c.setAttribute('aria-pressed', c === b ? 'true' : 'false'); });
            var cat = b.dataset.cat;
            document.querySelectorAll('#long-videos .video, #short-videos .video').forEach(function (card) {
                card.hidden = !(cat === 'all' || card.dataset.cat === cat);
            });
        });
    }

    /* ---------- Recipes ---------- */
    var recipeGrid = document.getElementById('recipe-grid');
    if (recipeGrid && HY.RECIPES) {
        var pillClass = { Drink: 'plum', Snack: 'rose' };
        recipeGrid.innerHTML = HY.RECIPES.map(function (r) {
            return '<article class="recipe reveal" data-goals="' + esc(r.goals.join('|')) + '" data-meal="' + esc(r.meal) + '">' +
                '<div class="recipe-top"><div class="recipe-emoji" aria-hidden="true">' + r.emoji + '</div>' +
                '<div><h3>' + esc(r.name) + '</h3><p>' + esc(r.blurb) + '</p></div></div>' +
                '<div class="recipe-facts">' +
                    '<span class="pill ' + (pillClass[r.meal] || '') + '">' + esc(r.meal) + '</span>' +
                    '<span class="pill"><i class="far fa-clock" aria-hidden="true"></i> ' + esc(r.time) + '</span>' +
                    '<span class="pill">Serves ' + esc(r.serves) + '</span>' +
                    r.goals.map(function (g) { return '<span class="pill rose">' + esc(g) + '</span>'; }).join('') +
                '</div>' +
                '<details><summary><i class="fas fa-chevron-right" aria-hidden="true"></i> Ingredients &amp; method</summary>' +
                    '<h4>Ingredients</h4><ul>' + r.ingredients.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>' +
                    '<h4>Method</h4><ol>' + r.steps.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ol>' +
                    '<p class="why"><strong>Why it helps:</strong> ' + esc(r.why) + '</p>' +
                '</details>' +
            '</article>';
        }).join('');

        // Structured data so recipes can appear as rich results in Google
        var ld = HY.RECIPES.map(function (r) {
            return {
                '@context': 'https://schema.org', '@type': 'Recipe', name: r.name, description: r.blurb,
                author: { '@type': 'Person', name: 'Yogeeta Sharma' },
                recipeCategory: r.meal, recipeYield: r.serves, keywords: r.goals.join(', '),
                recipeIngredient: r.ingredients,
                recipeInstructions: r.steps.map(function (s) { return { '@type': 'HowToStep', text: s }; })
            };
        });
        var s = document.createElement('script');
        s.type = 'application/ld+json';
        s.textContent = JSON.stringify(ld);
        document.head.appendChild(s);

        var goals = ['All'];
        HY.RECIPES.forEach(function (r) { r.goals.forEach(function (g) { if (goals.indexOf(g) < 0) goals.push(g); }); });
        var rf = document.getElementById('recipe-filters');
        if (rf) {
            rf.innerHTML = goals.map(function (g, i) {
                return '<button class="chip" type="button" data-goal="' + esc(g) + '" aria-pressed="' + (i === 0) + '">' + esc(g) + '</button>';
            }).join('');
            rf.addEventListener('click', function (e) {
                var b = e.target.closest('.chip');
                if (!b) return;
                rf.querySelectorAll('.chip').forEach(function (c) { c.setAttribute('aria-pressed', c === b ? 'true' : 'false'); });
                var g = b.dataset.goal;
                recipeGrid.querySelectorAll('.recipe').forEach(function (card) {
                    card.hidden = !(g === 'All' || card.dataset.goals.split('|').indexOf(g) >= 0);
                });
            });
        }
    }

    /* ---------- Reveal on scroll ---------- */
    var items = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('visible'); io.unobserve(en.target); } });
        }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
        items.forEach(function (el) { io.observe(el); });
    } else {
        items.forEach(function (el) { el.classList.add('visible'); });
    }
})();
