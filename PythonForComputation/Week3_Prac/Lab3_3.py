def weight_detect(weights):
    lorry = 0
    weight_active = True
    while True:
        for i in weights:
            if lorry <= 3000 - i:
                lorry += i
                print("Pallet added, now the total weight is {} Kg.".format(str(lorry)))
            else:
                print("Lorry would overload if pallet added, stopping procejure, the total weight is {} Kg now.".format(
                    str(lorry)))
                break
        break


weights = [750, 387, 291, 712, 100, 622, 109, 750, 282, 999, 100]
weight_detect(weights)
