# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:31:08 2022

@author: Marco
"""
def PrintAirconStat(AirconStat):
     print("airFlow \t\t: %s" % AirconStat.airFlow)
     print("canHomeLeaveMode: %s" % AirconStat.canHomeLeaveModeStatusRequest)
     print("coolHotJudge \t: %s" % AirconStat.coolHotJudge)
     print("electric \t\t: %s" % AirconStat.electric)
     print("entrust \t\t: %s" % AirconStat.entrust)
     print("errorCode \t\t: %s" % AirconStat.errorCode)
     #homeLeaveModeForCooling = null
     #homeLeaveModeForHeating = null
     print("indoorTemp \t\t: %s" % AirconStat.indoorTemp)
     print("isAutoHeating \t: %s" % AirconStat.isAutoHeating)
     print("isSelfCleanOpera: %s" % AirconStat.isSelfCleanOperation)
     print("isSelfCleanReset: %s" % AirconStat.isSelfCleanReset)
     print("isVacantProperty: %s" % AirconStat.isVacantProperty)
     print("modelNo \t\t: %s" % AirconStat.modelNo)
     print("operation \t\t: %s" % AirconStat.operation)
     print("operationMode \t: %s" % AirconStat.operationMode)
     print("outdoorTemp \t: %s" % AirconStat.outdoorTemp)
     print("presetTemp \t\t: %s" % AirconStat.presetTemp)
     print("windDirectionLR : %s" % AirconStat.windDirectionLR)
     print("windDirectionUD : %s" % AirconStat.windDirectionUD)