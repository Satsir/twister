import random

# body_part = ['Hl', 'Hr', 'Ll', 'Lr']
# color = ['W', 'B', 'Y', 'G']
body_part = ['Left Hand', 'Right Hand', 'Left Leg', 'Right Leg']
color = ['White', 'Blue', 'Yellow', 'Green']
res = random.choice(body_part) + ' on ' + random.choice(color) + '\n' + '\n' + 'Refresh (F5) to make a next move.'
# For Flask:
# res = random.choice(body_part) + ' on ' + random.choice(color) + '<br/>' + '<br/>' + 'Refresh (F5) to make a next move.'

print(res)

# Online Twister move generator
# http://satsir.pythonanywhere.com
