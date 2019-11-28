# Using Python to solve the questions.
# Question 2


def getSeason(num):
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]
    if num in winter:
        return "Winter"
    elif num in spring:
        return "Spring"
    elif num in summer:
        return "Summer"
    elif num in autumn:
        return "Autumn"
    else:
        raise ValueError("Invalid Value.")


print(getSeason(222))
