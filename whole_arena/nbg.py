'''arena = [[0, 0, 0, 1, 2, 3, 0, 0, 0],
         [0, 4, 5, 6, 7, 8, 9, 10, 0],
         [0, 11, 12, 13, 14, 15, 16, 17, 0],
         [18, 19, 20, 21, 22, 23, 24, 25, 26],
         [27, 28, 29, 30, 31, 32, 33, 34, 35],
         [36, 37, 38, 39, 40, 41, 42, 43, 44],
         [0, 45, 46, 47, 48, 49, 50, 51, 0],
         [0, 52, 53, 54, 55, 56, 57, 58, 0],
         [0, 0, 0, 59, 60, 61, 0, 0, 0]]
'''

arena = [[0, 0, 0, 1, 2, 3, 0, 0, 0],
         [0, 4, 5, 6, 7, 8, 9, 10, 0],
         [0, 11, 12, 13, 14, 15, 16, 17, 0],
         [0, 19, 20, 21, 22, 23, 24, 25, 0],
         [0, 28, 29, 30, 31, 32, 33, 34, 0],
         [0, 37, 38, 39, 40, 41, 42, 43, 0],
         [0, 45, 46, 47, 48, 49, 50, 51, 0],
         [0, 52, 53, 54, 55, 56, 57, 58, 0],
         [0, 0, 0, 59, 60, 61, 0, 0, 0]]

pairs = []
for i in xrange(len(arena)):
    for j in xrange(len(arena[i])):
        if arena[i][j]:
            first = (arena[i][j]<10) * "0" + str(arena[i][j])
            if (i > 0):
                if arena[i-1][j]:
                    second = (arena[i-1][j]<10) * "0" +  str(arena[i-1][j])
                    pairs.append([first, second, "left"])
            if (i < len(arena) - 1):
                if arena[i + 1][j]:
                    second = (arena[i+1][j]<10) * "0" +  str(arena[i+1][j])
                    pairs.append([first, second, "right"])
            if (j > 0):
                if arena[i][j-1]:
                    second = (arena[i][j-1]<10) * "0" +  str(arena[i][j-1])
                    pairs.append([first, second, "back"])
            if (j < len(arena[i]) - 1):
                if arena[i][j+1]:
                    second = (arena[i][j+1]<10) * "0" +  str(arena[i][j+1])
                    pairs.append([first, second, "front"])

nbg_file = 'digraph whole_arena {\n    subgraph "beearena" { \n'
for pair in pairs:
    nbg_file += '        "casu-0' + pair[0] + '" -> "casu-0' + pair[1] + '" [label = "' + pair[2] + '" ] \n'

nbg_file += "    }\n}\n"
print nbg_file

with open('nbg_file.nbg', 'w') as f:
    f.write(nbg_file)
