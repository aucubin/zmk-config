# zmk-config

ZMK config for the swweeep (36 keys, split) and the zilpzalp (28 keys).

| Keyboard | Keymap | Firmware artifact |
|---|---|---|
| swweeep, Colemak-DH | `config/swweeep_colemak.keymap` | `swweeep_left-colemak-dh` |
| swweeep, Aptmak | `config/swweeep_aptmak.keymap` | `swweeep_left-aptmak` |
| swweeep, right half | (keymap lives on the left half) | `swweeep_right-nice_nano_v2-zmk` |
| zilpzalp, Aptmak | `config/zilpzalp.keymap` | `zilpzalp-seeeduino_xiao_rp2040-zmk` |

The swweeep left half is the central and holds the keymap, so switching the
swweeep layout only means flashing the other left-half firmware. Each build
selects its keymap via `-DKEYMAP_FILE` in `build.yaml`.

The two swweeep keymaps only differ in the base layer. Everything else lives in
`config/swweeep_common.dtsi` (behaviors, combos, macros) and
`config/swweeep_layers.dtsi` (all other layers).

After editing a keymap, `python3 scripts/align_keymap.py <files>` re-aligns the
binding columns.

All keymaps assume US International with dead keys on both Mac and Linux
(Linux runs Toshy), so each has a single base layer.

**Legend:** `X/▸L` tap X, hold layer L · `⌃ ⌥ ⌘ ⇧` home row mod on hold
(Ctrl, Alt, GUI, Shift) · `⌥r` right Alt · `·` nothing · `boot` bootloader ·
`rst` reset · `,;` `.:` comma/dot that give `;`/`:` with Shift.

## swweeep

Thumbs, layers and combos follow the zilpzalp, the extra keys are filled in.

```
Base — Colemak-DH
Q    W    F    P    B    | J    L    U    Y    ;
A⌃   R⌥   S⌘   T⇧   G⌥r  | M⌥r  N⇧   E⌘   I⌥   O⌃
Z    X    C    D    V    | K    H    ,;   .:   /
  ESC/▸BT  '/▸NUM  SPC/▸NAV | BSPC/▸SYM  ENT/▸FUN  TAB
```

```
Base — Aptmak
V    W    F    P    B    | J    L    U    Y    ;
R⌃   S⌥   T⌘   H⇧   K⌥r  | X⌥r  N⇧   A⌘   I⌥   O⌃
Z    C    G    D    Q    | '    M    ,;   .:   /
  ESC/▸BT  '/▸NUM  SPC/▸NAV | E/▸SYM  ENT/▸FUN  TAB
```

The layers below are the same for both.

```
NUM (left thumb)
·    9    8    7    *    | +    7    8    9    ·
0⌃   6⌥   5⌘   4⇧   /    | -    4    5    6    .
·    3    2    1    ·    | ·    1    2    3    ·
                         | E    0
```

```
NAV (left thumb)
·    INS  ↑    BSPC VOL- | VOL+ BSPC DEL  INS  ·
⌃    ←⌥   ↓⌘   →⇧   MUTE | ←    ↓    ↑    →    TAB
·    HOME PGDN END  ·    | ·    HOME PGUP END  ·
```

```
SYM (right thumb)
·    `    "    °    {    | }    \    |    <    ·
!    @    #    $    (    | )    &    *    %    ^
·    ~    '    _    ·    | ·    -    +    =    ·
          [    ]         |
```
`°` is AltGr+Shift+; (US International).

```
FUN (right thumb)
·    ·    ·    ·    ·    | F12  F7   F8   F9   rst
·    ·    ·    ·    ·    | F11  F4   F5   F6   F10
·    ·    ·    ·    ·    | ·    F1   F2   F3   boot
```

```
BT (left thumb)
CLR  boot ·    BT4  BT2  | ·    ·    ·    ·    ·
NXT  rst  ·    BT3  BT1  | ·    ·    ·    ·    ·
PRV  ·    ·    ·    BT0  | ·    ·    ·    ·    ·
```
`BTn` selects Bluetooth profile n. Each half's bootloader/reset sits on a layer
held by that half's thumb.

**Combos** (same physical keys as on the zilpzalp)

| Combo | Aptmak keys | Colemak-DH keys |
|---|---|---|
| V | W+F | W+F |
| Q | F+P | F+P |
| Z | C+G | X+C |
| ESC | G+D | C+D |
| `-` | M+, | H+, |
| `/` | ,+. | ,+. |
| `{` `[` `(` `<` | W+S, F+T, P+H, B+K | W+R, F+S, P+T, B+G |
| `>` `)` `]` `}` | J+X, L+N, U+A, Y+I | J+M, L+N, U+E, Y+I |
| Caps word | H+N | T+N |
| Caps lock | W+Y | W+Y |
| Backspace | L+U | L+U |
| Delete | U+Y | U+Y |
| Delete word (Ctrl+BSPC) | L+Y | L+Y |
| ä / ö / ü (`"` then the letter) | A+E, O+E, U+E | E+BSPC, O+BSPC, U+BSPC |
| ß (AltGr+S) | S+Space | R+Space |

## zilpzalp — Aptmak

```
Base
     W    F    P    B    | J    L    U    Y
R⌃   S⌥   T⌘   H⇧   K⌥r  | X⌥r  N⇧   A⌘   I⌥   O⌃
     C    G    D         |      M    ,;   .:
          '/▸NUM  SPC/▸NAV | E/▸SYM  ENT/▸FUN
```

```
NUM (left thumb)
     9    8    7    *    | +    7    8    9
0⌃   6⌥   5⌘   4⇧   /    | -    4    5    6    .
     3    2    1         |      1    2    3
                         | E    0
```

```
NAV (left thumb)
     INS  ↑    BSPC VOL- | VOL+ BSPC DEL  INS
⌃    ←⌥   ↓⌘   →⇧   MUTE | ←    ↓    ↑    →    TAB
     HOME PGDN END       |      HOME PGUP END
```

```
SYM (right thumb)
     `    "    °    {    | }    \    |    <
!    @    #    $    (    | )    &    *    %    ^
     ~    '    _         |      -    +    =
          [    ]         |
```

```
FUN (right thumb)
     ·    ·    ·    ·    | F12  F7   F8   F9
boot ·    ·    ·    ·    | F11  F4   F5   F6   F10
     ·    ·    ·         |      F1   F2   F3
```

**Combos**

| Combo | Keys |
|---|---|
| V | W+F |
| Q | F+P |
| Z | C+G |
| ESC | G+D |
| `-` | M+, |
| `/` | ,+. |
| `{` `[` `(` `<` | W+S, F+T, P+H, B+K |
| `>` `)` `]` `}` | J+X, L+N, U+A, Y+I |
| Caps word | H+N |
| Caps lock | W+Y |
| Backspace | L+U |
| Delete | U+Y |
| Delete word (Ctrl+BSPC) | L+Y |
| ä / ö / ü | A+E, O+E, U+E (`"` then the letter) |
| ß (AltGr+S) | S+Space |
