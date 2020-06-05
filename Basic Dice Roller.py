import random
class Dice:

    def __init__(self, sides):
        self.sides = sides

    def __repr__(self):
        return "This is a " + str(self.sides) + "-sided dice."
    
    def roll_dice(dice):
        number_of_dice, dice_sides = dice.split('d')
        total_rolled = []
        for dice in range(0, int(number_of_dice)):
            dice_roll = 0
            dice_roll += random.randint(1,int(dice_sides))
            total_rolled.append(dice_roll)
        return total_rolled
    
    def dice_stats(total_rolled):
        smallest_roll = 1000
        stat_total = 0
        for number in total_rolled:
             if number < smallest_roll:
                smallest_roll = number
        stat_total = sum(total_rolled) - smallest_roll
        return (stat_total)
        return (total_rolled)

D6 = Dice(6)

print(D6)
