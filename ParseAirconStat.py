# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 12:23:17 2022

@author: Marco
"""
import AirconStatCoder
import PrintAirconStat
import Debug


# StatString = "AAeqrqT/AAAAAAAQCwAAAAAAAf////8RWoAECCYkjAAAiAAAAAEAAAAAAAOAIIz/gBCf/5QQVQCuFA==" #thing off
# StatString = "AAejv6j/AAAAAAAQCwAAAAAAAf////9QxoAEATcoigAAiAIAAAEAAAAAAAOAIIn/gBCj/5QQAADBug==" #temp 20, thing on
# StatString = "AAfjj7L/AAAAAAAQCwAAAAAAAf////+vbIAEQQcylwAAiAAAAAEAAAAAAAOAIJf/gBCl/5QQAABCcA==" #auto mode 25c
StatString = "AAfnj7L/AAAAAAAQCwAAAAAAAf////8UC4AERQcykwAAiAAAAAEAAAAAAAOAIJP/gBCk/5QQAACM0A==" #dry mode
# StatString = "AAfjj6z/AAAAAAAQCwAAAAAAAf/////MKAAAQQcs/wAAAAAAAAEAAAAAAAH/////mck="

# StatString = "AAfjj6z/AAAAAAAQCwAAAAAAAf/////MKAAAQQcs/wAAAAAAAAEAAAAAAAH/////mck="

global fname 
fname = 'log.txt'
with open(fname, 'w') as f:
    f.write('starting log\n')
    f.write('===========================\n')
    f.close()

Debug.StringToFile(StatString, fname)

ACS = AirconStatCoder.StringtoStat(StatString)
PrintAirconStat.PrintAirconStat(ACS)

Debug.AirconStatToFile(ACS, fname)

OutString = AirconStatCoder.toBase64(ACS)

print(StatString)
print(OutString)

Debug.StringToFile(StatString, fname)
Debug.StringToFile(OutString, fname)