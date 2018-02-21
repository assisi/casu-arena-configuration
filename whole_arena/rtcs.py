
casu = 16
bbg = 12
iCasu = 1

bbgs = {'1' : [1, 2, 6, 7], '2' : [3, 8], '9' : [18, 27, 36, 37], '12' : [26, 35, 43, 44], '14' : [54, 55, 59, 60], '15' : [48, 49, 56, 61]}

content = ['name: casu-0', 'pub_addr: tcp://bbg-0', 'sub_addr: tcp://bbg-0', 'msg_addr: tcp://*:5', 'neighbors:']

for bbg in bbgs.keys():
    casus = bbgs[bbg]
    for casu, iCasu in zip(casus, xrange(len(casus))):
        casuname = '0' + str(casu)
        casuname = casuname[-2:]

        bbgname = '0' + str(bbg)
        bbgname = bbgname[-2:]

        lines = []
        lines.append(content[0] + casuname + '\n')
        lines.append(content[1] + bbgname + ':' + str(iCasu + 1) + '556' +'\n')
        lines.append(content[2] + bbgname + ':' + str(iCasu + 1) + '555' +'\n')
        lines.append(content[3] + bbgname + casuname + '\n')
        lines.append(content[4] + '\n')

        filename = './rtcfiles/casu-0' + casuname + '.rtc'

        with open(filename, 'w') as rtc:
            for line in lines:
                rtc.write(line)

