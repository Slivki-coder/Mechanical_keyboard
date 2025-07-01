from kmk.kmk_keyboard import KMKKeyboard # type: ignore
from kmk.keys import KC                  # type: ignore
from kmk.scanners import DiodeOrientation# type: ignore
from kmk.key import Key                  # type: ignore
import board                             # type: ignore

from kmk.modules.layers import Layers    # type: ignore

keyboard = KMKKeyboard()

# Add layer support
keyboard.modules.append(Layers())

# Define matrix row and column pins
keyboard.row_pins = (board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26)
keyboard.col_pins = (board.GP17, board.GP16, board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2, board.GP1, board.GP0)

# Specify diode direction (most keyboards are COL2ROW)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

def macro_1(key, keyboard, *args):
    return False
def macro_2(key, keyboard, *args):
    return False
def macro_3(key, keyboard, *args):
    return False
def macro_4(key, keyboard, *args):
    return False
def macro_5(key, keyboard, *args):
    return False

KC_M1 = Key(macro_1)
KC_M2 = Key(macro_2)
KC_M3 = Key(macro_3)
KC_M4 = Key(macro_4)
KC_M5 = Key(macro_5)


# Define keymap layout (4 rows x 3 columns in this example)
keyboard.keymap = [
    [
        KC.NO, KC.ESC,   KC.NO,   KC.F1,   KC.F2, KC.F3, KC.F4,    KC.NO, KC.F5, KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F12,  KC.PRNT, KC.SLCK, KC.PAUS,
        KC_M1, KC.GRAVE, KC._1,   KC._2,   KC._3, KC._4, KC._5,    KC._6, KC._7, KC._8,   KC._9,   KC._0,   KC.MINS, KC.F11,  KC.BSPC, KC.INS,  KC.HOME, KC.PGUP,
        KC_M2, KC.TAB,   KC.Q,    KC.W,    KC.E,  KC.R,  KC.T,     KC.Y,  KC.U,  KC.I,    KC.O,    KC.P,    KC.LBRC, KC.EQL,  KC.BSLS, KC.DEL,  KC.END,  KC.PGDN,
        KC_M3, KC.CAPS,  KC.A,    KC.S,    KC.D,  KC.F,  KC.G,     KC.H,  KC.J,  KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.RBRC, KC.ENT,  KC.NO,   KC.NO,   KC.NO,
        KC_M4, KC.LSFT,  KC.Z,    KC.X,    KC.C,  KC.V,  KC.B,     KC.N,  KC.M,  KC.COMM, KC.DOT,  KC.SLSH, KC.NO,   KC.NO,   KC.RSFT, KC.NO,   KC.UP,   KC.NO,
        KC_M5, KC.LCTL,  KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.NO,   KC.RALT, KC.RGUI, KC.NO,   KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT


    ]
]

if __name__ == '__main__':
    keyboard.go()
