# Using Python to solve the questions.
# Question 4


def determinFinger(num):
    r = num % 8
    if r == 1:
        return "Thumb"
    if r == 5:
        return "Little Finger"
    if r == 0 or r == 2:
        return "Index Finger"
    if r == 3 or r == 7:
        return "Middle Finger"
    if r == 4 or r == 6:
        return "Ring Finger"


print(determinFinger(13))
