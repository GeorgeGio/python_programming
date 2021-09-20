def milkshakes(size,**kwargs):
    """Milkshake function """

    print(size)

    for keyword, flavor in kwargs.item():
        print("My", keyword, "is a", flavor)



ms_size = "small"

milkshakes(ms_size, kw1 = "mint",
                    kw2 = "chocolate",
                    kw3 = "banaa",
                    kw4 = "other flavor")
