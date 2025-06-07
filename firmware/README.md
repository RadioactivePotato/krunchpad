### Features

#### 3×4 Key Matrix

* 12 customizable keys in 3 rows and 4 columns.
* Default keymap sends letters A–L.

#### Rotary Encoder

* EC11 rotary encoder connected to GPIO0 and GPIO1.
* Turns:

  * Clockwise > Volume Up
  * Counterclockwise > Volume Down

#### OLED Display

* Displays `"Hello World"` centered vertically on boot.
* OLED dims after 10 seconds of inactivity, turns off after 20 minutes (1200 seconds).

---

### Pins

| Function       | GPIO Pins                                    |
| -------------- | -------------------------------------------- |
| Matrix Rows    | GP3, GP4, GP2                                |
| Matrix Columns | GP26, GP27, GP28, GP29                       |
| Encoder A/B    | GP1, GP0                                     |