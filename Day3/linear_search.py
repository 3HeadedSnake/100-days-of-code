def lin_search(ourlist, key):
    for index in range(0, len(ourlist)):
        if (ourlist[index] == key):
            return index
        
        else: return "Not Found"

ourlist = [15, 20, 19, 18, 13]

print(lin_search(ourlist, 55))