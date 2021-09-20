angry = True
bored = True
hungry = False
tired = False


if tired and hungry:
    print("T-Rex eats Iguanadon")
elif hungry and bored:
    print("T-Rex eats Stegasaurus")
elif tired:
    print("T-Rex is going bed")
elif angry and bored:
    print("T-Rex fights Velociraptor")
elif angry or bored:
    print("T-Rex roars")
else:
    print("T-Rex gives a smile")
