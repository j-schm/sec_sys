import time
import board
import random
import analogio
from adafruit_circuitplayground import cp

analogin = analogio.AnalogIn(board.A1)

# colors
Red = (255, 0, 0,)
Orange = (255, 125, 0)
Yellow = (125, 125, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)


# def get_voltage(pin):
#     return (pin.value * 3.3) / 65536


def flash_red_yellow():
    time.sleep(0.25)
    cp.pixels.fill(Black)
    cp.pixels[0] = Red
    cp.pixels[2] = Red
    cp.pixels[4] = Red
    cp.pixels[6] = Red
    cp.pixels[8] = Red
    cp.play_tone = (310, 0.35)  # was feeling a little nostalgic :P
    time.sleep(0.25)
    cp.pixels.fill(Black)
    cp.pixels[1] = Yellow
    cp.pixels[3] = Yellow
    cp.pixels[5] = Yellow
    cp.pixels[7] = Yellow
    cp.pixels[9] = Yellow
    cp.play_tone = (252, 0.35)
    time.sleep(0.25)
    cp.pixels.fill(Black)
    cp.pixels[0] = Red
    cp.pixels[2] = Red
    cp.pixels[4] = Red
    cp.pixels[6] = Red
    cp.pixels[8] = Red
    cp.play_tone = (310, 0.35)
    time.sleep(0.25)
    cp.pixels.fill(Black)
    cp.pixels[1] = Yellow
    cp.pixels[3] = Yellow
    cp.pixels[5] = Yellow
    cp.pixels[7] = Yellow
    cp.pixels[9] = Yellow
    cp.play_tone = (252, 0.35)


def flash_blue_green():
    time.sleep(0.25)
    cp.pixels.fill(Black)
    cp.pixels[1] = Green
    cp.pixels[3] = Green
    cp.pixels[5] = Green
    cp.pixels[7] = Green
    cp.pixels[9] = Green
    cp.play_tone = (415, 0.35)
    time.sleep(0.25)
    cp.pixels.fill(Black)
    cp.pixels[0] = Blue
    cp.pixels[2] = Blue
    cp.pixels[4] = Blue
    cp.pixels[6] = Blue
    cp.pixels[8] = Blue
    cp.play_tone = (209, 0.35)
    time.sleep(0.25)
    cp.pixels.fill(Black)
    cp.pixels[1] = Green
    cp.pixels[3] = Green
    cp.pixels[5] = Green
    cp.pixels[7] = Green
    cp.pixels[9] = Green
    cp.play_tone = (415, 0.35)
    time.sleep(0.25)
    cp.pixels.fill(Black)
    cp.pixels[0] = Blue
    cp.pixels[2] = Blue
    cp.pixels[4] = Blue
    cp.pixels[6] = Blue
    cp.pixels[8] = Blue
    cp.play_tone = (209, 0.35)


def flash_rand():
    if random.randint(0, 4) == 0:
        cp.pixels.fill(Red)
        cp.play_tone = (310, 0.35)
        time.sleep(0.5)
        cp.pixels.fill(Black)
    elif random.randint(0, 4) == 1:
        cp.pixels.fill(Orange)
        cp.play_tone = (252, 0.35)
        time.sleep(0.5)
        cp.pixels.fill(Black)
    elif random.randint(0, 4) == 2:
        cp.pixels.fill(Yellow)
        cp.play_tone = (252, 0.35)
        time.sleep(0.5)
        cp.pixels.fill(Black)
    elif random.randint(0, 4) == 3:
        cp.pixels.fill(Green)
        cp.play_tone = (415, 0.35)
        time.sleep(0.5)
        cp.pixels.fill(Black)
    elif random.randint(0, 4) == 4:
        cp.pixels.fill(Blue)
        cp.play_tone = (209, 0.35)
        time.sleep(0.5)
        cp.pixels.fill(Black)


def emergency_disco():
    for i in range(3):  # should loop through sequence five times
        cp.pixels.fill(Red)
        cp.play_tone = (310, 0.35)
        time.sleep(0.5)
        cp.pixels.fill(Black)
        time.sleep(0.5)
    for i in range(5):
        for j in range(2):  # flash red and yellow
            flash_red_yellow()
        for k in range(2):  # flash green and blue
            flash_blue_green()
        for l in range(5):
            flash_rand()


def set_password():
    # use code from making sequencer
    light_num = 1
    sequence = ["", "", "", ""]
    while True:
        if cp.switch:
            if cp.button_b and light_num < 4:
                cp.pixels.fill(0)
                light_num += 1
                time.sleep(0.3)
            if cp.button_a and light_num > 1:
                cp.pixels.fill(0)
                light_num -= 1
                time.sleep(0.3)
            # set password with A and B button
            if cp.button_a:
                sequence[light_num - 1] = cp.button_a
            if cp.button_b:
                sequence[light_num - 1] = cp.button_b
        return sequence
        # else:
        # # for step in sequence:
        #     # if step != "":
        #     # cp.play_file(step)


def use_password(sequence: list):
    count = 0
    for step in sequence:
        if cp.button_a:
            if cp.button_a == step:
                continue
            else:
                for i in range(2):
                    cp.pixels.fill(Red)
                    cp.play_tone = (310, 0.35)
                    time.sleep(0.25)
                    cp.pixels.fill(Black)
                    time.sleep(0.25)
                    exit()
        if cp.button_b:
            if cp.button_b == step:
                continue
            else:
                for i in range(2):
                    cp.pixels.fill(Red)
                    cp.play_tone = (310, 0.35)
                    time.sleep(0.25)
                    cp.pixels.fill(Black)
                    time.sleep(0.25)
                    exit()


def is_it_on(count: int):
    min_time_set = 10
    # temporary value (in seconds) - can be increased to average minimum time a package will sit outside
    for i in range(20):
        # print(f"Analog Voltage: {analogin.value}")
        if analogin.value > 10000:  # values without pressure range from 0 to 8000
            count += 1
            print(f"Count: {count}")
            time.sleep(1.0)
        if analogin.value < 10000 and count > min_time_set:
            emergency_disco()
            return False

        #
        # emergency_disco()
        # use_password()


while True:
    count = 0
    # print(f"Analog Voltage: {analogin.value}")
    # time.sleep(0.1)
    print(count)
    is_it_on(count)
    if is_it_on(count) == False:
        count = 0
        emergency_disco()
    if cp.switch:
        set_password()
    else:
        use_password(set_password())
