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

header = '# Deployment specification file\n# For each casu in the arena, we need to specifiy:\n#     - the hostname of the target machine\n#     - the controller and additional files to deploy\n\nbeearena :\n'

for bbg in bbgs.keys():
    for casu in bbgs[bbg]:
        casuname = '0' + str(casu)
        casuname = casuname[-2:]

        bbgname = '0' + str(int(bbg))
        bbgname = bbgname[-2:]

        line1 = '    casu-0' + casuname + ' :\n'
        line2 = '        hostname : bbg-0' + bbgname + '\n'
        line3 = '        prefix : deploy\n        controller : controllers/blink_and_send_seed.py\n        extra : []\n'
        header += line1 + line2 + line3

with open('whole_arena.dep', 'w') as depfile:
    depfile.write(header)
