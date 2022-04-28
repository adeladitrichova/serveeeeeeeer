#server
radio.set_group(28)

receiving = True
answers = []

def on_received_string(string):
    if receiving == True
        serialsus = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        answers.append({"serials":(serialsus), "vote":(answer)})

def on_button_pressed_a():
    global receiving
    if receiving == True:
        receiving = False
    else:
        receiving = True

def results():
    options = []
    for i in answers:
        if i not in options:
            options.append(i)
    for i in options:



input.on_button_pressed(Button.A, on_button_pressed_a)
radio.on_received_string(on_received_string)