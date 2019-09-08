#!/usr/bin/python3

import configparser


def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

config = configparser.ConfigParser()

config
config.read("gonet.ini")
config.sections()


raspistill_ss = ConfigSectionMap("Camera")['image_time']
print(raspistill_ss)

ISO_X = ConfigSectionMap("Camera")['iso']
print(ISO_X)

awb = ConfigSectionMap("Camera")['white_balance']
print(awb)

raspistill_tl = ConfigSectionMap("Camera")['total_time']
print(raspistill_tl)

junk_test= ConfigSectionMap("Camera")['junk']
print(junk_test)

