# Using Python to solve the questions.
# Question 1


def countXCharacters(string):
    # get the half length of the string
    half_len = len(string) // 2
    left_str = string.count("x", 0, half_len)
    right_str = string.count("x", half_len)
    print(left_str)
    print(right_str)

    if left_str > right_str:
        return "left"
    elif left_str < right_str:
        return "right"
    else:
        return "equal"


a = countXCharacters("xx-xxx")
print(a)
