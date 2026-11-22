/* =========================================================
   The Hormonal Yogini — site content
   ---------------------------------------------------------
   To add a YouTube video: copy one line in VIDEOS and change
   the id (the part after "v=" or "/shorts/" in the link).
   To add a recipe: copy one block in RECIPES.
   ========================================================= */

window.HY = window.HY || {};

HY.LINKS = {
    youtube: 'https://www.youtube.com/@thehormonalyogini',
    youtubeSubscribe: 'https://www.youtube.com/@thehormonalyogini?sub_confirmation=1',
    instagram: 'https://www.instagram.com/thehormonalyogini/',
    // tiktok: 'https://www.tiktok.com/@thehormonalyogini',  // add when the account is live
    portfolio: 'https://sharmayogeeta.github.io/portfolio/'
};

/* Video categories: hormones | calm | back | everyday
   type: "long" (normal video) or "short" (YouTube Short)       */
HY.VIDEOS = [
    // ---- Full classes ----
    { id: 'BhFDJNEQH_M', type: 'long',  cat: 'hormones', title: 'Yoga for Hormone Balance: 8 Gentle Poses for Women', length: '4:38',
      text: 'A slow outdoor flow to support your endocrine system, ease tension and help you feel more like yourself.' },
    { id: 'cY-Lb4bp_jg', type: 'long',  cat: 'calm',     title: '5-Minute Morning Yoga to Calm Your Nervous System (Toddler Approved)', length: '3:21',
      text: 'Real-life morning yoga for busy mums: gentle stretches and breathing to start the day calm.' },

    // ---- Shorts ----
    { id: 'bHVmZ7n9TSI', type: 'short', cat: 'hormones', title: 'Hormonal balance yoga' },
    { id: 'BQ9oVb43M58', type: 'short', cat: 'hormones', title: 'Take care of your hormones' },
    { id: 'C4Cfqkc1QvA', type: 'short', cat: 'hormones', title: 'Yoga for back and thyroid' },
    { id: 'DMq4INEO4S8', type: 'short', cat: 'calm',     title: '1-minute belly breathing' },
    { id: 'y-1408jk1Fo', type: 'short', cat: 'calm',     title: 'Learn about your nervous system' },
    { id: 'Lj0u5wvqhH0', type: 'short', cat: 'calm',     title: 'Nervous system reset yoga' },
    { id: 'NwVEk2jRtZ8', type: 'short', cat: 'calm',     title: 'Morning nervous system reset' },
    { id: 'uD1cZSNling', type: 'short', cat: 'back',     title: 'Yoga for back pain' },
    { id: 'h4Veu3T5hiY', type: 'short', cat: 'back',     title: 'Open your chest and shoulders' },
    { id: '8H5cFCLwDrE', type: 'short', cat: 'back',     title: 'The power of Cobra pose' },
    { id: '7u8iF6XAFmg', type: 'short', cat: 'back',     title: 'Back yoga' },
    { id: 'P9jGsyRWjUY', type: 'short', cat: 'everyday', title: 'Yoga for digestion and constipation' },
    { id: '5LElHP0JWfY', type: 'short', cat: 'everyday', title: 'Transformation' },
    { id: 'oipHKnup7a8', type: 'short', cat: 'everyday', title: 'Love your body' },
    { id: '7bL26cHZuO8', type: 'short', cat: 'everyday', title: 'Be kind to yourself' },
    { id: '0ckLwNB_NHM', type: 'short', cat: 'everyday', title: 'Surrender and stretch' },
    { id: 'TeASF9kPqwY', type: 'short', cat: 'everyday', title: 'Daily yoga' }
];

HY.VIDEO_CATS = {
    all: 'All',
    hormones: 'Hormone balance',
    calm: 'Stress & nervous system',
    back: 'Back & posture',
    everyday: 'Everyday wellbeing'
};

/* Recipe "meal": Breakfast | Main | Snack | Drink
   "goals" are used for the filter buttons.                       */
HY.RECIPES = [
    {
        name: 'Seed-Cycling Energy Balls', emoji: '🌰', meal: 'Snack', time: '15 min', serves: '12 balls',
        goals: ['Period-friendly', 'Hormone balance'],
        blurb: 'Two no-bake batches: flax & pumpkin for the first half of your cycle, sesame & sunflower for the second.',
        ingredients: [
            '120 g soft dates, pitted', '40 g rolled oats',
            'Days 1–14: 2 tbsp ground flaxseed + 2 tbsp pumpkin seeds',
            'Days 15–28: 2 tbsp sesame seeds + 2 tbsp sunflower seeds',
            '1 tbsp nut butter', 'Pinch of cinnamon and sea salt'
        ],
        steps: [
            'Blitz the dates and oats in a food processor until sticky.',
            'Add the seeds for the phase you are in, the nut butter, cinnamon and salt. Pulse to combine.',
            'Roll into 12 balls and chill for 20 minutes. Keeps 5 days in the fridge.'
        ],
        why: 'Seeds bring fibre, healthy fats, zinc and magnesium. Seed cycling is a gentle ritual many women enjoy; the bigger win is simply eating more seeds every day.'
    },
    {
        name: 'Golden Turmeric Moon Milk', emoji: '🥛', meal: 'Drink', time: '5 min', serves: '1 mug',
        goals: ['Calm & sleep', 'Period-friendly'],
        blurb: 'A warm, caffeine-free bedtime drink with turmeric, ginger and a pinch of black pepper.',
        ingredients: [
            '250 ml milk or unsweetened oat milk', '½ tsp ground turmeric', '¼ tsp ground ginger',
            '¼ tsp cinnamon', 'Pinch of black pepper', '1 tsp honey or maple syrup (optional)'
        ],
        steps: [
            'Whisk everything except the honey in a small pan.',
            'Warm gently for 3–4 minutes without boiling.',
            'Pour into a mug, sweeten if you like, and sip slowly away from screens.'
        ],
        why: 'A warm, comforting ritual helps signal "rest" to your nervous system. Black pepper helps your body absorb the curcumin in turmeric.'
    },
    {
        name: 'Ginger, Cinnamon & Fennel Period Tea', emoji: '🫖', meal: 'Drink', time: '10 min', serves: '2 cups',
        goals: ['Period-friendly'],
        blurb: 'A soothing spiced tea to sip with a hot water bottle on heavy, crampy days.',
        ingredients: [
            '3 cm fresh ginger, sliced', '1 cinnamon stick', '1 tsp fennel seeds',
            '500 ml water', 'Squeeze of lemon and a little honey to taste'
        ],
        steps: [
            'Lightly crush the fennel seeds.',
            'Simmer the ginger, cinnamon and fennel in the water for 8–10 minutes.',
            'Strain, add lemon and honey, and drink warm.'
        ],
        why: 'Ginger has been studied for easing period pain, and warm drinks plus gentle movement can help cramping muscles relax.'
    },
    {
        name: 'Spinach & Moong Dal', emoji: '🍲', meal: 'Main', time: '30 min', serves: '4',
        goals: ['Iron-rich', 'Postpartum', 'High-protein'],
        blurb: 'Creamy yellow lentils with a whole bag of spinach, finished with a cumin and garlic tadka.',
        ingredients: [
            '200 g split yellow moong dal, rinsed', '800 ml water', '½ tsp turmeric',
            '200 g spinach, chopped', '1 tbsp ghee or oil', '1 tsp cumin seeds',
            '3 garlic cloves, sliced', '1 small onion and 1 tomato, chopped', 'Salt, chilli and lemon to taste'
        ],
        steps: [
            'Simmer the dal with the water and turmeric for 20 minutes until soft.',
            'Stir in the spinach and cook 2–3 minutes until wilted.',
            'Heat the ghee, sizzle the cumin and garlic, then soften the onion and tomato. Pour over the dal.',
            'Season, add a squeeze of lemon and serve with rice or roti.'
        ],
        why: 'Lentils and leafy greens give plant iron and protein. The vitamin C in lemon and tomato helps your body absorb that iron, which matters if your periods are heavy.'
    },
    {
        name: 'Flax & Berry Overnight Oats', emoji: '🫐', meal: 'Breakfast', time: '5 min + overnight', serves: '1',
        goals: ['Hormone balance', 'High-protein'],
        blurb: 'Prep in five minutes the night before. Fibre, protein and colour for a steady-energy morning.',
        ingredients: [
            '45 g rolled oats', '1 tbsp ground flaxseed', '1 tbsp chia seeds',
            '100 g Greek or soya yoghurt', '120 ml milk of choice', 'Handful of berries', 'Cinnamon'
        ],
        steps: [
            'Stir the oats, flax, chia, yoghurt, milk and cinnamon together in a jar.',
            'Cover and refrigerate overnight.',
            'Top with berries in the morning. Eat cold or warm through.'
        ],
        why: 'A breakfast with protein and fibre helps keep blood sugar steady, which can mean fewer mid-morning crashes and cravings.'
    },
    {
        name: 'Ragi (Finger Millet) Porridge', emoji: '🥣', meal: 'Breakfast', time: '10 min', serves: '1',
        goals: ['Iron-rich', 'Postpartum'],
        blurb: 'A traditional South Indian porridge, nutty and smooth, sweetened with jaggery and cardamom.',
        ingredients: [
            '3 tbsp ragi flour', '250 ml milk or water', '1–2 tsp jaggery', 'Pinch of cardamom',
            'Chopped almonds or walnuts to top'
        ],
        steps: [
            'Whisk the ragi flour into a little cold milk until smooth.',
            'Add the rest of the milk and cook on low heat, stirring, for 5–7 minutes until thick.',
            'Stir in jaggery and cardamom, then top with nuts.'
        ],
        why: 'Ragi is naturally rich in calcium and also offers iron and fibre, which is why it is a popular food for new mums in India.'
    },
    {
        name: 'Chickpea & Quinoa Glow Bowl', emoji: '🥗', meal: 'Main', time: '25 min', serves: '2',
        goals: ['High-protein', 'Hormone balance'],
        blurb: 'Roasted veg, crispy chickpeas and quinoa with a lemon-tahini dressing. Great for lunchboxes.',
        ingredients: [
            '100 g quinoa', '1 tin chickpeas, drained', '1 sweet potato, cubed', '1 red pepper, sliced',
            'Handful of rocket or spinach', '½ avocado',
            'Dressing: 2 tbsp tahini, juice of ½ lemon, 1 tsp maple syrup, water to loosen'
        ],
        steps: [
            'Roast the sweet potato, pepper and chickpeas with oil, salt and paprika at 200°C for 20–25 minutes.',
            'Meanwhile cook the quinoa.',
            'Whisk the dressing. Build bowls with greens, quinoa, roasted veg, avocado and a generous drizzle.'
        ],
        why: 'Protein, fibre and healthy fats in every bowl keep you full and help balance blood sugar, a foundation for steadier hormones.'
    },
    {
        name: 'Gentle Vegetable Khichdi', emoji: '🍛', meal: 'Main', time: '35 min', serves: '3',
        goals: ['Postpartum', 'Calm & sleep'],
        blurb: 'One-pot rice and lentils with vegetables and ghee. Easy to digest and deeply comforting.',
        ingredients: [
            '100 g basmati rice', '100 g split moong dal', '1 litre water', '½ tsp turmeric',
            '1 carrot and a handful of peas or beans', '1 tbsp ghee', '1 tsp cumin seeds', 'Pinch of asafoetida',
            '2 cm ginger, grated', 'Salt to taste'
        ],
        steps: [
            'Rinse the rice and dal together.',
            'Warm the ghee, add cumin, asafoetida and ginger, then the rice, dal, vegetables, turmeric and water.',
            'Simmer covered for 25 minutes (or 3 whistles in a pressure cooker) until soft and porridge-like.',
            'Season and serve with yoghurt and a little extra ghee.'
        ],
        why: 'Khichdi is a classic recovery food: warm, soft and easy on the gut, which makes it ideal on low-energy days or after birth.'
    },
    {
        name: 'Dark Chocolate Date Bites', emoji: '🍫', meal: 'Snack', time: '15 min', serves: '10 bites',
        goals: ['Period-friendly', 'Calm & sleep'],
        blurb: 'For PMS chocolate cravings: stuffed dates dipped in 70% dark chocolate with sea salt.',
        ingredients: [
            '10 Medjool dates', '10 tsp almond or peanut butter', '60 g dark chocolate (70%+)',
            'Flaky sea salt', 'Crushed pistachios (optional)'
        ],
        steps: [
            'Slit and stone the dates, then fill each with a teaspoon of nut butter.',
            'Melt the chocolate and dip or drizzle over the dates.',
            'Sprinkle with salt and pistachios and chill until set.'
        ],
        why: 'Dark chocolate, nuts and dates provide magnesium, a mineral often linked to easing PMS symptoms, in a treat that still feels like a treat.'
    }
];
