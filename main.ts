let pick_ramdom = 0
input.onButtonPressed(Button.A, function () {
    pick_ramdom = randint(0, 1)
    basic.showNumber(pick_ramdom)
    if (pick_ramdom == 1) {
        basic.showString("ON")
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showString("OFF")
        basic.showIcon(IconNames.No)
    }
})
