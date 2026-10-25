# (review, label). Alternating positive/negative so every slice stays balanced.
DATA = [
    ("Absolutely loved this movie, the acting was fantastic.", "positive"),
    ("Terrible experience, the food was cold and the waiter was rude.", "negative"),
    ("The battery lasts all day and the screen is gorgeous.", "positive"),
    ("The phone broke after two days. Complete waste of money.", "negative"),
    ("Great service, the staff were friendly and quick.", "positive"),
    ("Boring plot and wooden acting, I nearly fell asleep.", "negative"),
    ("Best pizza I've had in years, will definitely come back.", "positive"),
    ("Way too expensive for what you get.", "negative"),
    ("Easy to set up and works perfectly.", "positive"),
    ("The app crashes every time I open it.", "negative"),
    ("The book kept me hooked from the first page to the last.", "positive"),
    ("Shipping took a month and the box arrived damaged.", "negative"),
    ("Fast delivery and the product was exactly as described.", "positive"),
    ("I wouldn't recommend this to anyone.", "negative"),
    ("I'm so happy with this purchase, totally worth the money.", "positive"),
    ("The room smelled awful and the bed was uncomfortable.", "negative"),
    ("The hotel room was spotless and the view was breathtaking.", "positive"),
    ("I thought it would be great, but it was a huge letdown.", "negative"),
    ("Surprisingly good for the price, I'd recommend it.", "positive"),
    ("Oh great, another update that breaks everything.", "negative"),
    ("Not bad at all, actually quite enjoyable.", "positive"),
    ("The manual is useless and support never replied.", "negative"),
    ("I expected to hate it, but it won me over completely.", "positive"),
    ("Cheaply made, the handle snapped on first use.", "negative"),
    ("The concert was incredible, I got chills.", "positive"),
    ("Disappointing. The description was completely misleading.", "negative"),
    ("Customer support solved my problem in minutes.", "positive"),
    ("Loud, slow and overpriced.", "negative"),
    ("Comfortable, stylish, and durable. Five stars.", "positive"),
    ("Not good. Not good at all.", "negative"),
]

# The split that matters later:
DEV = DATA[:20]        # you tune prompts on these
HELD_OUT = DATA[20:]   # you only check these at the end




# Harder reviews: sarcasm, mixed opinions, negation. 11 positive / 11 negative.
HARD = [
    ("I can't say I didn't enjoy it.", "positive"),
    ("Yeah, because waiting two hours for cold food is exactly what I wanted.", "negative"),
    ("The plot was predictable, but the performances made it worth watching.", "positive"),
    ("Great camera, but the battery died within hours and support was useless.", "negative"),
    ("Not exactly a masterpiece, yet I smiled the whole way through.", "positive"),
    ("I wanted to love this, but it just never delivered.", "negative"),
    ("Hardly the disaster I was warned about. It works fine.", "positive"),
    ("Thanks for nothing, customer service.", "negative"),
    ("No complaints whatsoever.", "positive"),
    ("If you enjoy wasting money, this is perfect for you.", "negative"),
    ("The first half dragged, but the ending completely blew me away.", "positive"),
    ("Stunning visuals, shame about everything else.", "negative"),
    ("Never again will I shop anywhere else.", "positive"),
    ("Looks great in photos; in person it's a flimsy piece of junk.", "negative"),
    ("The service was slow, but the food was so good I forgot about the wait.", "positive"),
    ("I'd give zero stars if I could.", "negative"),
    ("Couldn't put it down, stayed up until 3am reading.", "positive"),
    ("I keep waiting for it to get good. It never does.", "negative"),
    ("Honestly, I'd pay double for this.", "positive"),
    ("Fine for a day, then it fell apart.", "negative"),
    ("It does what it says, nothing more, and I'm satisfied.", "positive"),
    ("A true masterpiece of boredom.", "negative"),
]
