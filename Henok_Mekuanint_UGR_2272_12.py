#function that merges
import random
num_list=[0,1]
num1=random.choice((0,2))
num2=random.choice((0,2))
num3=random.choice((0,2))
num4=random.choice((0,2))
num5=random.choice((0,2))
num6=random.choice((0,2))
num7=random.choice((0,2))
num8=random.choice((0,2))
num9=random.choice((0,2))
num10=random.choice((0,2))
num11=random.choice((0,2))
num12=random.choice((0,2))
num13=random.choice((0,2))
num14=random.choice((0,2))
num15=random.choice((0,2))
num16=random.choice((0,2))
store1=[num1,num2,num3,num4]
store2=[num5,num6,num7,num8]
store3=[num9,num10,num11,num12]
store4=[num13,num14,num15,num16]
store=[]
print(store1,"                            A ---FOR  LEFT SHIFT")
print(store2,"                            D ---FOR RIGHT SHIFT")
print(store3,"                            W ---FOR UP SHIFT")
print(store4,"                            S ---FOR DOWN SHIFT and               press C TO LEAVE THE GAME")
button=1
while True:
    button = input("PLEASE ENTER THE ABOVE BUTTON TO PLAY THE GAME:")
    if button == 'A' or button == 'a':
        def merge(row):
            def single_column_or_row_merger(array1):
                array2 = []
                i = 0
                while (i < len(array1)):
                    if array1[i] != 0:
                        array2.append(array1[i])
                    i += 1
                if (len(array2) < len(array1)):
                    array2.extend([0] * (len(array1) - len(array2)))
                return array2

            def add_tiles(array1):
                i = 0
                while (i < (len(array1) - 1)):
                    while (array1[i] == array1[i + 1]):
                        array1[i] = array1[i] * 2
                        array1[i + 1] = 0
                        break
                    i = i + 1
                return array1

            tile1 = single_column_or_row_merger(row)
            tile2 = add_tiles(tile1)
            tile3 = single_column_or_row_merger(tile2)
            return tile3


        store1 = merge(store1)
        store2 = merge(store2)
        store3 = merge(store3)
        store4 = merge(store4)

        for i in range(0,3):
            if store1[i]==0:
                store1[i]=2
                print("new 2 generated on first row",i,"index")
                break
            if store2[i]==0:
                store2[i]=2
                print("new 2 generated on second row", i, "index")
                break
            if store3[i]==0:
                store3[i]=2
                print("new 2 generated on third row", i, "index")
                break
            if store4[i]==0:
                store4[i]=2
                print("new 2 generated on fourth row", i, "index")




        print((store1), "                            A ---FOR  LEFT SHIFT")
        print((store2), "                            D ---FOR RIGHT SHIFT")
        print((store3), "                            W ---FOR UP SHIFT")
        print((store4), "                            S ---FOR DOWN SHIFT AND           PRESS C TO LEAVE THE GAME")


    if button == 'd' or button == 'D':
        def merge_right(row):
            def row_merger(array1):
                array2 = []
                i = len(array1) - 1
                while (i >= 0):
                    if array1[i] != 0:
                        array2.insert(i, array1[i])
                    i -= 1
                d = len(array1) - len(array2)
                i = 0
                while (i < d):
                    array2.insert(i, 0)
                    i += 1
                return array2

            def add_tiles(array1):
                i = 0
                while (i < (len(array1) - 1)):
                    while (array1[i] == array1[i + 1]):
                        array1[i] = array1[i] * 2
                        array1[i + 1] = 0
                        break
                    i = i + 1
                return array1

            tile1 = row_merger(row)
            tile2 = add_tiles(tile1)
            tile3 = row_merger(tile2)
            return tile3


        store1 = merge_right(store1)
        store2 = merge_right(store2)
        store3 = merge_right(store3)
        store4 = merge_right(store4)
        for i in range(0,3):
            if store1[i] == 0:
                store1[i] = 2
                print("new 2 generated on first row", i, "index")
                break

            if store2[i]==0:
                store2[i]=2
                print("new 2 generated on second row", i, "index")
                break
            if store3[i]==0:
                store3[i]=2
                print("new 2 generated on third row", i, "index")
                break
            if store4[i]==0:
                store4[i]=2
                print("new 2 generated on fourth row", i, "index")
        print((store1), "                            A ---FOR  LEFT SHIFT")
        print((store2), "                            D ---FOR RIGHT SHIFT")
        print((store3), "                            W ---FOR UP SHIFT")
        print((store4), "                            S ---FOR DOWN SHIFT              PRESS C LEAVE THE GAME")



    if button == 'w' or button == "W":
        store_a = [store1[0],store2[0],store3[0],store4[0]]
        store_b = [store1[1],store2[1],store3[1],store4[1]]
        store_c = [store1[2],store2[2],store3[2],store4[2]]
        store_d = [store1[3],store2[3],store3[3],store4[3]]


        def merge(row):
            def single_column_or_row_merger(array1):
                array2 = []
                i = 0
                while (i < len(array1)):
                    if array1[i] != 0:
                        array2.append(array1[i])
                    i += 1
                if (len(array2) < len(array1)):
                    array2.extend([0] * (len(array1) - len(array2)))
                return array2

            def add_tiles(array1):
                i = 0
                while (i < (len(array1) - 1)):
                    while (array1[i] == array1[i + 1]):
                        array1[i] = array1[i] * 2
                        array1[i + 1] = 0
                        break
                    i = i + 1
                return array1

            tile1 = single_column_or_row_merger(row)
            tile2 = add_tiles(tile1)
            tile3 = single_column_or_row_merger(tile2)
            return tile3


        storeha = merge(store_a)
        storehu = merge(store_b)
        storehi = merge(store_c)
        storehe = merge((store_d))
        store1[0] = storeha[0]
        store2[0] = storeha[1]
        store3[0] = storeha[2]
        store4[0] = storeha[3]

        store1[1] = storehu[0]
        store2[1] = storehu[1]
        store3[1] = storehu[2]
        store4[1] = storehu[3]

        store1[2] = storehi[0]
        store2[2] = storehi[1]
        store3[2] = storehi[2]
        store4[2] = storehi[3]

        store1[3] = storehe[0]
        store2[3] = storehe[1]
        store3[3] = storehe[2]
        store4[3] = storehe[3]

        for i in range(0,3):
            if store1[i]==0:
                store1[i]=2
                print("new 2 generated on first row",i,"index")
                break
            if store2[i]==0:
                store2[i]=2
                print("new 2 generated on second row", i, "index")
                break
            if store3[i]==0:
                store3[i]=2
                print("new 2 generated on third row", i, "index")
                break
            if store4[i]==0:
                store4[i]=2
                print("new 2 generated on fourth row", i, "index")

        print(store1, "                            A ---FOR  LEFT SHIFT")
        print(store2, "                            D ---FOR RIGHT SHIFT")
        print(store3, "                            W ---FOR UP SHIFT")
        print(store4, "                            S ---FOR DOWN SHIFT                     PRESS C TO LEAVE THE GAME")


    if button == "s" or button == "S":
        store_a = [store1[0], store2[0], store3[0], store4[0]]
        store_b = [store1[1], store2[1], store3[1], store4[1]]
        store_c = [store1[2], store2[2], store3[2], store4[2]]
        store_d = [store1[3], store2[3], store3[3], store4[3]]


        def merge_right(row):
            def row_merger(array1):
                array2 = []
                i = len(array1) - 1
                while (i >= 0):
                    if array1[i] != 0:
                        array2.insert(i, array1[i])
                    i -= 1
                d = len(array1) - len(array2)
                i = 0
                while (i < d):
                    array2.insert(i, 0)
                    i += 1
                return array2

            def add_tiles(array1):
                i = 0
                while (i < (len(array1) - 1)):
                    while (array1[i] == array1[i + 1]):
                        array1[i] = array1[i] * 2
                        array1[i + 1] = 0
                        break
                    i = i + 1
                return array1

            tile1 = row_merger(row)
            tile2 = add_tiles(tile1)
            tile3 = row_merger(tile2)
            return tile3


        storeha = merge_right(store_a)
        storehu = merge_right(store_b)
        storehi = merge_right(store_c)
        storehe = merge_right((store_d))

        store1 = [storeha[0], storehu[0], storehi[0], storehe[0]]
        store2 = [storeha[1], storehu[1], storehi[1], storehe[1]]
        store3 = [storeha[2], storehu[2], storehi[2], storehe[2]]
        store4 = [storeha[3], storehu[3], storehi[3], storehe[3]]

        for i in range(0,3):
            if store1[i]==0:
                store1[i]=2
                print("new 2 generated on first row",i,"index")
                break
            if store2[i]==0:
                store2[i]=2
                print("new 2 generated on second row", i, "index")
                break
            if store3[i]==0:
                store3[i]=2
                print("new 2 generated on third row", i, "index")
                break
            if store4[i]==0:
                store4[i]=2
                print("new 2 generated on fourth row", i, "index")

        print(store1, "                            A ---FOR  LEFT SHIFT")
        print(store2, "                            D ---FOR RIGHT SHIFT")
        print(store3, "                            W ---FOR UP SHIFT")
        print(store4, "                            S ---FOR DOWN SHIFT            PRESS C TO LEAVE THE GAME")
    if button=="c" or button=="C":
        print("GAME OVER")
        break
    for i in range(0,3):
        if store1[i]==2048:
            print("CONGRATULATION YOU HAVE WON THE GAME")
            break
        if store2[i]==2048:
            print("CONGRATULATION YOU HAVE WON THE GAME")
            break
        if store3[i]==2048:
            print("CONGRATULATION YOU HAVE WON THE GAME")
            break
