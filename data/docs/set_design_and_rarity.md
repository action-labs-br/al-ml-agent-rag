# Set Design and Rarity in Magic: The Gathering

## Rarity System

Every Magic card is printed at one of four rarities, indicated by the color of the set symbol:

### Common (Black set symbol)
Commons are the most frequently opened cards in booster packs (~10 per 15-card pack). They are designed to be:
- **Simple** — Under the "New World Order" design principle (adopted in 2008), commons must be understandable by new players. Complex mechanics are reserved for higher rarities.
- **Draft workhorses** — Commons form the backbone of Limited (draft/sealed) decks. Cards like Murder, Negate, and Rampant Growth are common-rarity staples.
- **Low individual impact** — Commons rarely define constructed formats. However, some commons are Commander staples: Sol Ring was originally common (Alpha), and cards like Brainstorm, Ponder, Preordain, and Swords to Plowshares were common in their first printing.
- **EDHREC impact** — Commons tend to have worse (higher) EDHREC ranks on average because most are designed for Limited and lack the power level for Commander. Exceptions are the all-time great commons mentioned above.

### Uncommon (Silver set symbol)
Uncommons appear ~3 per booster pack and occupy a middle ground:
- **Build-around potential** — Uncommons are often the cards that define draft archetypes. Cards like Talisman of Dominance, Counterspell (uncommon in many printings), and Lightning Greaves are uncommon.
- **Stronger effects** — More complex and powerful than commons, but not splashy enough for rare.
- **Commander relevance** — Many Commander staples are uncommon: Arcane Signet, Swords to Plowshares, Beast Within, Cultivate, and Sakura-Tribe Elder. These cards provide efficient, universally useful effects.
- **Lower price point** — Uncommons are more accessible than rares/mythics, which contributes to higher play rates and better EDHREC ranks for the best uncommons.

### Rare (Gold set symbol)
Rares appear 1 per booster pack and represent powerful, complex, or build-around cards:
- **Format-defining power** — Cards like Rhystic Study, Smothering Tithe, Cyclonic Rift, and Dockside Extortionist are rare.
- **Higher complexity** — Rares can have multiple abilities, complex interactions, and niche strategies.
- **Economic impact** — Rares drive pack sales and secondary market prices. Powerful rares range from $1 to $50+ depending on demand.
- **Commander popularity** — The best rares rank very well on EDHREC because they offer unique, powerful effects. However, the average rare ranks worse than the average uncommon staple because many rares are niche or format-specific.

### Mythic Rare (Orange/red set symbol)
Introduced in Alara block (2008), mythic rares appear in roughly 1 in 8 packs:
- **Splashy and complex** — Mythics are designed to feel special: powerful planeswalkers, massive creatures, game-warping effects.
- **Low print run** — About 2x rarer than regular rares, driving up prices.
- **Examples** — Craterhoof Behemoth, Mana Crypt, The Great Henge, Expropriate, Doubling Season. These are some of the most impactful cards in Commander.
- **Price barrier** — Mythic staples can cost $20-$100+, which limits play rates. This creates an interesting dynamic where a mythic might be extremely powerful but have a mediocre EDHREC rank because fewer players own copies.
- **Bonus/Special rarity** — Some datasets include "bonus" as a rarity for special promotional printings (e.g., Timeshifted cards, The List inserts). These often behave similarly to rare or mythic in terms of power level.

## New World Order (NWO)

Adopted by Wizards of the Coast R&D in 2008, New World Order is a design philosophy that restricts complexity at common:
- Commons should have at most one ability
- Board complexity (number of game-relevant things to track) should be manageable
- Complex keywords appear at uncommon or higher
- This explains why common cards in the dataset tend to have shorter oracle text (lower oracle_text_length) and fewer keywords

## Set Types

Magic cards are released in different types of sets, each with distinct design goals:

### Expansion (Standard-Legal Sets)
The primary product line, released 3-4 times per year. Examples: Throne of Eldraine, Innistrad: Midnight Hunt, Phyrexia: All Will Be One, Wilds of Eldraine.
- **Standard format**: Cards are legal in Standard for ~2 years after release
- **Draft environment**: Designed for a balanced Limited experience
- **New mechanics**: Each expansion introduces 2-4 new keyword mechanics
- **Commander impact**: Many Commander staples originate in Standard sets because of the large print run and wide availability

### Core Sets
Simpler sets focused on evergreen mechanics, designed for new players. Core sets were discontinued after Core Set 2021 but historically introduced cards like Llanowar Elves, Shivan Dragon, and Serra Angel. Core set cards tend to have simpler oracle text and fewer keywords.

### Commander Products
Sets designed specifically for Commander play:
- **Commander preconstructed decks** (2011-present) — 4-5 precon decks per year, each with a ready-to-play 100-card deck including new cards exclusive to the product. Cards like Dockside Extortionist, Fierce Guardianship, and Deflecting Swat were printed exclusively in Commander products.
- **Commander Legends** (2020) — The first Commander draft set. Introduced powerful cards like Jeweled Lotus, Hullbreacher (later banned), and Court of Grace.
- **Commander Legends: Battle for Baldur's Gate** (2022) — Second Commander draft set with D&D flavor.
- **Commander Masters** (2023) — Reprint set focused on Commander staples.

### Masters Sets
Reprint-focused sets with higher price points ($10-15 per pack vs $4-5 for Standard packs):
- Modern Masters, Eternal Masters, Ultimate Masters, Double Masters, Commander Masters
- Contain only reprints of existing cards
- Help increase supply of expensive staples
- Cards in these sets have `is_reprint = True` in the dataset

### Supplemental Products
- **Secret Lair** — Limited-run collectible products with alternate art versions
- **Un-sets** (Unglued, Unhinged, Unstable, Unfinity) — Comedic, silver-bordered sets with unusual mechanics. Some Unfinity cards are legal in Commander.
- **Universes Beyond** — Crossover sets featuring IP like Lord of the Rings, Warhammer 40K, Doctor Who, and Fallout. These have introduced many popular Commander cards.

## The Reserved List

In 1996, after the Chronicles reprint set tanked the secondary market value of older cards, Wizards of the Coast created the **Reserved List** — a promise to never reprint certain cards. This list includes some of the most powerful cards ever printed:

- **Black Lotus** — 0 mana, sacrifice for 3 mana of any color. The most valuable Magic card (~$100,000+ for Alpha printing).
- **Original Dual Lands** — Underground Sea, Volcanic Island, Tundra, etc. The best mana fixing ever printed ($200-$1000+ each).
- **Time Walk** — 2 mana, take an extra turn.
- **Ancestral Recall** — 1 mana, draw 3 cards.
- **Mox Sapphire, Mox Jet, Mox Ruby, Mox Pearl, Mox Emerald** — 0-mana rocks that produce colored mana.

Reserved List cards appear in the dataset with `is_reserved = True`. Because they can never be reprinted, their supply is fixed and prices are extremely high. Despite their power, many Reserved List cards have mediocre EDHREC ranks because so few players own them. This makes `is_reserved` an interesting feature: it correlates with high power but limited adoption.

## Reprints and Supply

A card being reprinted (`is_reprint = True`) has important implications:
- **Increased supply** lowers prices, making the card accessible to more players
- **Multiple printings** in the dataset may represent different set contexts
- **Price accessibility** is a major factor in EDHREC popularity — a $1 staple will see more play than a $50 staple of similar power level
- **Recent reprints** often spike in EDHREC popularity as more players acquire copies

## Power Creep

Over Magic's 30+ year history, the average power level of new cards has gradually increased:
- Creatures have gotten significantly stronger (compare Grizzly Bears — 2 mana 2/2 from 1993 — to Tarmogoyf, Questing Beast, or Sheoldred, the Apocalypse)
- Free spells and cost reduction have proliferated (Fierce Guardianship, Deadly Rollick, Deflecting Swat — all free with your commander in play)
- Commander-specific designs push the envelope (Dockside Extortionist, Thassa's Oracle + Demonic Consultation combo)
- Newer cards on average have more oracle text, more keywords, and stronger effects per mana spent

This power creep means that `year_released` correlates with card quality — newer cards are often more powerful per mana cost. However, this interacts with the `card_age_days` temporal confound (see edhrec_and_metagame.md), making it a nuanced feature to model.

## Rarity Distribution in the Dataset

The MTG cards dataset reflects the actual rarity distribution of Magic cards:

| Rarity | Approximate % of Dataset | Avg EDHREC Rank |
|--------|-------------------------|-----------------|
| Common | ~35% | ~12,000 (worst avg — most are draft filler) |
| Uncommon | ~30% | ~9,500 |
| Rare | ~25% | ~7,500 |
| Mythic | ~8% | ~6,000 (best avg — but wide variance) |
| Bonus/Special | ~2% | ~8,000 (mixed — promotional, timeshifted) |

The correlation between rarity and EDHREC rank is meaningful but not straightforward. While mythics have the best average rank, there's enormous variance — a mythic bomb like Craterhoof Behemoth might rank in the top 100, while a niche mythic planeswalker might rank above 15,000.

## Set Type Distribution in the Dataset

The `set_type` feature in the dataset categorizes which product a card was printed in:

- **expansion** — Standard-legal sets (largest category, ~40% of dataset)
- **commander** — Commander-specific products (~15% of dataset)
- **masters** — Reprint sets like Double Masters, Commander Masters (~10%)
- **core** — Core Sets (~8%)
- **draft_innovation** — Sets like Modern Horizons, Conspiracy (~7%)
- **funny** — Un-sets and joke cards (~3%)
- **starter** — Starter products for new players (~2%)
- Other categories include: treasure_chest, promo, box, masterpiece, alchemy

Set type is a useful predictor because Commander-specific products (set_type = "commander") tend to have cards designed for the format and thus better EDHREC ranks on average. Expansion and core set cards are more variable, as they are designed for Standard/Limited first. Masters sets contain reprints of already-popular cards, so they tend to have good ranks as well.
