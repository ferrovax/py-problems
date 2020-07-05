# 16.2
# Game 1: You get one shot to make the hoop
# Game 2: You get three shots and must make two of them
# If p is probability of making a shot, find p values for which you should pick
# one game over the other.

# Chance of winning game 1: p

# Chance of winning game 2: p^3 + (1 - p)p^2 * 3

# p = -2p^3 + 3p^2
# ...
# (2p - 1)(p - 1) = 0

# Doesn't matter which game we play at p = 0.5 or at p = 1
# ( or at p = 0 )

# Between 0 and 0.5, p > -2p^3 + 3p^2
# Choose game 1

# Between 0.5 and 1, p < -2p^3 + 3p^2
# Choose game 2
