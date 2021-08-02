input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    radio.sendValue("ROCK", 1)
    Output = 1
    control.waitMicros(100000)
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    radio.sendValue("SCISSORS", 3)
    Output = 3
    control.waitMicros(100000)
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    radio.sendValue("PAPER", 2)
    Output = 2
    control.waitMicros(100000)
})
input.onGesture(Gesture.Shake, function () {
    Output = 0
    OpponentInput = 0
    basic.showLeds(`
        . . . . #
        . . . # .
        # . # . .
        . # . . .
        . . . . .
        `)
})
radio.onReceivedValue(function (name, value) {
    OpponentInput = value
})
let Output = 0
let OpponentInput = 0
OpponentInput = 0
Output = 0
radio.setGroup(4)
basic.forever(function () {
    if (Output == 1 && OpponentInput == 1) {
        basic.showString("TIED")
    }
    if (Output == 1 && OpponentInput == 2) {
        basic.showString("LOSE")
    }
    if (Output == 1 && OpponentInput == 3) {
        basic.showString("WIN")
    }
    if (Output == 2 && OpponentInput == 1) {
        basic.showString("WIN")
    }
    if (Output == 2 && OpponentInput == 2) {
        basic.showString("TIED")
    }
    if (Output == 2 && OpponentInput == 3) {
        basic.showString("WIN!")
    }
    if (Output == 3 && OpponentInput == 1) {
        basic.showString("LOSE")
    }
    if (Output == 3 && OpponentInput == 2) {
        basic.showString("WIN")
    }
    if (Output == 3 && OpponentInput == 3) {
        basic.showString("TIED")
    }
})
