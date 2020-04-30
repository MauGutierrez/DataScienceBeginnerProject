import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv 

x = []
mostGoals = []
championGoals = []
lessGoals = []
championGoalsAgainst = []

index = 0
bar_width = 0.20

with open("data/GoalsScoredPerTeam.csv", 'r') as f:
	wines = list(csv.reader(f, delimiter=","))

fig, ax = plt.subplots()
for data in wines[1:]:
	index += 1
	x.append((data[0]))
	mostGoals.append(int(data[1]))
	lessGoals.append(int(data[2]))
	championGoals.append(int(data[3]))
	championGoalsAgainst.append(int(data[4]))

index = np.arange(index)

bestOffensive = ax.bar(index, mostGoals, bar_width, label="Best Offensive")
offensiveChampion = ax.bar(index+bar_width, championGoals, bar_width, label="Offensive Champion")
bestDefensive = ax.bar(index, lessGoals, bar_width, label="Best Defensive")
defensiveChampion = ax.bar(index+bar_width, championGoalsAgainst, bar_width, label="Defensive Champion")

ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(x)
ax.legend()
plt.grid()
plt.show()