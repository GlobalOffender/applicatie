ervaring = input('Hoeveel jaren praktijkervaring heeft u met acrobatiek?: ')
if ervaring >= "3":
    diploma = input("Heeft u een MBO-4 onderneming's diploma in bezit? [Y/N]: ").lower()
    if diploma == "y":
        vracht = input("Heeft u een geldig vrachtwagen rijbewijs in bezit? [Y/N]: ").lower()
        if vracht == "y":
            hoed = input("Heeft u een hoge hoed in bezit? [Y/N]: ").lower()
            if hoed == "y":
                gender = input("Bent u een man of vrouw? ").lower()
                if gender == "man":
                    snor = input("Heeft u een snor van 10 cm breed? [Y/N]: ").lower()
                    if snor == "y":
                        lengteM = input("Hoe lang bent u?: ")
                        if lengteM >= "150":
                            gewichtM = input("Hoe zwaar bent u?: ")
                            if gewichtM >= "90":
                                certificaatM = input('Heeft u de "Overleven met gevarlijk personeel" certificaat? [Y/N]: ').lower()
                                if certificaatM == "y":
                                    print("U bent aangenomen!")
                                else:
                                    print("U bent niet aangenomen.")
                            else:
                                print("U bent niet aangenomen.")
                        else:
                            print("U bent niet aangenomen.")
                    else:
                        print("U bent niet aangenomen.")
                else:
                    haar = input("Draagt u rood krullenhaar langer dan 20 cm? [Y/N]: ").lower()
                    if haar == "y":
                        lengteF = input("Hoe lang bent u?: ")
                        if lengteF >= "150":
                            gewichtF == input("Hoe zwaar bent u?: ")
                            if gewichtF >= "90":
                                certificaatF = input('Heeft u de "Overleven met gevarlijk personeel" certificaat? [Y/N]: ').lower()
                                if certificaatF == "y":
                                    print("U bent aangenomen!")
                                else:
                                    print("U bent niet aangenomen.")
                            else:
                                print("U bent niet aangenomen.")
                        else:
                            print("U bent niet aangenomen.")
                    else:
                        print("U bent niet aangenomen.")
            else:
                print("U bent niet aangenomen.")
        else:
            print("U bent niet aangenomen.")
    else:
        print("U bent niet aangenomen.")
else:
    print("U bent niet aangenomen.")