def SwapFileData ():

    file1=input("Enter your file name:")
    with open(file1) as a:
        data_a=a.read()

    with open(file1) as a:
        data_b=a.read()

    with open(file1) as a:
        a.write(data_b)


    with open(file1) as a:
        a.write(data_a)

SwapFileData()