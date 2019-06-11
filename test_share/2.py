lst = "[1, 2, 3, 4, 5, 6, 7]"

intLst = (1, 2, 3, 4, 5, 6, 7, 8, 0)

tempLst = lst.replace("[", "").replace("]", "").split(", ").copy()
lst = []
for element in tempLst:
    try:
        if int(element) in intLst:
            lst.append(int(element))
        else:
            lst.append(element)
    except:
        lst.append(element)

print(lst)