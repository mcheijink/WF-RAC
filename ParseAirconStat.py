# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 12:23:17 2022

@author: Marco
"""
import Constants
import base64
import AirconStatCoder as ASC
import AirconStat

def andBytes(abytes, bbytes):
    return bytes([a & b for a, b in zip(abytes[::-1], bbytes[::-1])][::-1])

def maskedStat(mask,byteStat):
    return andBytes(bytes(mask), byteStat)

def checkMode(modeDef,byteStat):
    return bytes(modeDef)==byteStat

v_MAX_VALUE = -1;
airconStat = AirconStat.AirconStat()

# StatString = "AAeqrqT/AAAAAAAQCwAAAAAAAf////8RWoAECCYkjAAAiAAAAAEAAAAAAAOAIIz/gBCf/5QQVQCuFA==" #thing off
# StatString = "AAejv6j/AAAAAAAQCwAAAAAAAf////9QxoAEATcoigAAiAIAAAEAAAAAAAOAIIn/gBCj/5QQAADBug==" #temp 20, thing on
# StatString = "AAfjj7L/AAAAAAAQCwAAAAAAAf////+vbIAEQQcylwAAiAAAAAEAAAAAAAOAIJf/gBCl/5QQAABCcA==" #auto mode 25c
StatString = "AAfnj7L/AAAAAAAQCwAAAAAAAf////8UC4AERQcykwAAiAAAAAEAAAAAAAOAIJP/gBCk/5QQAACM0A==" #dry mode
# StatString = "AAfjj6z/AAAAAAAQCwAAAAAAAf/////MKAAAQQcs/wAAAAAAAAEAAAAAAAH/////mck="

StatByte = base64.b64decode(StatString.replace("\n", ""))

i5 = (StatByte[18]&v_MAX_VALUE)*4 + 21
wrap2 = StatByte[i5:i5+18]
copyOfRange = StatByte[i5+19:len(StatByte)]

i6 = 1




if checkMode(ASC.op_n_on,maskedStat([0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],wrap2)):
    airconStat.operation = 1
else:
    airconStat.operation = 0

airconStat.presetTemp = (wrap2[4]&v_MAX_VALUE)/2.0

opBytes = maskedStat([0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],wrap2)

if checkMode(ASC.om_n_au,opBytes):    #check if not auto
    airconStat.operationMode = 0    #auto
elif not checkMode(ASC.om_n_au,opBytes):
    if checkMode(ASC.om_n_re,wrap2): 
        airconStat.operationMode = 1    #cool
    elif checkMode(ASC.om_n_dn,opBytes):
        airconStat.operationMode = 2    #hot
    elif checkMode(ASC.om_n_so,opBytes):
        airconStat.operationMode = 3    #sendair
    elif checkMode(ASC.om_n_jo,opBytes):
        airconStat.operationMode = 4    #dry


print("op: {}, opmode: {}, tset: {}".format(airconStat.operation,airconStat.operationMode,airconStat.presetTemp))