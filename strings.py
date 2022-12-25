# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = 'Ruud Gullit '
scorer_1 = 'Marco van Basten '

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + str(goal_0)  + ", " + scorer_1 + str(goal_1)

report = f'{scorer_0}scored in the {goal_0}nd minute' '\n' f'{scorer_1}scored in the {goal_1}th minute'

player = "Frank Rijkaard"
first_name = player[:5]
last_name = player[6:]
name_short = player[0] + '. ' + last_name
last_name_len = 8
first_name_len = 5
chant = (first_name +'!' + ' ') * first_name_len
chant = chant[:-1]
good_chant = (chant[-1] != ' ')

print(good_chant)




