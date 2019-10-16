import csv
import pickle

games = []
with open("sudoku.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[1] != 'solutions':
            games.append(row[1])



with open("sudoku.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    games_short = []
    count = 0
    for row in readCSV:
        if count > 2000:
            break
        elif row[1] != 'solutions':
            games_short.append(row[1])
            count += 1

pickle.dump(games, open("games.p", "wb"))
pickle.dump(games_short, open("games_short.p", "wb"))

