arena = [[0, 0, 0, 1, 2, 3, 0, 0, 0],
         [0, 4, 5, 6, 7, 8, 9, 10, 0],
         [0, 11, 12, 13, 14, 15, 16, 17, 0],
         [0, 19, 20, 21, 22, 23, 24, 25, 0],
         [0, 28, 29, 30, 31, 32, 33, 34, 0],
         [0, 37, 38, 39, 40, 41, 42, 43, 0],
         [0, 45, 46, 47, 48, 49, 50, 51, 0],
         [0, 52, 53, 54, 55, 56, 57, 58, 0],
         [0, 0, 0, 59, 60, 61, 0, 0, 0]]

bbgs = {
    '1' : [7, 6, 1],
    '2' : [3, 2, 8],
    '3' : [5, 4, 12],
    '4' : [10, 9, 17],
    '5' : [13, 14, 21, 22],
    '6' : [15, 32, 23],
    '7' : [20, 28, 29],
    '8' : [25, 24, 34],
    '9' : [11, 19, 37],
    '10' : [30, 39, 38],
    '11' : [41, 40, 47],
    '12' : [51, 43, 42],
    '13' : [46, 52, 45],
    '14' : [55, 53, 54],
    '15' : [49, 56, 48],
    '16' : [50, 57, 58],
    '17' : [59, 60, 61],
    '18' : [16, 31, 33]}

header = '# Configuration file describing a whole arena\n\n# the position of the CASUs in reality and GUI is identical\n\n# Layer names can be assigned arbitrarily,\n# as long as they consist only of letters, dashes and underscores\n\nbeearena :\n    # Casu names have to start with casu- in order for\n    # automatic spawning to work; they are also only\n    # allowed to contain letters, dashes and underscores\n'

for iArena in range(len(arena)):
    for jArena in range(len(arena[iArena])):
        casu = arena[iArena][jArena]
        if casu:
            posX = -36 + jArena * 9
            posY = 36 - iArena * 9
            bbg = [key for key in bbgs.keys() if casu in bbgs[key]]
            bbg = bbg[0]
            casus = bbgs[bbg]
            if len(casus) < 4:
                i = 0
                while (len(casus) < 4):
                    temp = []
                    temp.append(casus[0:i+1])
                    temp.append([0])
                    temp.append(casus[i+1:])
                    casus = [item for sublist in temp for item in sublist]
                    i += 2
            iCasu = casus.index(casu)
            casuname = '0' + str(casu)
            casuname = casuname[-2:]
            bbgname = '0' + str(bbg)
            bbgname = bbgname[-2:]
            line1 = '    casu-0' + casuname + ' : \n'
            line2 = '        pose : {x : ' + str(posX) + ', y : ' + str(posY) + ', yaw : -1.57}\n'
            line3 = '        sub_addr : tcp://bbg-0' + bbgname + ':' + str(iCasu+1) + '555\n'
            line4 = '        pub_addr : tcp://bbg-0' + bbgname + ':' + str(iCasu+1) + '556\n'
            line5 = '        msg_addr : tcp://bbg-0' + bbgname + ':5' + bbgname + '0' + str(iCasu+1) + '\n\n'
            header += line1 + line2 + line3 + line4 + line5

with open('arenafile.arena', 'w') as arenafile:
    arenafile.write(header)
