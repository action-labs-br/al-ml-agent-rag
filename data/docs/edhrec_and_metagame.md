# EDHREC and the Commander Metagame

## What Is EDHREC?

**EDHREC** (edhrec.com) is the most comprehensive data aggregation platform for Commander deckbuilding. Founded in 2014, it scrapes publicly shared decklists from sources including Archidekt, Moxfield, TappedOut, and Deckstats. As of 2024, EDHREC tracks data from over **2 million decklists** and catalogs virtually every card legal in Commander.

EDHREC provides statistics on how frequently each card appears in Commander decks, both globally (across all decks) and per-commander (how often a card appears in decks led by a specific commander). This data makes EDHREC the definitive source for understanding the Commander metagame.

## EDHREC Rank

The **EDHREC rank** is a numerical ranking from 1 to approximately 25,000+ that measures a card's overall popularity in Commander. Key properties:

- **Lower rank = more popular**. Rank 1 is the most-played card in the format.
- **Rank 1: Sol Ring** — Appears in approximately **67% of all Commander decks** tracked by EDHREC. It has held the #1 position since EDHREC's inception.
- **Rank 2-5 typically**: Command Tower (~65% of decks), Arcane Signet (~58% of decks), Lightning Greaves (~35% of decks), Swords to Plowshares (~30% of decks).
- **Rank 100**: Cards in approximately 15-20% of eligible decks.
- **Rank 1000**: Cards in approximately 3-5% of eligible decks.
- **Rank 5000+**: Niche cards appearing in less than 1% of decks.
- **Rank 15000+**: Very rarely played cards, often draft chaff or highly specialized combo pieces.

The rank is computed from the card's inclusion rate across all tracked decklists, weighted by recency (newer decklists count slightly more).

## Factors That Determine EDHREC Rank

### 1. Universality (Color Identity)
The single biggest structural factor. A **colorless** card (no color identity) can go in every Commander deck, giving it the widest possible audience. A mono-colored card can only go in decks that include its color. A 3-color card has the narrowest audience.

- Sol Ring (colorless): 67% inclusion → Rank 1
- Swords to Plowshares (W): ~30% of white-inclusive decks → Rank ~5
- Counterspell (U): ~25% of blue-inclusive decks → Rank ~15
- A 3-color gold card: max audience is ~15-20% of all decks even at 100% adoption

This is why the top 20 EDHREC cards are almost entirely **colorless artifacts and lands**.

### 2. Power Level
Cards that provide efficient, universally useful effects rank well:
- **Mana acceleration**: Sol Ring, Arcane Signet, Mana Crypt
- **Card advantage**: Rhystic Study, Mystic Remora, Sylvan Library
- **Removal**: Swords to Plowshares, Cyclonic Rift, Beast Within
- **Protection**: Lightning Greaves, Swiftfoot Boots
- **Mana fixing lands**: Command Tower, Exotic Orchard

### 3. Recency Bias
Newly released cards tend to enter EDHREC with **inflated popularity** because:
- Players are excited to try new cards
- Content creators feature new cards prominently
- EDHREC weights recent decklists more heavily

Over time (6-12 months), the hype settles and the card finds its true rank. This means a card released in 2023 might initially rank at #500 but stabilize at #2000 once the novelty wears off.

This temporal pattern is the primary reason that **`card_age_days` is the single strongest predictor** of EDHREC rank in the dataset. Newer cards (smaller card_age_days) tend to have better (lower) ranks, but this is partly a measurement artifact — not because newer cards are inherently better.

### 4. Price Accessibility
Card prices significantly affect play rates:
- A $1 uncommon that's moderately good will see more play than a $50 rare that's slightly better
- Reprints that lower a card's price cause its EDHREC rank to improve
- Reserved List cards (which cannot be reprinted) often have worse ranks than their power level would suggest because fewer players own them
- Example: Mana Crypt (cEDH staple, ~$150) ranks worse than Arcane Signet (~$1) despite being more powerful, purely due to price

### 5. Commander-Specific Synergies
Some cards are played in a narrow set of decks but at very high rates:
- Goblin tribal cards rank well within Krenko decks but poorly overall
- Combo pieces (Thassa's Oracle, Demonic Consultation) are cEDH staples but rare in casual
- Niche enchantments or artifacts that combo with specific commanders

## Staples vs. Niche Cards

### Universal Staples (Rank 1-100)
Cards that go in nearly every deck of their color:
- **Colorless**: Sol Ring, Command Tower, Arcane Signet, Lightning Greaves, Swiftfoot Boots, Thought Vessel, Sol Ring, Reliquary Tower
- **White**: Swords to Plowshares, Path to Exile, Smothering Tithe, Generous Gift
- **Blue**: Counterspell, Rhystic Study, Cyclonic Rift, Swan Song
- **Black**: Demonic Tutor, Toxic Deluge, Feed the Swarm, Vampiric Tutor
- **Red**: Chaos Warp, Blasphemous Act, Dockside Extortionist, Vandalblast
- **Green**: Cultivate, Kodama's Reach, Beast Within, Sakura-Tribe Elder

### Niche Cards (Rank 5000+)
Cards that are powerful in specific contexts but rarely played overall:
- Tribal support cards (Elvish Archdruid — only in Elf decks)
- Color-specific hosers (Red Elemental Blast — only in competitive blue-heavy metas)
- Narrow combo pieces (Basalt Monolith — primarily in infinite mana combos)
- Draft/Limited-designed cards that lack Commander power level

## cEDH vs. Casual Commander

The Commander community spans a wide power spectrum:

### Casual (90%+ of players)
- Games last 60-90 minutes
- Budget considerations ($50-$500 decks)
- Social contract, no infinite combos before turn 8-10
- Value-oriented: Rhystic Study, Smothering Tithe, big haymakers
- EDHREC rankings primarily reflect casual play patterns

### Competitive EDH (cEDH) (<10% of players)
- Games end by turn 3-5
- Budget not restricted ($1000-$5000+ decks)
- Fast mana: Mana Crypt, Chrome Mox, Mox Diamond
- Efficient interaction: Force of Will, Fierce Guardianship, Pact of Negation
- Compact win conditions: Thassa's Oracle + Demonic Consultation, Ad Nauseam
- cEDH card priorities differ significantly from casual, but because cEDH represents a small fraction of all decks, EDHREC ranks mostly reflect casual preferences

## Metagame Shifts

Several factors cause the Commander metagame to shift over time:

### Bans and Unbans
When a card is banned (e.g., Golos, Tireless Pilgrim in 2021), its EDHREC rank plummets as it's removed from all decklists. When a card is unbanned, it surges. Bans in adjacent formats (Standard, Modern) don't directly affect Commander legality but can influence perception.

### New Printings
New sets release every 2-3 months, each introducing hundreds of new cards. Cards that are strict upgrades to existing staples can displace them:
- Generous Gift replaced Beast Within in many white decks (same effect, easier mana cost for white)
- Farewell displaced older board wipes like Austere Command in many decks
- Each new Commander precon introduces unique cards that often become instant staples

### Content Creators
The Commander community is heavily influenced by content creators:
- **The Command Zone** (YouTube, 1M+ subscribers) — Game Knights episodes showcase commanders and strategies that see play spikes
- **Tolarian Community College** (YouTube, 900K+ subscribers) — Product reviews and deck techs
- **EDHREC's own articles** — "Top 10" lists and set reviews influence deckbuilding

When a popular creator features a card or commander, EDHREC often shows a measurable spike in that card's inclusion rate within days.

### Temporal Patterns in the Dataset

The dataset feature `card_age_days` (days since the card was released) is the **strongest single predictor** of EDHREC rank. This happens because:

1. **Newer cards start with hype-inflated ranks** — Players add new cards to decks quickly, creating temporarily high inclusion rates.
2. **Older cards have had time to be forgotten** — Even good older cards may have worse EDHREC ranks than inferior newer cards simply because fewer recent decklists include them.
3. **EDHREC's recency weighting** — The algorithm weights recent decklists more, amplifying the effect.
4. **Power creep** — Newer cards genuinely are stronger on average due to design philosophy shifts.

This means a naive model might over-rely on `card_age_days` and learn that "newer = more popular" without understanding the actual card attributes that drive popularity. A robust model should capture both the temporal effect and the intrinsic card qualities (CMC, color identity, rarity, card type, keywords) that determine long-term popularity.

### Seasonal Patterns
- Commander precon release months (typically August, November) see spikes in new deck registrations
- "Spoiler season" (2-3 weeks before each set release) generates speculation and pre-registration of new cards
- End-of-year retrospectives cause classic staples to resurface in decklists
