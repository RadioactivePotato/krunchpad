import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.oled import OLED

keyboard = KMKKeyboard()

# matrix
keyboard.row_pins = (board.GP3, board.GP4, board.GP2)
keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
keyboard.diode_orientation = MatrixScanner.DIODE_COL2ROW

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C, KC.D,
        KC.E, KC.F, KC.G, KC.H,
        KC.I, KC.J, KC.K, KC.L,
    ]
]

# volume knob
encoder = EncoderHandler()
encoder.pins = ((board.GP1, board.GP0),)
encoder.map = [((KC.VOLU, KC.VOLD))]  # cw = vol up, ccw = vol down
keyboard.modules.append(encoder)

display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Hello World', x=0, y=0, y_anchor='M'),
    ],
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

keyboard.modules.append(display)

if __name__ == '__main__':
    keyboard.go()
