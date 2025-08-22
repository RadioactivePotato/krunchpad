import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.LED import LED

keyboard = KMKKeyboard()

# matrix
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.TAB, KC.Q, KC.W, KC.E,
        KC.LSHIFT, KC.A, KC.S, KC.D,
        KC.LCTRL, KC.F3, KC.F5, KC.SPACE,
    ]
]

# volume knob
encoder = EncoderHandler()
encoder.pins = ((board.D7, board.D6),)
encoder.map = [((KC.VOLU, KC.VOLD))]  # cw = vol up, ccw = vol down
keyboard.modules.append(encoder)

# 128x32 OLED display

keyboard.SCL = board.D5
keyboard.SDA = board.D4

display = Display(
    display=SSD1306(sda=board.D4, scl=board.D5),
    entries=[
        TextEntry(text="""
hello
world
        """),
    ],
    height=32,
)
keyboard.extensions.append(display)

# MCU neopixel

mcuneopixel = RGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=1,
    val_limit=100,
    val_default=25,
    animation_mode=AnimationModes.RAINBOW,
)
keyboard.extensions.append(mcuneopixel)

if __name__ == '__main__':
    keyboard.go()
