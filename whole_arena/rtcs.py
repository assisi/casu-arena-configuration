fbc1 = "# A Firmware Board Configuratoin (FBC) template file (yaml syntax) \n# Each firmware instance should be run with it's own FBC file \n# FBC naming convention: each beaglebone has 4 FBC files of format casu-00?.fbc: \n#    casu-001.fbc \n#    casu-002.fbc \n#    casu-003.fbc \n#    casu-004.fbc \n# ? used pub_addr, sub_addr, i2c_bus, and i2c_connector \n \n# Name of the CASU that the firmware instance is controlling \n# Casu names defined in Arena_layout_rectangle depending on which beaglebone \n# they are connected. Casu name does not match fbc file name! \nname : casu-0"

fbc2 = "\n \n# Address to publish sensor data from \n# * means \"bind to all interfaces\" \n# this corresponds to the \"sub_addr\" in RTC files \n# ? determined from the fbc name (casu-001.fbc > ? = 1) \npub_addr : tcp://*:"

fbc3 = "555 \n \n# Address from which actuator commands are read \n# Corresponds to the \"pub_addr\" in RTC files \n# ? determined from the fbc name (casu-001.fbc > ? = 1) \nsub_addr : tcp://*:"

fbc4 = "556 \n \n# The number of I2C bus on beaglebone being used for communication. \n# ? = {1, 2} > i2c_bus : 2; ? = {3, 4} > i2c_bus : 1 \ni2c_bus : "

fbc5 = " \n \n# Hardware address on I2C bus \ni2c_addr : 0x11 \n \n# I2C connector on bbg \n# ? corresponds to number in filename \ni2c_connector : "

fbc6 = " \n \n# Flag determines if temp control will run, 1 - on, 0 - off \ntempCtlOn : 1 \n \n# Proportional gain of PI controller \nKp : 10 \n \n# Integral gain of PI controller \nKi : 0.115 \n \n# Weight of current casu ring in computation of discrete PT1 filter for wax tem$ \nKf1 : 0.1029 \n \n# Weight of old casu ring temp in computation of PT1 filter for wax temperature$ \nKf2 : 0.1029 \n \n# Weight of old wax temp in computation of discrete PT1 filter for wax temperat$ \nKf3 : 0.7893 \n \n# Flag determines if fan for cooling casu will runn, 1 - on, 0 - off \nfanCtlOn : 1 \n \n# 0 = PI; 1 = SMC \ncontroller_type : 1 \n \n# Derivative gain \nC1_sigma : 1.0 \n \n# Derivative gain in alpha adaptation \nC2_sigma_m : 1.0 \n \n# Alpha adaptation speed \nK1_alpha : 0.01 \n \n# Beta / alpha relation \nK2_beta : 0.01 \n \n# Deadzone for sigma_m \nepsilon : 0.3 \n \n# Alpha initial condition \nalphak1 : 7.00 \n"

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

content = ['name: casu-0', 'pub_addr: tcp://bbg-0', 'sub_addr: tcp://bbg-0', 'msg_addr: tcp://*:5', 'neighbors:']


for bbg in bbgs.keys():
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

    for casu, iCasu in zip(casus, xrange(len(casus))):
        if (casu != 0) :
            casuname = '0' + str(casu)
            casuname = casuname[-2:]

            bbgname = '0' + str(bbg)
            bbgname = bbgname[-2:]

            lines = []
            lines.append(content[0] + casuname + '\n')
            lines.append(content[1] + bbgname + ':' + str(iCasu + 1) + '556' +'\n')
            lines.append(content[2] + bbgname + ':' + str(iCasu + 1) + '555' +'\n')
            lines.append(content[3] + bbgname + '0' + str(iCasu + 1) + '\n')
            lines.append(content[4] + '\n')

            filename = './rtcfiles/casu-0' + casuname + '.rtc'

            with open(filename, 'w') as rtc:
                for line in lines:
                    rtc.write(line)

            filename = './fbcfiles/bbg-0' + str(bbgname) + '/casu-00' + str(iCasu+1) + '.fbc'

            with open(filename, 'w') as fbc:
                fbc.write(fbc1 + str(casuname) + fbc2 + str(iCasu+1) + fbc3 + str(iCasu+1) + fbc4 + str((1 if iCasu > 1 else 2)) + fbc5 + str(iCasu+1) + fbc6)
