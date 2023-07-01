import sys
import time
import bext, random

width, height = bext.size()
width -= 1
PAUSE_AMOUNT=0.1
number_of_logos = 50
up_left = 'ul'
up_right = 'ur'
down_right = 'dr'
down_left = 'dl'
directions = (up_right, up_left, down_right, down_left)
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
color = 'color'
x = 'x'
y = 'y'
dir = 'direction'


def main():

    cornerBounces = 0
    bext.clear()
    logos = []
    for i in range(number_of_logos):
        logos.append({color: random.choice(colors),
                      x:random.randint(1, width-4),
                      y:random.randint(1, height -4),
                      dir: random.choice(directions)})
        
        if logos[-1][x] % 2 == 1:
            logos[-1][x] -= 1
        
    while True:
        for logo in logos:
            bext.goto(logo[x], logo[y])
            print('    ', end='')

            originalDirection = logo[dir]

            if logo[x] == 0 and logo[y] == 0:
                logo[dir] = down_right
                cornerBounces += 1 
                    
            elif logo[x] == 0 and logo[y] == height - 1:
                logo[dir] = up_right
                cornerBounces += 1 
                    
            elif logo[x] == width - 3 and logo[y] == 0:
                logo[dir] = down_left
                cornerBounces += 1

            elif logo[x] == width - 3 and logo[y] == height - 1:
                logo[dir] = down_left
                cornerBounces += 1

            elif logo[x] == 0 and logo[dir] == up_left:
                logo[dir] = up_right              
            elif logo[x] == 0 and logo[dir] == down_left:
                logo[dir] = down_right

            elif logo[x] == width - 3 and logo[dir] == up_right:
                logo[dir] = up_left
            elif logo[x] == width - 3 and logo[dir] == down_right:
                logo[dir] = down_left

            elif logo[y] == 0 and logo[dir] == up_left:
                logo[dir] = down_left
            elif logo[y] == 0 and logo[dir] == up_right:
                logo[dir] = down_right

            elif logo[y] == height - 1 and logo[dir] == down_left:
                logo[dir] = up_left
            elif logo[y] == height - 1 and logo[dir] == down_right:
                logo[dir] = up_right


            if logo[dir] != originalDirection:
                logo[color] = random.choice(colors)


            if logo[dir] == up_right:
                logo[x] += 2
                logo[y] -= 1

            elif logo[dir] == up_left:
                logo[x] -= 2
                logo[y] -= 1

            elif logo[dir] == down_right:
                logo[x] += 2
                logo[y] += 1

            elif logo[dir] == down_left:
                logo[x] -= 2
                logo[y] += 1
            
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces)
        for logo in logos:
            bext.goto(logo[x], logo[y])
            bext.fg(logo[color])
            print('DVD', end='')
            
        bext.goto(0, 0)
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit()