# Using Python to solve the questions.
# Question 3

from string import ascii_lowercase
from string import ascii_uppercase


def encryptMessage(msg):
    alphabet_lower = ascii_lowercase
    alphabet_lower_reverse = alphabet_lower[::-1]
    alphabet_upper = ascii_uppercase
    alphabet_upper_reverse = alphabet_upper[::-1]
    encrypt_dict = {}
    lower_dict = dict(zip(alphabet_lower, alphabet_lower_reverse))
    upper_dict = dict(zip(alphabet_upper, alphabet_upper_reverse))
    encrypt_dict.update(lower_dict)
    encrypt_dict.update(upper_dict)

    msg_reverse = ""
    msg_reverse_list = [encrypt_dict[i] for i in msg]
    msg_reverse = "".join(msg_reverse_list)
    return msg_reverse


print(encryptMessage("CashCalc"))
