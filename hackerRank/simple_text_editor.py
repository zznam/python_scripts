stackUndo = []


def doQuery(s, query, isUndo):
    parts = query.split(' ')
    if (parts[0] == "1"):
        s += parts[1]
        if (not isUndo): stackUndo.append("2 " + str(len(parts[1])))
    elif (parts[0] == "2"):
        newLen = len(s) - int(parts[1])
        removed = s[newLen:len(s)]
        s = s[0:newLen]
        if (not isUndo): stackUndo.append("1 " + removed)
    elif (parts[0] == "3"):
        print(s[int(parts[1]) - 1])
    elif (parts[0] == "4"):
        query = stackUndo.pop()
        s = doQuery(s, query, True)
    return s


s = ''
query = '1 abc'
s = doQuery(s, query, False)
query = '2 1'
s = doQuery(s, query, False)
query = '3 2'
s = doQuery(s, query, False)
query = '4'
s = doQuery(s, query, False)
