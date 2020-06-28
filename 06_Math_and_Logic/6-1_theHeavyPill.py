# 6.1
# You have 20 bottles of pills. 19 bottles have 1.0 g pills, but one has pills
# weighing 1.1 g. Given a scale that provides an exact measurement, how would
# you find the heavy bottle?
# You can only use the scale once.

import random

num = 20

# keep a list of the bottles by their pill weight, one being 1.1 grams
bottles = [1] * num
bottles[random.randint(0, num - 1)] = 1.1

pills = [0] * num

# add pills from each bottle equal to the bottle number
for index in range(num):
    pills[index] = (index + 1) * bottles[index]

weight = sum(pills)

# num*(num+1)/2 is the sum we would expect if all pills weighed 1 gram
diff = round(weight - num * (num + 1) / 2, 1)

bottle = int(diff * 10 - 1)

print(bottles[bottle] == 1.1)
