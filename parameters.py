print("\nWELCOME to the Exploratory Data Analysis zone ...\n")
t=0

while t<1:
    print("Select the parameter to analyze and visualize data\n")
    y = int(input("1. Engine Location\n2. Engine Fuel\n3. Horse Power\n\n"))

    if y == 1:
        print("Select the mode of visualization\n")
        z = int(input("1. Bar Graph\n2. Histogram\n3. Pie Chart\n\n"))

        if z == 1:
            import enginetype

            enginetype.frontengine()
            enginetype.rearengine()
            import main

        elif z == 2:
            import enginetype_histogram
            import main

        elif z == 3:
            import enginetype_piechart
            import main

        else:
            print("Invalid input")
            import main

    elif y == 2:
        print("Select the mode of visualization\n")
        z = int(input("1. Bar Graph\n2. Double bar graph\n3. Histogram\n4. Pie Chart\n\n"))

        if z == 1:
            import fuelbargraph
            import main

        elif z == 2:
            import fueldoublegraph
            import main

        elif z == 3:
            import fuelgraphhistogram
            import main

        elif z == 4:
            import fuelgraphpie
            import main

        else:
            print("Invalid input")
            import main

    elif y == 3:
        print("Select the mode of visualization\n")
        z = int(input("1. Bar Graph\n2. Histogram\n3. Pie Chart\n\n"))
        import horsepowergraph

        if z == 1:
            horsepowergraph.barg()
            import main

        elif z == 2:
            horsepowergraph.histogram()
            import main

        elif z == 3:
            horsepowergraph.piechart()
            import main

        else:
            print("Invalid input")
            import main



    else:
        print("Invalid intput")
        import main












