# Open the input file as button instructions and answer

def open_instructions(filename):
    arcade = []
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

        button_a, button_b, prize = None, None, None

        for line in lines:
            if line.startswith("Button A"):
                x = line.split()[2]
                y = line.split()[3]
                ax = int(x.split('+')[1].strip(','))
                ay = int(y.split('+')[1])
                button_a = (ax, ay)
            elif line.startswith("Button B"):
                x = line.split()[2]
                y = line.split()[3]
                bx = int(x.split('+')[1].strip(','))
                by = int(y.split('+')[1])
                button_b = (bx, by)
            elif line.startswith("Prize"):
                x_prize = int(line.split()[1].split('=')[1].strip(','))
                y_prize = int(line.split()[2].split('=')[1])
                prize = (x_prize, y_prize)

                if button_a and button_b and prize:
                    arcade.append({
                        'Button A': button_a,
                        'Button B': button_b,
                        'Prize': prize
                    })

                    button_a, button_b, prize = None, None, None
    return arcade
                                       
            
# Part 1 describes a claw magine arcade game, where instead of joystick we have 2 buttons "A" and "B"
# Assuming we start at (0, 0) on a grid, we need to reach the prize at location (x, y)
# Button A costs 3 tokens to use and moves along the X and Y axis a certain amount
# Button B costs 1 token to use and also moves along the X and Y axis a certain amount
# Each button should be pressed no more than 100 times to win a prize
# Goal is to find the least amount of tokens used to win as many prizes as possible









print(open_instructions("testinput.txt"))