import collections
import math

class Block():
    def __init__(self, school = False, gym = False, market = False, cinema = False):
        #self.school, self.gym, self.market, self.cinema = school, gym, market, cinema
        self.data = {"School":school, "Gym":gym, "Market":market, "Cinema":cinema}

#__main__
b1 = Block()
b2 = Block()
b3 = Block(school=True, gym=True)
b4 = Block()
b5 = Block(market = True)

lane = [b1, b2, b3, b4, b5]
necc = ["Gym", "School", "Market"]

indices = {}
distances = []

#Get the indices of the neccesities
for i in necc:
    index = 0
    for j in lane:
        if j.data[i] == True:
            indices[i] = index
        index += 1

#Get the distances of neccesities from each block
index = 0
for k in lane:
    dis = 0
    for l in necc:
        dis += abs(indices[l] - index)
    distances.append(dis)
    index += 1

#Get the smallest distance
smallest_distance = math.inf
app_house_index = None

for m in distances:
    if m < smallest_distance:
        smallest_distance = m
        app_house_index = distances.index(m)

print(app_house_index)