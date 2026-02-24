# Card Types and Strategy in Commander

## Overview of Card Types

Every Magic: The Gathering card has a **type line** that determines its fundamental game behavior. The type line appears in the middle of the card and follows the format: `[Supertypes] [Card Type] — [Subtypes]`. For example, "Legendary Creature — Elf Druid" has the supertype "Legendary," the card type "Creature," and the subtypes "Elf" and "Druid."

Understanding card types is essential for predicting EDHREC popularity because different types serve different roles in Commander, and certain types (like artifacts and lands) have inherent advantages due to color identity flexibility.

## Creatures

Creatures are the most common card type in Magic. They have **power** (attack strength) and **toughness** (defense), printed as P/T in the bottom-right corner (e.g., 4/4). Creatures can attack opponents and block attackers.

### Power and Toughness

- **Numeric values**: Most creatures have fixed P/T (e.g., Llanowar Elves is 1/1, Craterhoof Behemoth is 5/5)
- **Variable values ("*")**: Some creatures have * for power, toughness, or both, meaning the value is defined by an ability. For example, Tarmogoyf has */1+* (power equals card types in all graveyards). In the dataset, approximately 3-4% of creatures have "*" in their power or toughness fields.
- **Non-creature cards**: Instants, sorceries, enchantments (without creature subtype), artifacts (without creature subtype), planeswalkers, and lands have **no power/toughness** — these fields are null. This accounts for ~46% of the dataset.

### Evasion Keywords

Keywords on creatures determine how they interact with combat:
- **Flying** — Can only be blocked by creatures with flying or reach. One of the most common evasion keywords, appearing on ~15% of creatures in the dataset.
- **Trample** — Excess combat damage carries over to the defending player. Critical for Voltron commanders and big green creatures.
- **Haste** — Can attack and use tap abilities the turn it enters. Red's signature keyword. Lightning Greaves and Swiftfoot Boots grant haste.
- **First Strike / Double Strike** — Deals damage before normal combat (double strike deals damage in both steps). Makes creatures much more effective in combat.
- **Deathtouch** — Any damage this creature deals to another creature is enough to destroy it. Makes even 1/1 creatures deadly blockers.
- **Hexproof** — Cannot be targeted by opponents' spells or abilities. Extremely powerful for protecting key creatures.
- **Vigilance** — Doesn't tap when attacking, so it can also block. Common in white.
- **Lifelink** — Damage dealt by this creature also gains you that much life.
- **Menace** — Can only be blocked by two or more creatures. Common in black and red.

### Tribal Synergies

Many Commander decks are built around a creature type (tribe), using cards that reward having many creatures of the same type:

- **Elves** — Mana generation and going wide. Llanowar Elves, Elvish Archdruid, Priest of Titania. Commanders: Lathril, Blade of the Elves; Ezuri, Renegade Leader.
- **Goblins** — Aggressive, sacrifice synergies. Goblin Warchief, Krenko, Mob Boss, Skirk Prospector.
- **Dragons** — Expensive but powerful flyers. The Ur-Dragon, Lathliss, Dragon Queen, Terror of the Peaks.
- **Zombies** — Graveyard recursion, sacrifice outlets. Gravecrawler, Undead Augur, Wilhelt, the Rotcleaver.
- **Humans** — The largest tribe in Magic. Thalia's Lieutenant, Champion of the Parish, Winota, Joiner of Forces.

## Instants and Sorceries

Instants and sorceries are one-time effects that go to the graveyard after resolving. The key difference: **instants** can be cast at any time (including during opponents' turns), while **sorceries** can only be cast during your main phase.

### Key Categories

- **Removal**: Destroying, exiling, or otherwise dealing with threats
  - Swords to Plowshares (W, instant) — Exile target creature, they gain life. The gold standard of removal.
  - Path to Exile (W, instant) — Exile target creature, they search for a basic land.
  - Counterspell (UU, instant) — Counter target spell. The classic.
  - Cyclonic Rift (1U, instant) — Bounce one permanent, or overload for 7 mana to bounce all opponents' nonland permanents. One of the most powerful and controversial cards in Commander.
  - Chaos Warp (2R, instant) — Shuffle target permanent into its owner's library. Red's only answer to enchantments.
  - Beast Within (2G, instant) — Destroy target permanent, they get a 3/3 beast. Green's most versatile removal.

- **Board Wipes**: Mass removal that resets the battlefield
  - Wrath of God (2WW, sorcery) — Destroy all creatures. The original board wipe.
  - Damnation (2BB, sorcery) — Black version of Wrath of God.
  - Blasphemous Act (8R, sorcery) — 13 damage to all creatures. Costs 1 mana when enough creatures are in play.
  - Farewell (4WW, sorcery) — Choose any combination: exile all artifacts, creatures, enchantments, and/or graveyards.
  - Toxic Deluge (2B, sorcery) — Pay life to give all creatures -X/-X. Bypasses indestructible.

- **Tutors**: Search your library for specific cards
  - Demonic Tutor (1B, sorcery) — Search for any card. The most efficient tutor.
  - Vampiric Tutor (B, instant) — Search for any card, put it on top of your library.
  - Enlightened Tutor (W, instant) — Search for an artifact or enchantment.

## Enchantments

Enchantments are permanent cards that remain on the battlefield and provide ongoing effects. They are among the hardest permanent types to remove (fewer cards destroy enchantments compared to creatures or artifacts).

### Commander Staple Enchantments

- **Rhystic Study** (2U) — Draws a card whenever an opponent casts a spell unless they pay {1}. One of the most powerful card advantage engines in Commander. EDHREC rank consistently in the top 20.
- **Smothering Tithe** (3W) — Creates a treasure token whenever an opponent draws a card unless they pay {2}. Generates enormous mana advantage in multiplayer.
- **Mystic Remora** (U) — Draws cards when opponents cast noncreature spells. Cumulative upkeep makes it temporary.
- **Phyrexian Arena** (1BB) — Draw an extra card each upkeep, lose 1 life. Steady, reliable card advantage.
- **Doubling Season** (4G) — Doubles tokens and counters. Enables instant ultimate on planeswalkers.

## Artifacts

Artifacts are colorless permanents (unless they have colored mana in their cost). Because most artifacts have no color identity, they can go in any Commander deck, making them disproportionately popular on EDHREC.

### Mana Rocks

Mana rocks are artifacts that produce mana, forming the backbone of Commander manabases:
- **Sol Ring** (1) — Tap for {C}{C}. EDHREC rank #1. In ~67% of all decks.
- **Arcane Signet** (2) — Tap for one mana of any color in your commander's identity.
- **Signets** (2 each) — Ten two-color mana rocks (Azorius Signet, Dimir Signet, etc.).
- **Talismans** (2 each) — Ten two-color rocks that can also tap for colorless.
- **Mana Crypt** (0) — Free Sol Ring with a coin-flip downside (3 damage 50% of the time).

### Equipment

Equipment attaches to creatures to grant bonuses:
- **Lightning Greaves** (2) — Grants haste and shroud. Protects your commander.
- **Swiftfoot Boots** (2) — Grants haste and hexproof. Allows targeting unlike Greaves.
- **Sword of Feast and Famine** (3) — Protection from black and green, discard + untap lands.
- **Skullclamp** (1) — Equip to a 1-toughness creature, it dies, you draw 2 cards. Banned in other formats for being too powerful.

## Planeswalkers

Planeswalkers enter with loyalty counters and can activate one ability per turn. They are powerful but attract attention in Commander — opponents can attack them with creatures, making them hard to keep alive in a 4-player game. Despite this, planeswalkers with strong enters-the-battlefield abilities or that can protect themselves see play.

Notable Commander planeswalkers: Teferi, Time Raveler (shuts down opponents' instant-speed plays), Narset, Parter of Veils (limits opponents to one draw per turn), Ugin, the Spirit Dragon (board wipe on a stick).

## Lands

Lands produce mana and don't cost mana to play (one per turn normally). The mana base is arguably the most important part of a Commander deck.

### Key Land Categories

- **Command Tower** — Taps for any color in your commander's identity. Auto-include in every multicolor deck.
- **Fetch lands** — Polluted Delta, Flooded Strand, etc. Sacrifice to search for a land with a basic land type. Fix mana and thin the deck. 10 fetch lands, each ~$15-40.
- **Original dual lands** — Underground Sea, Tundra, etc. Count as two basic land types with no drawback. On the Reserved List, extremely expensive ($200-$1000+). Only 10 exist.
- **Shock lands** — Watery Grave, Hallowed Fountain, etc. Dual lands that enter tapped unless you pay 2 life. The most practical dual land fixing ($10-20 each).
- **Utility lands** — Reliquary Tower (no maximum hand size), Rogue's Passage (make a creature unblockable), Bojuka Bog (exile a graveyard), Urza's Saga (fetch small artifacts).

### Why Lands Are Popular on EDHREC

Lands like Command Tower, Exotic Orchard, and Mana Confluence appear near the top of EDHREC rankings because they are colorless (no color identity restriction), every deck needs lands, and good mana fixing is universally valuable. A Commander deck typically runs 35-38 lands plus 10-12 mana rocks.
