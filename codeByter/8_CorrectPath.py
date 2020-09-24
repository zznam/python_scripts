import time
start_time = time.time()


class Node:
    def __init__(self, strA, positions, depth=0, last_node=None):
        if depth == len(strA):
            Node.strA = strA
            Node.positions = positions
        else:
            if strA[depth] == '?':
                self.possible_direction = ['r', 'l', 'u', 'd']
                if (positions[depth][0] == 0):
                    self.possible_direction.remove('u')
                elif (positions[depth][0] == 4):
                    self.possible_direction.remove('d')
                if (positions[depth][1] == 0):
                    self.possible_direction.remove('l')
                elif (positions[depth][1] == 4):
                    self.possible_direction.remove('r')
            else:
                self.possible_direction = [strA[depth]]

            self.possible_next_node = []
            for d in self.possible_direction:
                next_pos = Node.deplace(positions[depth], d)
                if ((positions[depth+1] == []) or (positions[depth+1] == next_pos)) and ((next_pos[0] >= 0) and (next_pos[0] <= 4) and (next_pos[1] >= 0) and (next_pos[1] <= 4)):
                    positions_ = positions[:depth+1] + \
                        [next_pos]+positions[depth+2:]
                    strA_ = strA[:depth]+d+strA[depth+1:]
                    self.possible_next_node += [Node(strA_, positions_, depth+1, self)]

    def deplace(pos_, s):
        pos = [pos_[0], pos_[1]]
        if(s == 'r'):
            pos[1] += 1
        elif(s == 'l'):
            pos[1] -= 1
        elif(s == 'd'):
            pos[0] += 1
        elif(s == 'u'):
            pos[0] -= 1
        return pos


def CorrectPath(strA):
    print([[0, 0]]+[[] for i in range(len(strA)-1)]+[[4, 4]])
    tree = Node(strA, [[0, 0]]+[[] for i in range(len(strA)-1)]+[[4, 4]])
    return tree.strA


print(CorrectPath("???rrurdr?"))

# keep this function call here
# print(CorrectPath("???rrurdr?"))  # dddrrurdrd
print(CorrectPath("drdr??rrddd?"))  # drdruurrdddd
# print(checkCorrectPath("drdruurrdddd"))  # drdruurrdddd
# print(checkCorrectPath("dddrrurdrd"))  # drdruurrdddd
# print(CorrectPath(input()))
print("--- %s seconds ---" % (time.time() - start_time))
