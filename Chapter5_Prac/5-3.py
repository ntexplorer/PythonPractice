import random
import os
color = ["Green", "Yellow", "Red"]
bullet_num = 10
Game_Point = 0
while bullet_num > 0:
    target_color = random.choice(color)
    os.system('pause')
    if target_color == color[0]:
        print("You just killed a " + target_color +" alien and gained 5 points!")
        Game_Point += 5
    elif target_color == color[1]:
        print("You just killed a " + target_color +" alien and gained 10 points!")
        Game_Point += 10
    else:
        print("You just killed a " + target_color +" alien and gained 15 points!")
        Game_Point += 15
    bullet_num -= 1
    if bullet_num == 0:
        break
print("You've ran out of bullets! Your total score is " + str(Game_Point) + "!")
