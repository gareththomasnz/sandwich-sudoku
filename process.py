import csv
import pickle

games = []
with open("sudoku.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[1] != 'solutions':
            games.append(row[1])
pickle.dump(games, open("games.p", "wb"))

