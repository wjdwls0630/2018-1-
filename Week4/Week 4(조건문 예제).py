#pH 측정
while True :
    try :
        pH = float(input("Enter the pH level: "))
        if 0.0 <= pH <= 14.0:
            if pH < 5.0:
                print(pH, "is strong acid!")
                print("Be careful wiht that!")
            elif pH < 7.0:
                print(pH, "is weak acid!")
                print("Be careful wiht that!")
            elif pH < 8.0:
                print(pH, "is neutral.")
            elif pH < 10.0:
                print(pH, "is weak base!")
                print("Be careful wiht that!")
            else:
                print(pH, "is strong base!")
                print("Be careful wiht that!")
            break
        else:
            print("You enter the wrong pH level!\npH value has to be a number between 0 and 14")

    except ValueError : print("pH level is a number! ")



#compound 이름 알려주기
while True :
    compound = (input("Enter the compound[Caution: You can only choose H2O, NH4, CH4]:")).upper()
    if compound in ["H2O", "NH4", "CH4"]:
        if compound == "H2O":
            print("Water")
        elif compound == "NH4":
            print("Ammonia")
        else:
            print("Methane")
        break
    else:
        print("Unknown compound!\nEnter again!")


