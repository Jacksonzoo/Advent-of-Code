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

def check_math(a, b, button_ax, button_ay, button_bx, button_by, prize_x, prize_y):
    return a * button_ax + b * button_bx == prize_x and a * button_ay + b * button_by == prize_y


def play_machine(arcade):
    total_tokens = 0
    for machine in arcade:
        
        direction_a, direction_b, position_p = machine['Button A'], machine['Button B'], machine['Prize']
        ax, ay = direction_a
        bx, by = direction_b
        px, py = position_p

        token_cost = float('inf')
        
        for a in range(100):
            for b in range(100):
                if check_math(a, b, ax, ay, bx, by, px, py):
                    token = a * 3 + b
                    token_cost = min(token_cost, token)

        if token_cost != float('inf'):
            total_tokens += token_cost

    return total_tokens


arcade = open_instructions("testinput.txt")
machine = play_machine(arcade)
print(machine)


# Part 2



