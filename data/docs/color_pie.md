# The Color Pie: Magic's Core Design Philosophy

## Overview

Magic: The Gathering uses five colors of mana — White (W), Blue (U), Black (B), Red (R), and Green (G) — collectively called **WUBRG** (pronounced "woo-berg"). Each color represents a philosophy, a set of mechanical strengths, and a set of weaknesses. The color pie is the foundational design tool that gives Magic its strategic depth: no single color can do everything, so players must choose which strengths to prioritize and which weaknesses to accept.

Colors are arranged in a pentagon: W-U-B-R-G. Adjacent colors (allied pairs) share philosophies and cooperate naturally. Opposite colors (enemy pairs) have fundamentally different values and create tension.

## The Five Colors

### White (W) — Order, Community, Protection

White believes in the greater good, rules, and structure. Mechanically, white excels at:
- **Tokens and go-wide strategies** — cards like Raise the Alarm, Increasing Devotion, and Martial Coup create many small creatures
- **Lifegain** — Soul Warden, Heliod Sun-Crowned, and Aetherflux Reservoir
- **Board wipes** — Wrath of God (4 mana, destroy all creatures), Day of Judgment, Austere Command, and Farewell are white's signature mass removal
- **Removal** — Swords to Plowshares (1 mana, exile a creature) is the most efficient single-target removal in Magic
- **Protection and taxation** — Smothering Tithe generates treasure tokens when opponents draw cards; Ghostly Prison taxes attackers
- **Weakness** — White struggles with card draw and ramp, making it traditionally the weakest mono-color in Commander

### Blue (U) — Knowledge, Control, Manipulation

Blue values intellect, information, and careful planning. Mechanically:
- **Card draw** — Rhystic Study (draws a card whenever an opponent casts a spell without paying {1}) is the most-played blue enchantment in Commander. Brainstorm, Ponder, and Preordain filter draws.
- **Counterspells** — Counterspell (2 mana, counter target spell), Mana Drain (counters and gives you mana), Force of Will (free counter by exiling a blue card), Swan Song, Negate
- **Bounce** — Cyclonic Rift (2 mana to bounce one permanent, or 7 mana to bounce all opponents' nonland permanents) is one of the most powerful cards in Commander
- **Copy effects** — Clone, Clever Impersonator, Sakashima of a Thousand Faces
- **Weakness** — Blue has very limited permanent removal (it can counter threats before they resolve but struggles to remove them once on the battlefield)

### Black (B) — Ambition, Death, Power at Any Cost

Black believes power is there for the taking, regardless of the price. Mechanically:
- **Removal** — Doom Blade, Go for the Throat, Toxic Deluge (pay life to give all creatures -X/-X), Damnation (black Wrath of God)
- **Discard** — Thoughtseize, Hymn to Tourach (less effective in multiplayer since it only hits one opponent)
- **Reanimation** — Reanimate, Animate Dead, Living Death bring creatures from graveyards to the battlefield; Sheoldred, Whispering One reanimates every turn
- **Paying life as a resource** — Necropotence (pay 1 life to draw a card), Bolas's Citadel (play cards from your library by paying life), Phyrexian Arena
- **Tutors** — Demonic Tutor, Vampiric Tutor, and Diabolic Intent search your library for any card, providing unmatched consistency
- **Weakness** — Black cannot destroy artifacts or enchantments, making it vulnerable to those permanent types

### Red (R) — Chaos, Freedom, Emotion

Red acts on impulse, values freedom, and prefers action over planning. Mechanically:
- **Direct damage** — Lightning Bolt (3 damage for 1 mana), Blasphemous Act (13 damage to all creatures, often costs just 1 mana), Comet Storm
- **Haste** — Red creatures frequently have haste, attacking the turn they enter; Fervor and Fires of Yavimaya grant haste to all your creatures
- **Temporary effects** — "Impulse draw" (exile the top card, play it this turn), Threaten effects (steal a creature for one turn)
- **Artifact interaction** — Vandalblast, Shattering Spree, Dockside Extortionist (creates treasure tokens equal to opponents' artifacts and enchantments — one of the most powerful Commander cards ever printed)
- **Weakness** — Red has limited card advantage and almost no enchantment removal. Red also struggles in long, grindy games typical of Commander.

### Green (G) — Nature, Growth, Strength

Green trusts in the natural order — the strongest survive. Mechanically:
- **Mana ramp** — Cultivate, Kodama's Reach, Sakura-Tribe Elder, Llanowar Elves, Birds of Paradise. Green is the best color at accelerating mana, which is critical in Commander where spells are expensive.
- **Big creatures** — Craterhoof Behemoth (a 5/5 that gives all your creatures +X/+X and trample), Old Gnawbone, Vorinclex
- **Naturalize effects** — Beast Within (destroy any permanent), Nature's Claim, Krosan Grip destroy artifacts and enchantments
- **Card draw tied to creatures** — Beast Whisperer, Guardian Project, The Great Henge draw cards when creatures enter
- **Weakness** — Green has very limited interaction with the stack (no counterspells) and poor single-target creature removal

## Color Pairs (Guilds)

Each two-color combination is named after a Ravnican guild and has a distinct mechanical identity:

### Allied Pairs (adjacent on the color wheel)
- **Azorius (WU)** — Control, law. Flickers, detain, counterspells + board wipes. Example: Brago, King Eternal.
- **Dimir (UB)** — Stealth, manipulation. Mill, surveil, reanimation + card draw. Example: The Scarab God.
- **Rakdos (BR)** — Destruction, madness. Sacrifice, discard synergies, aggressive damage. Example: Kroxa, Titan of Death's Hunger.
- **Gruul (RG)** — Savagery, nature. Big creatures, lands matter, combat tricks. Example: Xenagos, God of Revels.
- **Selesnya (GW)** — Harmony, community. Tokens, lifegain, enchantments matter. Example: Trostani, Selesnya's Voice.

### Enemy Pairs (opposite on the color wheel)
- **Orzhov (WB)** — Religion, taxation. Lifedrain, aristocrats (sacrifice synergies), extort. Example: Teysa Karlov.
- **Izzet (UR)** — Science, experimentation. Spellslinger, copy effects, storm. Example: Niv-Mizzet, Parun.
- **Golgari (BG)** — Death and rebirth. Graveyard recursion, -1/-1 counters, dredge. Example: Meren of Clan Nel Toth.
- **Boros (RW)** — Military, justice. Aggressive combat, equipment, mentor. Example: Winota, Joiner of Forces.
- **Simic (UG)** — Evolution, adaptation. +1/+1 counters, card draw + ramp, flash creatures. Example: Kinnan, Bonder Prodigy.

## Three-Color Combinations

### Shards (a color and its two allies, from Alara block)
- **Bant (WUG)** — Exalted, value, enchantments
- **Esper (WUB)** — Artifacts, control, sphinxes
- **Grixis (UBR)** — Graveyard, spellslinger, demons
- **Jund (BRG)** — Sacrifice, value, dragons
- **Naya (RGW)** — Big creatures, tokens, combat

### Wedges (a color and its two enemies, from Khans of Tarkir)
- **Abzan (WBG)** — +1/+1 counters, graveyard, outlast
- **Jeskai (URW)** — Spells matter, prowess, monks
- **Sultai (UBG)** — Graveyard, delve, value engines
- **Mardu (RWB)** — Aggressive, warriors, raid
- **Temur (GUR)** — Big spells, creatures with power 4+, ferocious

## Four and Five Colors

Four-color commanders are rare (only the 2016 Commander set and a few others). Five-color commanders like **Kenrith, the Returned King**, **Jodah, the Unifier**, and **The Ur-Dragon** can play any card in Magic, making them extremely flexible but harder to build a focused mana base for.

## Colorless

Colorless cards have no color identity restrictions — they can go in any Commander deck. This universality is why colorless staples like Sol Ring, Arcane Signet, and Command Tower dominate the top of the EDHREC rankings. Colorless commanders like Kozilek, the Great Distortion are built around Wastes (colorless basic lands) and colorless-producing lands.

## Color Identity in the Dataset

In the MTG cards dataset, `color_identity` is stored as a comma-separated string of color letters. Examples:
- `""` (empty) — Colorless cards like Sol Ring, Mana Crypt
- `"W"` — Mono-white cards like Swords to Plowshares
- `"U,B"` — Dimir cards like The Scarab God
- `"W,U,B,R,G"` — Five-color cards like Kenrith, the Returned King

The `num_colors` derived feature counts the number of colors (0 for colorless, 1-5 for colored cards). This is a useful predictor because:
- **0 colors (colorless)**: Widest possible audience, generally best EDHREC ranks
- **1 color (mono)**: Can go in any deck containing that color (~60-70% of decks include any given color)
- **2 colors**: Narrower audience, but still significant
- **3+ colors**: Most restricted, smallest potential player base

## Color Popularity Statistics

Based on EDHREC data, the most popular colors in Commander are:
- **Green** — Appears in ~55% of all Commander decks (ramp is universally needed)
- **Blue** — Appears in ~50% (card draw and counterspells are premium)
- **Black** — Appears in ~48% (tutors and removal are essential)
- **White** — Appears in ~45% (board wipes and efficient removal)
- **Red** — Appears in ~40% (the least represented color, as its strengths — direct damage, haste — are less impactful in multiplayer)

The most popular color combinations for commanders are:
1. **Simic (UG)** — Green ramp + blue card draw
2. **Sultai (UBG)** — Value, graveyard, the "good stuff" wedge
3. **Golgari (BG)** — Graveyard synergies
4. **Esper (WUB)** — Control, artifacts
5. **Temur (GUR)** — Big spells, creature-based value

## Impact on EDHREC Popularity

A card's color identity directly affects its potential player base. A mono-blue card can only go in decks that include blue, while a colorless card can go in every deck. This is a major reason why colorless utility cards and lands consistently have the lowest (best) EDHREC ranks. Similarly, cards with fewer colors in their identity have a wider potential audience than those with more restrictive color requirements.

When building a prediction model, color identity is one of the most important features. The encoding strategy matters — one-hot encoding each of the 5 colors (W, U, B, R, G) as binary features is more informative than simply using `num_colors`, because it captures which specific colors a card belongs to. Some colors (green, blue) are more popular in Commander than others (red), so a green card has a larger potential audience than a red card even though both are mono-colored.
