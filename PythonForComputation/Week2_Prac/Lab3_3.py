def rhyme():
    a = input("Please enter name A: ")
    b = input("Please enter name B: ")
    rhyme1 = "\tChild_a and Child_b went up the hill,\n\tto fetch a pail of water. \n\tChild_a fell down and broke his crown, \n\tand Child_b came tumbling after."
    rhyme1 = rhyme1.replace("Child_a", a).replace("Child_b", b)
    print(rhyme1)


rhyme()
