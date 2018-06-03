import matplotlib.pyplot as plt
from pylab import *

nisradlist = []
nislidlist = []

with open("./output/NIS_lidar.txt") as file:
    for line in file:
        line = line.strip()
        nislidlist.append(line)

with open("./output/NIS_radar.txt") as file:
    for line in file:
        line = line.strip()
        nisradlist.append(line)

plt.figure(figsize=(8, 4))
plt.plot(nisradlist)
plt.ylabel('NIS Value')
plt.xlabel('Time Step')
plt.title('Radar NIS Values')
plt.axhline(y=7.8, color='r', linestyle='-')
plt.ylim([0,15])
# plt.show()
plt.savefig('NIS_radar.png')


plt.figure(figsize=(8,4))
plt.plot(nislidlist)
plt.ylabel('NIS Value')
plt.xlabel('Time Step')
plt.title('Lidar NIS Values')
plt.axhline(y=6.0, color='r', linestyle='-')
plt.ylim([0,15])
# plt.show()
plt.savefig('NIS_lidar.png')