import pickle
import random
from PIL import Image, ImageDraw

games = pickle.load(open("games.p", "rb"))
mx = len(games)
index = random.randrange(0,mx)

grid = []
counter = 0
for i in range(9):
    row = []
    for j in range(9):
        row.append(games[index][counter])
        counter+=1
    grid.append(row)

for row in grid:
    print(row)

row_sums = []
for row in grid:
    one = row.index(1)
    nine = row.index(9)
    if abs(one-nine) == 1:
        row_sums.append(0)

im = Image.new('RGB', (1200,1200), color='white')
draw = ImageDraw.Draw(im)

draw.rectangle([(0, 0), (1200, 1200)], outline='black', width=10)

for i in range(1,10):
    for j in range(1,10):
        draw.rectangle([(i*100, j*100), ((i+1)*100, (j+1)*100)], outline='black')

for i in range(3):
    for j in range(3):
        draw.rectangle([(i*300+100, j*300+100), ((i+1)*300+100, (j+1)*300+100)], outline='black', width=5)


im.save('test.png', 'PNG')

