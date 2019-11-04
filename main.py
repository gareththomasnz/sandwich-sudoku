import pickle
import random
from PIL import Image, ImageDraw, ImageFont

games = pickle.load(open("games_short.p", "rb"))
mx = len(games)
index = random.randrange(0,mx)

grid = []
counter = 0
x = 0
# load in game data from a random string in games
for i in range(9):
    row = []
    for j in range(9):
        row.append(int(games[index][counter]))
        counter+=1
    grid.append(row)


# calculate and store row sums
row_sums = []
for row in grid:
    one = row.index(1)
    nine = row.index(9)
    if abs(one-nine) == 1:
        row_sums.append(0)
    elif one > nine:
        sm = 0
        for i in range(nine+1, one):
            sm += row[i]
        row_sums.append(sm)
    else:
        sm = 0
        for i in range(one+1, nine):
            sm += row[i]
        row_sums.append(sm)


# calculate and store column sums
cols = []
for j in range(9):
    col = []
    for i in range(9):
        col.append(grid[i][j])
    cols.append(col)

col_sums = []
for col in cols:
    one = col.index(1)
    nine = col.index(9)
    if abs(one-nine) == 1:
        col_sums.append(0)
    elif one > nine:
        sm = 0
        for i in range(nine+1, one):
            sm += col[i]
        col_sums.append(sm)
    else:
        sm = 0
        for i in range(one+1, nine):
            sm += col[i]
        col_sums.append(sm)


        

for row in grid:
    print(row)

print('\n')
print(col_sums)
print(row_sums)




sol = Image.new('RGB', (1200,1200), color='white')
s_draw = ImageDraw.Draw(sol)

puz = Image.new('RGB', (1200, 1200), color='white')
p_draw = ImageDraw.Draw(puz)

s_draw.rectangle([(0, 0), (1200, 1200)], outline='black', width=10)
fnt = ImageFont.truetype('arial.ttf', 60)


# generate starting squares
xy = []
while len(xy) < 10:
    t = (random.randrange(9), random.randrange(9))
    if t not in xy:
        xy.append(t)

# draw 9 x 9 grid with numbers

for i in range(1,10):
    for j in range(1,10):
        s_draw.rectangle([(i*100, j*100), ((i+1)*100, (j+1)*100)], outline='black')
        p_draw.rectangle([(i*100, j*100), ((i+1)*100, (j+1)*100)], outline='black')
        s_draw.text((i*100+35, j*100+15), '{}'.format(grid[i-1][j-1]), font=fnt, fill=(0,0,0,255))

        if (i-1, j-1) in xy:
            p_draw.text((i*100+35, j*100+15), '{}'.format(grid[i-1][j-1]), font=fnt, fill=(0,0,0,255))
    


# draw 3 x 3 thick grid
for i in range(3):
    for j in range(3):
        s_draw.rectangle([(i*300+100, j*300+100), ((i+1)*300+100, (j+1)*300+100)], outline='black', width=5)
        p_draw.rectangle([(i*300+100, j*300+100), ((i+1)*300+100, (j+1)*300+100)], outline='black', width=5)


# draw row + column sums
for i in range(9):
    s_draw.text((1025, i*100+110), '{}'.format(col_sums[i]), font=fnt, fill=(0,0,0,255))
    p_draw.text((1025, i*100+110), '{}'.format(col_sums[i]), font=fnt, fill=(0,0,0,255))
    if int(row_sums[i]/10)==0:
        s_draw.text((i*100+135, 1015), '{}'.format(row_sums[i]), font=fnt, fill=(0,0,0,255))
        p_draw.text((i*100+135, 1015), '{}'.format(row_sums[i]), font=fnt, fill=(0,0,0,255))
    else:
        s_draw.text((i*100+120, 1015), '{}'.format(row_sums[i]), font=fnt, fill=(0,0,0,255))
        p_draw.text((i*100+120, 1015), '{}'.format(row_sums[i]), font=fnt, fill=(0,0,0,255))






sol.save('solution.png', 'PNG')
puz.show()
puz.save('puzzle.png', 'PNG')

