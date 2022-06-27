# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 08:02:42 2022

@author: Marco
"""


def BytesToFile(ByteStream,name,filename):
    with open(filename, 'a') as f:
        string = ''
        for a in zip(ByteStream):
            binstring = bin(256+a[0])
            string += str(binstring[3:]+ " ")
        string += "\t \t" + name +"\n"
        f.write(string)
    f.close()
    
def StringToFile(String,filename):
    with open(filename, 'a') as f:
        f.write(String+"\n")
    f.close()
    
def AirconStatToFile(AirconStat,filename):
    with open(filename, 'a') as f:
         f.write("airFlow \t\t: %s\n" % AirconStat.airFlow)
         f.write("canHomeLeaveMode: %s\n" % AirconStat.canHomeLeaveModeStatusRequest)
         f.write("coolHotJudge \t: %s\n" % AirconStat.coolHotJudge)
         f.write("electric \t\t: %s\n" % AirconStat.electric)
         f.write("entrust \t\t: %s\n" % AirconStat.entrust)
         f.write("errorCode \t\t: %s\n" % AirconStat.errorCode)
         #homeLeaveModeForCooling = null
         #homeLeaveModeForHeating = null
         f.write("indoorTemp \t\t: %s\n" % AirconStat.indoorTemp)
         f.write("isAutoHeating \t: %s\n" % AirconStat.isAutoHeating)
         f.write("isSelfCleanOpera: %s\n" % AirconStat.isSelfCleanOperation)
         f.write("isSelfCleanReset: %s\n" % AirconStat.isSelfCleanReset)
         f.write("isVacantProperty: %s\n" % AirconStat.isVacantProperty)
         f.write("modelNo \t\t: %s\n" % AirconStat.modelNo)
         f.write("operation \t\t: %s\n" % AirconStat.operation)
         f.write("operationMode \t: %s\n" % AirconStat.operationMode)
         f.write("outdoorTemp \t: %s\n" % AirconStat.outdoorTemp)
         f.write("presetTemp \t\t: %s\n" % AirconStat.presetTemp)
         f.write("windDirectionLR : %s\n" % AirconStat.windDirectionLR)
         f.write("windDirectionUD : %s\n" % AirconStat.windDirectionUD)
         f.close()