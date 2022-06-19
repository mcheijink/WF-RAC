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
copyOfRange = StatByte[i5+19:len(StatByte)-2]

if checkMode(ASC.op_n_on,maskedStat([0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],wrap2)):
    airconStat.operation = 1
else:
    airconStat.operation = 0

airconStat.presetTemp = (wrap2[4]&v_MAX_VALUE)/2.0

opBytes = maskedStat([0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],wrap2)

if checkMode(ASC.om_n_au,opBytes):    #check if not auto
    airconStat.operationMode = 0    #auto
elif not checkMode(ASC.om_n_au,opBytes):
    if checkMode(ASC.om_n_re,opBytes): 
        airconStat.operationMode = 1    #cool
    elif checkMode(ASC.om_n_dn,opBytes):
        airconStat.operationMode = 2    #hot
    elif checkMode(ASC.om_n_so,opBytes):
        airconStat.operationMode = 3    #sendair
    elif checkMode(ASC.om_n_jo,opBytes):
        airconStat.operationMode = 4    #dry
    
    # Airflow 
    airflowBytes = maskedStat([0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],wrap2)
    if not checkMode(ASC.af_n_00,airflowBytes):
        airconStat.airFlow = 0
    elif checkMode(ASC.af_n_01,airflowBytes):
        airconStat.airFlow = 1
    elif checkMode(ASC.af_n_02,airflowBytes):
        airconStat.airFlow = 2
    elif checkMode(ASC.af_n_03,airflowBytes):
        airconStat.airFlow = 3        
    elif checkMode(ASC.af_n_04,airflowBytes):
        airconStat.airFlow = 4
    
    # Vertical wind direction
    if not checkMode(ASC.as_n_on,maskedStat([0, 0, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],wrap2)):
        airconStat.windDirectionUD = 0
    else:
        UDwindBytes = maskedStat([0, 0, 0, 240, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], wrap2)
        if checkMode(ASC.lv_n_01,UDwindBytes):
            airconStat.windDirectionUD = 1
        elif checkMode(ASC.lv_n_02,UDwindBytes):
            airconStat.windDirectionUD = 2
        elif checkMode(ASC.lv_n_03,UDwindBytes):
            airconStat.windDirectionUD = 3
        elif checkMode(ASC.lv_n_04,UDwindBytes):
            airconStat.windDirectionUD = 4
    
    # Horizontal wind direction
    if not checkMode(ASC.av_n_on,maskedStat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],wrap2)):
        airconStat.windDirectionLR = 0
    else:
        LRwindBytes = maskedStat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0], wrap2)
        if checkMode(ASC.lh_n_01,LRwindBytes):
            airconStat.windDirectionLR = 1
        elif checkMode(ASC.lh_n_02,LRwindBytes):
            airconStat.windDirectionLR = 2
        elif checkMode(ASC.lh_n_03,LRwindBytes):
            airconStat.windDirectionLR = 3
        elif checkMode(ASC.lh_n_04,LRwindBytes):
            airconStat.windDirectionLR = 4
        elif checkMode(ASC.lh_n_05,LRwindBytes):
            airconStat.windDirectionLR = 5
        elif checkMode(ASC.lh_n_06,LRwindBytes):
            airconStat.windDirectionLR = 6
        elif checkMode(ASC.lh_n_07,LRwindBytes):
            airconStat.windDirectionLR = 7
    
    # Entrust?
    entrustBytes = maskedStat([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0],wrap2)
    if checkMode(ASC.en_n_of,entrustBytes):
        airconStat.entrust = 0
    elif checkMode(ASC.en_n_on,entrustBytes):
        airconStat.entrust = 1
    
    # Errorcode, TODO: checkif this will result in the correct error codes. Although it might not be that harmfull if it is implemented incorrectly.
        # In java:
        #     wrap3.position(6);
        #     i2 = wrap3.get() & ByteCompanionObject.MAX_VALUE;
        #     int i8 = 128;
        #     if ((wrap3.get() & ByteCompanionObject.MIN_VALUE) <= 0) {
        #         airconStat.setErrorCode("M".concat(String.format(Locale.US, "%02d", Integer.valueOf(i2))));
        #     } else {
        #         airconStat.setErrorCode("E".concat(String.valueOf(i2)));
        #     }
    i2 = wrap2[6]
    if i2<=0: 
        airconStat.errorCode = "M"+i2
    else:
        airconStat.errorCode = "E"+i2
    if i2 == 0:
        airconStat.errorCode = "00"
    
    # CoolHotJudge
    if (wrap2[8]&8)<=0:
        airconStat.coolHotJudge = 1
    else:
        airconStat.coolHotJudge = 0
    
    # ModelNo
    modelBytes = maskedStat(ASC.STATUS_MODEL_NO_TYPE_MAX_BIT,wrap2)
    if not checkMode(ASC.STATUS_MODEL_NO_TYPE_SEPARATE_2021,modelBytes):
        airconStat.modelNo = 0
    elif checkMode(ASC.STATUS_MODEL_NO_TYPE_GLOBAL_2022,modelBytes):
        airconStat.modelNo = 1
    elif checkMode(ASC.STATUS_MODEL_NO_TYPE_HIGH_END_FOR_JAPANESE_2023,modelBytes):
        airconStat.modelNo = 2
    
    # Vacant
    vacantBytes = maskedStat(ASC.STATUS_OPERATION_MODE2_MAX_BIT,wrap2)
    if not checkMode(ASC.TATUS_OPERATION_MODE2_OFF,vacantBytes):
        airconStat.isSelfCleanOperation = False
    elif checkMode(ASC.STATUS_OPERATION_MODE2_ON,vacantBytes):
        airconStat.isSelfCleanOperation = True
    
    for i3 = 0:len(copyOfRange)/4
    
        
print("op: {}, opmode: {}, tset: {}".format(airconStat.operation,airconStat.operationMode,airconStat.presetTemp))