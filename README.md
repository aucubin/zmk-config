# zmk-config

ZMK config for the swweeep (36 keys, split) and the zilpzalp (28 keys).

| Keyboard | Keymap | Firmware artifact |
|---|---|---|
| swweeep, Colemak-DH | `config/swweeep.keymap` | `swweeep_left-colemak-dh` |
| swweeep, Aptmak | `config/swweeep_aptmak.keymap` | `swweeep_left-aptmak` |
| swweeep, right half | (keymap lives on the left half) | `swweeep_right-nice_nano_v2-zmk` |
| zilpzalp, Aptmak | `config/zilpzalp.keymap` | `zilpzalp-seeeduino_xiao_rp2040-zmk` |

The swweeep left half is the central and holds the keymap, so switching the
swweeep layout only means flashing the other left-half firmware. The Aptmak
build selects its keymap via `-DKEYMAP_FILE` in `build.yaml`.

After editing a keymap, `python3 scripts/align_keymap.py` re-aligns the binding
columns.

**Legend:** `X/▸L` tap X, hold layer L · `⌃ ⌥ ⌘ ⇧` home row mod on hold
(Ctrl, Alt, GUI, Shift) · `⌥r` right Alt · `·` nothing · `boot` bootloader ·
`rst` reset · `,;` `.:` comma/dot that give `;`/`:` with Shift.

## swweeep — Colemak-DH

```
Base (Mac and Linux identical, Linux only switches the SYM layer)
Q    W    F    P    B    | J    L    U    Y    ;
A⌃   R⌥   S⌘   T⇧   G    | M    N⇧   E⌘   I⌥   O⌃
Z    X    C    D    V    | K    H    ,    .    /
     ESC/▸BT  ▸SYM  TAB  | SPC/▸NAV  BSPC/▸NUM  ENT
```
`BSPC/▸NUM` repeats Backspace on tap, then hold.

```
SYM (left thumb)
boot ·    ·    ·    ·    | ]    }    )    ·    |
`    ~    _    =    ·    | [    {    (    ·    \
rst  ·    +    -    ·    | ¨    ß    :    "    '
```
`¨` and `ß`: Option+U / Option+S on Mac, AltGr+Shift+' / AltGr+S on Linux.

```
NUM (right thumb)
!    @    #    $    %    | ^    &    *    |    ·
1    2    3    4    5    | 6    7    8    9    0
·    ·    ·    ·    ·    | ·    ·    ·    ·    ·
```

```
NAV (right thumb)
·    F1   F4   F7   F10  | boot HOME ↑    END  ·
·    F2   F5   F8   F11  | rst  ←    ↓    →    ·
·    F3   F6   F9   F12  | ·    ·    ·    ·    DEL
```

```
BT (left thumb)
CLR  ·    ·    BT4  lin2 | ·    ·    ·    ·    ·
NXT  ·    ·    BT3  mac1 | ·    ·    ·    ·    ·
PRV  ·    ·    ·    mac0 | ·    ·    ·    ·    ·
```
`macN` / `linN` select Bluetooth profile N and switch to the Mac / Linux base layer.

**Combos**

| Combo | Keys |
|---|---|
| Zoom in (⌘=) | Q+W |
| Zoom out (⌘-) | W+F |
| Caps word | T+N |

## swweeep — Aptmak

Thumbs, layers and combos follow the zilpzalp, the extra keys are filled in.

```
Base (Mac and Linux identical, Linux only switches OS-specific combos)
V    W    F    P    B    | J    L    U    Y    ;
R⌃   S⌥   T⌘   H⇧   K⌥r  | X⌥r  N⇧   A⌘   I⌥   O⌃
Z    C    G    D    Q    | '    M    ,;   .:   /
  ESC/▸BT  '/▸NUM  SPC/▸NAV | E/▸SYM  ENT/▸FUN  TAB
```

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
CLR  boot ·    BT4  lin2 | ·    ·    ·    ·    ·
NXT  rst  ·    BT3  mac1 | ·    ·    ·    ·    ·
PRV  ·    ·    ·    mac0 | ·    ·    ·    ·    ·
```
Each half's bootloader/reset sits on a layer held by that half's thumb.

**Combos** (same letters as on the zilpzalp)

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
| Delete word | L+Y (Option+BSPC on Mac, Ctrl+BSPC on Linux) |
| ä / ö / ü | A+E, O+E, U+E |
| ß | S+Space |

Umlauts and ß use Option+U / Option+S on Mac and AltGr+Shift+' / AltGr+S on Linux.

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
