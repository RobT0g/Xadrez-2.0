def getMinPos(pos, line):
    if line:
        return [[i for i in range(pos[0])], [i for i in range(pos[0]+1, 8)], 
            [i for i in range(pos[1])], [i for i in range(pos[1]+1, 8)]]
    return [[]]
    
print(getMinPos((5, 5), diagonal=0))
