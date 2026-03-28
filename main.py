pick_ramdom = 0

def on_button_pressed_a():
    global pick_ramdom
    pick_ramdom = randint(0, 1)
    basic.show_number(pick_ramdom)
    if pick_ramdom == 1:
        basic.show_string("ON")
        basic.show_icon(IconNames.YES)
    else:
        basic.show_string("OFF")
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)
