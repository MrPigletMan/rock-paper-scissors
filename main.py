def on_button_pressed_a():
    global Output
    basic.clear_screen()
    radio.send_value("ROCK", 1)
    Output = 1
    control.wait_micros(100000)
    while OpponentInput != 0:
        if OpponentInput == 1:
            basic.show_string("TIED!")
        if OpponentInput == 2:
            basic.show_string("LOSE")
        if OpponentInput == 3:
            basic.show_string("WIN!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Output
    basic.clear_screen()
    radio.send_value("SCISSORS", 3)
    Output = 3
    control.wait_micros(100000)
    while OpponentInput != 0:
        if OpponentInput == 1:
            basic.show_string("LOSE")
        if OpponentInput == 2:
            basic.show_string("WIN!")
        if OpponentInput == 3:
            basic.show_string("TIED!")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Output
    basic.clear_screen()
    radio.send_value("PAPER", 2)
    Output = 2
    control.wait_micros(100000)
    while OpponentInput != 0:
        if OpponentInput == 1:
            basic.show_string("WIN!")
        if OpponentInput == 2:
            basic.show_string("TIED!")
        if OpponentInput == 3:
            basic.show_string("LOSE")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global Output, OpponentInput
    Output = 0
    OpponentInput = 0
    basic.show_leds("""
        . . . . #
                . . . # .
                # . # . .
                . # . . .
                . . . . .
    """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_received_value(name, value):
    global OpponentInput
    OpponentInput = value
radio.on_received_value(on_received_value)

Output = 0
OpponentInput = 0
OpponentInput = 0
Output = 0
radio.set_group(4)

def on_forever():
    pass
basic.forever(on_forever)
