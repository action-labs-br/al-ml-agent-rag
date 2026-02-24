# Mana Curve and Card Evaluation in Commander

## Converted Mana Cost (CMC)

Every Magic card has a **converted mana cost** (CMC), also called **mana value** in modern terminology. CMC is the total amount of mana required to cast a spell, regardless of color. For example, a card costing {2}{W}{U} has a CMC of 4. CMC is one of the most important factors in determining a card's playability — cheaper cards are generally more versatile and can be deployed earlier.

In the dataset, CMC ranges from 0 (lands, free spells like Mana Crypt, Pact of Negation) to 16 (Draco). The majority of playable Commander cards fall between CMC 1 and 6.

## Mana Curve in Commander

The "mana curve" describes how a deck's cards are distributed across mana costs. A well-built Commander deck typically follows this distribution:

| CMC | Typical Count | Role |
|-----|--------------|------|
| 0   | 2-5 | Free spells, Mana Crypt, Mox Opal |
| 1   | 6-10 | Mana dorks (Llanowar Elves), cheap interaction (Swords to Plowshares, Swan Song) |
| 2   | 8-12 | Mana rocks (Arcane Signet, Signets), early threats, cheap removal |
| 3   | 7-10 | Key value pieces (Rhystic Study, Cultivate), removal (Beast Within) |
| 4   | 5-8 | Mid-range threats, board wipes (Wrath of God), powerful enchantments |
| 5   | 4-6 | Impactful threats, sweepers (Farewell, Cyclonic Rift overload) |
| 6+  | 3-6 | Finishers, haymakers (Craterhoof Behemoth), commanders with high CMC |
| Lands | 35-38 | Mana base — Command Tower, fetch lands, dual lands, utility lands |

A common deckbuilding mistake is loading up on expensive, flashy cards while neglecting the 1-3 CMC slots. In Commander, you need early plays to establish your board, even though the format is slower than 1v1 formats.

## Mana Ramp

Because Commander games require more mana (bigger spells, longer games), **mana ramp** — cards that accelerate your mana production — is essential. The best ramp comes online early (turns 1-3) and is cheap:

- **Sol Ring** (CMC 1) — Produces 2 colorless mana. The single best mana rock in the format. EDHREC rank #1.
- **Arcane Signet** (CMC 2) — Produces 1 mana of any color in your commander's color identity. In the top 5 most-played cards.
- **Signets** (CMC 2) — Azorius Signet, Dimir Signet, etc. Each produces 2 colors for a 1-mana activation.
- **Talismans** (CMC 2) — Similar to Signets but can tap for colorless without activation.
- **Cultivate / Kodama's Reach** (CMC 3) — Green sorceries that fetch two basic lands. Staples in any green deck.
- **Sakura-Tribe Elder** (CMC 2) — Green creature that sacrifices to fetch a basic land. Ramp + chump blocker.
- **Mana Crypt** (CMC 0) — Free Sol Ring with a coin-flip downside. cEDH staple, costs $150+.
- **Dockside Extortionist** (CMC 2) — Creates treasure tokens equal to opponents' artifacts and enchantments. Often generates 5-10+ mana in a single play.

A typical Commander deck runs **10-12 ramp sources** to consistently deploy threats ahead of curve.

## Card Advantage in Multiplayer

In a 4-player game, you draw 1 card per turn while your 3 opponents collectively draw 3 cards per turn. This means you're falling behind in resources every turn cycle unless you have card advantage engines. The best Commander cards address this multiplayer math:

- **Rhystic Study** — "Whenever an opponent casts a spell, you may draw a card unless they pay {1}." In practice, opponents often don't pay, and you draw 3-5 extra cards per turn cycle.
- **Mystic Remora** — Similar to Rhystic Study but for noncreature spells, with a cumulative upkeep.
- **Sylvan Library** — Draw 3, keep what you need (paying 4 life per extra card).
- **Necropotence** — Pay 1 life per card. Extremely powerful but risky.
- **Smothering Tithe** — Creates a treasure token whenever an opponent draws unless they pay {2}. Generates enormous mana advantage.

Cards that generate incremental advantage every turn cycle are much more valuable in Commander than one-shot effects.

## Tempo vs. Value

In competitive 1v1 Magic, **tempo** (spending mana efficiently to develop your board faster than your opponent) is critical. In Commander, **value** (generating more resources over time) is generally more important because:

1. The game lasts longer (40 life, 4 players)
2. You must answer 3 opponents, not just 1
3. Aggressive strategies that work in 1v1 are diluted by multiplayer

However, tempo still matters in cEDH, where fast combo wins are common and games can end by turn 3-4. The tension between tempo and value is reflected in EDHREC rankings: efficient, low-cost staples that provide incremental value rank highest.

## Card Evaluation Frameworks

### BREAD (for Limited/Draft, applicable to Commander)

- **B — Bombs**: Cards that win the game if unanswered. In Commander: Craterhoof Behemoth, Expropriate, Torment of Hailfire.
- **R — Removal**: Cards that answer threats. Swords to Plowshares, Cyclonic Rift, Beast Within, Chaos Warp.
- **E — Evasion**: Creatures that can get damage through. Flying, trample, unblockable, menace.
- **A — Aggro**: Efficient threats that pressure life totals. Less impactful in Commander than in 1v1.
- **D — Duds**: Cards that don't affect the board meaningfully. Avoid these.

### Quadrant Theory

Evaluate cards based on how they perform in four game states:

1. **Developing** (early game, building mana and board): Mana rocks, ramp spells, and cheap creatures excel. This is why Sol Ring and Arcane Signet are so popular.
2. **Parity** (board stall, no one is ahead): Cards that generate incremental advantage shine — Rhystic Study, Phyrexian Arena, Smothering Tithe.
3. **Winning** (you're ahead): Cards that close the game. Craterhoof Behemoth, Triumph of the Hordes, Torment of Hailfire.
4. **Losing** (you're behind): Board wipes (Wrath of God, Cyclonic Rift), removal, and comeback mechanics.

Cards that perform well in multiple quadrants are the most valuable and tend to have the best EDHREC rankings. Sol Ring is excellent in all four quadrants: it accelerates in developing, provides advantage in parity, speeds up your winning turn, and helps you recover when losing.

## Why Low-Cost Staples Dominate EDHREC

The top of the EDHREC rankings is dominated by cheap, efficient, universally useful cards. This pattern emerges from several converging factors:

1. **Colorless cards fit in every deck** — Sol Ring, Command Tower, and Arcane Signet have the widest possible audience.
2. **Low CMC means early deployment** — Cards you can play on turns 1-3 are relevant in every game.
3. **Mana efficiency** — A 1-mana card that does something useful is almost always worth including.
4. **Commander tax** — As your commander gets more expensive to recast, having cheap support cards becomes more important.
5. **Consistency** — In a 99-card singleton deck, redundancy in your mana base and ramp is essential.

This explains why the average EDHREC rank is much better (lower) for cards with CMC 0-3 than for cards with CMC 6+, even though expensive cards may be more individually powerful.

## CMC Distribution in the Dataset

The MTG cards dataset shows a characteristic right-skewed CMC distribution:

| CMC Range | Approximate % of Cards | Avg EDHREC Rank |
|-----------|----------------------|-----------------|
| 0         | ~5% | ~4,000 (best average — includes Sol Ring, Mana Crypt, lands) |
| 1         | ~12% | ~6,500 |
| 2         | ~16% | ~7,000 |
| 3         | ~17% | ~8,000 |
| 4         | ~15% | ~9,000 |
| 5         | ~12% | ~10,000 |
| 6         | ~8% | ~11,000 |
| 7+        | ~15% | ~13,000 (worst average — expensive, niche cards) |

The negative correlation between CMC and EDHREC rank (lower CMC correlates with better rank) is one of the strongest feature-target relationships in the dataset.

## Oracle Text Length as a Feature

The `oracle_text_length` feature measures the character count of a card's rules text. This is a proxy for complexity:
- **Short oracle text (0-50 chars)**: Simple, often efficient effects. Lands have 0 oracle text. Llanowar Elves has ~30 characters.
- **Medium oracle text (50-150 chars)**: Standard effects, one or two abilities. Most removal spells, creatures with a keyword and one ability.
- **Long oracle text (150-300 chars)**: Complex cards with multiple abilities or detailed conditions. Planeswalkers, modal spells.
- **Very long oracle text (300+ chars)**: Highly complex cards, often mythic rares or specialized mechanics.

In general, cards with moderate oracle text (100-200 characters) tend to have the best EDHREC ranks, because they are powerful enough to be interesting but not so complex as to be niche. Very short oracle text (basic creatures with no abilities) tends to correlate with unplayable cards, while very long oracle text may indicate niche combo pieces.

## Keywords as Predictive Features

The `keywords` column in the dataset contains comma-separated keyword abilities (e.g., "Flying,Trample"). The most common keywords in Commander-relevant cards are:

1. **Flying** (~15% of creatures) — Evasion, relevant across all power levels
2. **Trample** (~8% of creatures) — Pushes damage through, important for green strategies
3. **Haste** (~6% of creatures) — Immediate impact, critical for aggressive strategies
4. **Flash** (~4% of cards) — Allows instant-speed deployment, highly valued in Commander
5. **Deathtouch** (~5% of creatures) — Efficient removal through combat
6. **Vigilance** (~4% of creatures) — Attack without tapping
7. **Lifelink** (~4% of creatures) — Life gain through combat

Cards with multiple keywords (e.g., "Flying, Vigilance, Lifelink" on Baneslayer Angel) tend to be more powerful and popular. The keyword count itself is a useful derived feature, as is one-hot encoding the most common individual keywords.
