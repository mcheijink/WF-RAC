# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 11:35:57 2022

@author: Marco
"""
import base64
from AirconStat import AirconStat
import InttoTemp
import Debug
global fname
fname = 'log.txt'

COMMAND_EXTENSION_HOME_LEAVE_MODE_FAN_SPEED_AUTO = 0
COMMAND_EXTENSION_HOME_LEAVE_MODE_FAN_SPEED_VOLUME1 = 3
COMMAND_EXTENSION_HOME_LEAVE_MODE_FAN_SPEED_VOLUME2 = 5
COMMAND_EXTENSION_HOME_LEAVE_MODE_FAN_SPEED_VOLUME3 = 7
COMMAND_EXTENSION_HOME_LEAVE_MODE_FAN_SPEED_VOLUME4 = 14
COMMAND_SELF_CLEAN_RESET_OFF = [0]*18
ELECTRIC_ENERGY_COFFICIENT = 0.25
STATUS_EXTENSION_CODE_HOME_LEAVE_MODE = 248
STATUS_EXTENSION_HOME_LEAVE_MODE_FAN_SPEED_AUTO = 0
STATUS_EXTENSION_HOME_LEAVE_MODE_FAN_SPEED_VOLUME1 = 3
STATUS_EXTENSION_HOME_LEAVE_MODE_FAN_SPEED_VOLUME2 = 5
STATUS_EXTENSION_HOME_LEAVE_MODE_FAN_SPEED_VOLUME3 = 7
STATUS_EXTENSION_HOME_LEAVE_MODE_FAN_SPEED_VOLUME4 = 14
STATUS_EXTENSION_OP1_HOME_LEAVE_MODE_COMMAND = 0
STATUS_EXTENSION_OP1_HOME_LEAVE_MODE_REQUEST = 255
STATUS_EXTENSION_OP1_HOME_LEAVE_MODE_STATUS = 16
STATUS_EXTENSION_OP2_HOME_LEAVE_MODE_FAN_SPEED_FOR_COOLING = 31
STATUS_EXTENSION_OP2_HOME_LEAVE_MODE_FAN_SPEED_FOR_HEATING = 32
STATUS_EXTENSION_OP2_HOME_LEAVE_MODE_TEMP_RULE_FOR_COOLING = 27
STATUS_EXTENSION_OP2_HOME_LEAVE_MODE_TEMP_RULE_FOR_HEATING = 28
STATUS_EXTENSION_OP2_HOME_LEAVE_MODE_TEMP_SETTING_FOR_COOLING = 29
STATUS_EXTENSION_OP2_HOME_LEAVE_MODE_TEMP_SETTING_FOR_HEATING = 30
STATUS_MODEL_NO_TYPE_SEPARATE_2021 = [0]*18
STATUS_OPERATION_MODE2_OFF = [0]*18
STATUS_VACANT_PROPERTY_MAX_BIT = [0]*18
STATUS_VACANT_PROPERTY_OFF = [0]*18
STATUS_VACANT_PROPERTY_ON = [0]*18
TAG = "AirconStatCoder"
zeros = 0
receive_init = [0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
op_n_of = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
op_n_on = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
om_n_au = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    #changed 3th 0 to 2
om_n_jo = [0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
om_n_re = [0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
om_n_so = [0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
om_n_dn = [0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
as_n_of = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
as_n_on = [0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
av_n_of = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
av_n_on = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
lv_n_01 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lv_n_02 = [0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lv_n_03 = [0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lv_n_04 = [0, 0, 0, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lh_n_01 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lh_n_02 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
lh_n_03 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0]
lh_n_04 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
lh_n_05 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0]
lh_n_06 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0]
lh_n_07 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0]
af_n_00 = [0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
af_n_01 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
af_n_02 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
af_n_03 = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
af_n_04 = [0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
en_n_of = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
en_n_on = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0]
STATUS_MODEL_NO_TYPE_GLOBAL_2022 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
STATUS_MODEL_NO_TYPE_HIGH_END_FOR_JAPANESE_2023 = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
STATUS_MODEL_NO_TYPE_MAX_BIT = [127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
STATUS_OPERATION_MODE2_ON = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
STATUS_OPERATION_MODE2_MAX_BIT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0]
command_init = [0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
as_p_of = [0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
as_p_on = [0, 0, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
om_p_au = [0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
om_p_jo = [0, 0, 36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
om_p_re = [0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
om_p_so = [0, 0, 44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
om_p_dn = [0, 0, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
op_p_of = [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
op_p_on = [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lv_p_01 = [0, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lv_p_02 = [0, 0, 0, 144, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lv_p_03 = [0, 0, 0, 160, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lv_p_04 = [0, 0, 0, 176, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
af_p_00 = [0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
af_p_01 = [0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
af_p_02 = [0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
af_p_03 = [0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
af_p_04 = [0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tm_p_no = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tm_p_au = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
lh_p_01 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0]
lh_p_02 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0]
lh_p_03 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0]
lh_p_04 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0]
lh_p_05 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0]
lh_p_06 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0]
lh_p_07 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0]
av_p_of = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]
av_p_on = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]
en_p_of = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0]
en_p_on = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0]
COMMAND_VACANT_PROPERTY_OFF = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
COMMAND_VACANT_PROPERTY_ON = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
COMMAND_SELF_CLEAN_RESET_ON = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0]
COMMAND_OPERATION_MODE2_OFF = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 0, 0, 0]
COMMAND_OPERATION_MODE2_ON = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 144, 0, 0, 0, 0, 0]

def andBytes(abytes, bbytes):
    return bytes([a & b for a, b in zip(abytes[::-1], bbytes[::-1])][::-1])

def orBytes(abytes, bbytes):
    return bytes([a | b for a, b in zip(abytes[::-1], bbytes[::-1])][::-1])

def maskedStat(mask,byteStat):
    return andBytes(bytes(mask), byteStat)

def checkMode(modeDef,byteStat):
    return bytes(modeDef)==byteStat

def StringtoStat(StatString):
    airconStat = AirconStat()
    v_MAX_VALUE = -1;
    StatByte = base64.b64decode(StatString.replace("\n", ""))
    
    Debug.BytesToFile(StatByte, "Decoded AirconStat", fname)
    
    # print(StatByte[18])
    i5 = (StatByte[18]&v_MAX_VALUE)*4 + 21
    # i5 = (StatByte[18]&v_MAX_VALUE)*4 + 2
    # print(i5)
    wrap2 = StatByte[i5:i5+18]
    copyOfRange = StatByte[i5+19:len(StatByte)-2]
    
    Debug.BytesToFile(wrap2, "wrap2", fname)
    
    opMask = [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Debug.BytesToFile(bytes(opMask), "opMask", fname)
    Debug.BytesToFile(maskedStat(opMask,wrap2), "opMasked", fname)
    if checkMode(op_n_on,maskedStat(opMask,wrap2)):
        airconStat.operation = 1
    else:
        airconStat.operation = 0
    
    airconStat.presetTemp = (wrap2[4]&v_MAX_VALUE)/2.0
    # print((wrap2[4]&v_MAX_VALUE)/2.0)
    opModeMask = [0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Debug.BytesToFile(bytes(opModeMask), "opModeMask", fname)
    opBytes = maskedStat(opModeMask,wrap2)
    
    Debug.BytesToFile(bytes(om_n_au), "om_n_au", fname)
    if checkMode(om_n_au,opBytes):
        airconStat.operationMode = 0    #auto                    
    elif checkMode(om_n_re,opBytes): 
        airconStat.operationMode = 1    #cool
    elif checkMode(om_n_dn,opBytes):
        airconStat.operationMode = 2    #hot
    elif checkMode(om_n_so,opBytes):
        airconStat.operationMode = 3    #sendair
    elif checkMode(om_n_jo,opBytes):
        airconStat.operationMode = 4    #dry
    
    # Airflow 
    afMask = [0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Debug.BytesToFile(bytes(afMask), "afMask", fname)
    airflowBytes = maskedStat(afMask,wrap2)
    Debug.BytesToFile(airflowBytes, "afBytes", fname)
    Debug.BytesToFile(bytes(af_n_00), "afBytes0", fname)
    Debug.BytesToFile(bytes(af_n_01), "afBytes1", fname)
    Debug.BytesToFile(bytes(af_n_02), "afBytes2", fname)
    Debug.BytesToFile(bytes(af_n_03), "afBytes3", fname)
    Debug.BytesToFile(bytes(af_n_04), "afBytes4", fname)
    if checkMode(af_n_00,airflowBytes):
        airconStat.airFlow = 0
    elif checkMode(af_n_01,airflowBytes):
        airconStat.airFlow = 1
    elif checkMode(af_n_02,airflowBytes):
        airconStat.airFlow = 2
    elif checkMode(af_n_03,airflowBytes):
        airconStat.airFlow = 3        
    elif checkMode(af_n_04,airflowBytes):
        airconStat.airFlow = 4
    
    # Vertical wind direction
    VDAutoMask = [0, 0, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Debug.BytesToFile(bytes(VDAutoMask), "VDAutoMask", fname)
    if checkMode(as_n_on,maskedStat(VDAutoMask,wrap2)):
        airconStat.windDirectionUD = 0
    else:
        UDmodeMask = [0, 0, 0, 240, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Debug.BytesToFile(bytes(UDmodeMask), "UDmodeMask", fname)
        UDwindBytes = maskedStat(UDmodeMask, wrap2)
        if checkMode(lv_n_01,UDwindBytes):
            airconStat.windDirectionUD = 1
        elif checkMode(lv_n_02,UDwindBytes):
            airconStat.windDirectionUD = 2
        elif checkMode(lv_n_03,UDwindBytes):
            airconStat.windDirectionUD = 3
        elif checkMode(lv_n_04,UDwindBytes):
            airconStat.windDirectionUD = 4
    
    # Horizontal wind direction
    HDAutoMask = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]
    Debug.BytesToFile(bytes(HDAutoMask), "HDAutoMask", fname)
    if checkMode(av_n_on,maskedStat(HDAutoMask,wrap2)):
        airconStat.windDirectionLR = 0
    else:
        LRmodeMask = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0]
        Debug.BytesToFile(bytes(LRmodeMask), "LRmodeMask", fname)
        LRwindBytes = maskedStat(LRmodeMask, wrap2)
        if checkMode(lh_n_01,LRwindBytes):
            airconStat.windDirectionLR = 1
        elif checkMode(lh_n_02,LRwindBytes):
            airconStat.windDirectionLR = 2
        elif checkMode(lh_n_03,LRwindBytes):
            airconStat.windDirectionLR = 3
        elif checkMode(lh_n_04,LRwindBytes):
            airconStat.windDirectionLR = 4
        elif checkMode(lh_n_05,LRwindBytes):
            airconStat.windDirectionLR = 5
        elif checkMode(lh_n_06,LRwindBytes):
            airconStat.windDirectionLR = 6
        elif checkMode(lh_n_07,LRwindBytes):
            airconStat.windDirectionLR = 7
    
    # Entrust?
    EntrustMask = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0]
    Debug.BytesToFile(bytes(EntrustMask), "EntrustMask", fname)
    entrustBytes = maskedStat(EntrustMask,wrap2)
    if checkMode(en_n_of,entrustBytes):
        airconStat.entrust = 0
    elif checkMode(en_n_on,entrustBytes):
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
        airconStat.errorCode = "M%s" % i2
    else:
        airconStat.errorCode = "E%s" % i2
    if i2 == 0:
        airconStat.errorCode = "00"
    
    # CoolHotJudge
    if (wrap2[8]&8)<=0:
        airconStat.coolHotJudge = 1
    else:
        airconStat.coolHotJudge = 0
    
    # ModelNo
    modelBytes = maskedStat(STATUS_MODEL_NO_TYPE_MAX_BIT,wrap2)
    if not checkMode(STATUS_MODEL_NO_TYPE_SEPARATE_2021,modelBytes):
        airconStat.modelNo = 0
    elif checkMode(STATUS_MODEL_NO_TYPE_GLOBAL_2022,modelBytes):
        airconStat.modelNo = 1
    elif checkMode(STATUS_MODEL_NO_TYPE_HIGH_END_FOR_JAPANESE_2023,modelBytes):
        airconStat.modelNo = 2
    
    # Vacant
    vacantBytes = maskedStat(STATUS_OPERATION_MODE2_MAX_BIT,wrap2)
    if not checkMode(STATUS_OPERATION_MODE2_OFF,vacantBytes):
        airconStat.isSelfCleanOperation = False
    elif checkMode(STATUS_OPERATION_MODE2_ON,vacantBytes):
        airconStat.isSelfCleanOperation = True
    
    Debug.BytesToFile(copyOfRange, "copyOfRange", fname)
    
    # Convert the temp bytes. Originally a lookup table is used. Here a polynominal fit is used.
    for i3 in range(int(len(copyOfRange)/4)):
        i9 = i3*4
        b1 = copyOfRange[i9]
        b2 = copyOfRange[i9+1]
        b3 = copyOfRange[i9+2]
        b4 = copyOfRange[i9+3]
        if b1==128 and b2==16:
            airconStat.outdoorTemp=round(InttoTemp.OutsideTemp(b3),1)
        elif b1==128 and b2==32:
            airconStat.indoorTemp=round(InttoTemp.InsideTemp(b3),1)
    return airconStat

def CommandtoByte(airconStat):
    
    InitByte = bytes(command_init)
    
    # On/Off
    if airconStat.operation:
        StatByte = orBytes(InitByte,bytes(op_p_on))
    else:
        StatByte = orBytes(InitByte,bytes(op_p_of))
    
    #Operating Mode
    if airconStat.operationMode == 0:
        StatByte = orBytes(StatByte,bytes(om_p_au))
    elif airconStat.operationMode == 1:
        StatByte = orBytes(StatByte,bytes(om_p_re))
    elif airconStat.operationMode == 2:
        StatByte = orBytes(StatByte,bytes(om_p_dn))
    elif airconStat.operationMode == 3:
        StatByte = orBytes(StatByte,bytes(om_p_so))
    elif airconStat.operationMode == 4:
        StatByte = orBytes(StatByte,bytes(om_p_jo))
        
    #airflow
    if airconStat.airFlow == 0:
        StatByte = orBytes(StatByte,bytes(af_p_00))
    elif airconStat.airFlow == 1:
        StatByte = orBytes(StatByte,bytes(af_p_01))
    elif airconStat.airFlow == 2:
        StatByte = orBytes(StatByte,bytes(af_p_02))
    elif airconStat.airFlow == 3:
        StatByte = orBytes(StatByte,bytes(af_p_03))
    elif airconStat.airFlow == 4:
        StatByte = orBytes(StatByte,bytes(af_p_04))        
        
    # Vertical wind direction
    if airconStat.windDirectionUD == 0:
        StatByte = orBytes(orBytes(StatByte,bytes(as_p_on)),bytes(lv_p_01))
    elif airconStat.windDirectionUD == 1:
        StatByte = orBytes(orBytes(StatByte,bytes(as_p_of)),bytes(lv_p_01))
    elif airconStat.windDirectionUD == 2:
        StatByte = orBytes(orBytes(StatByte,bytes(as_p_of)),bytes(lv_p_02))
    elif airconStat.windDirectionUD == 3:
        StatByte = orBytes(orBytes(StatByte,bytes(as_p_of)),bytes(lv_p_03))
    elif airconStat.windDirectionUD == 4:
        StatByte = orBytes(orBytes(StatByte,bytes(as_p_of)),bytes(lv_p_04))
        
    # Horizontal wind direction
    if airconStat.windDirectionLR == 0:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_on)),bytes(lh_p_01))
    elif airconStat.windDirectionLR == 1:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_01))
    elif airconStat.windDirectionLR == 2:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_02))
    elif airconStat.windDirectionLR == 3:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_03))
    elif airconStat.windDirectionLR == 4:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_04))
    elif airconStat.windDirectionLR == 5:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_05))
    elif airconStat.windDirectionLR == 6:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_06))
    elif airconStat.windDirectionLR == 7:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_07))
    
    
    #preset temp
    presetTemp = 25.0 if airconStat.operationMode == 3 else airconStat.presetTemp
    iArr = [0]*18
    iArr[4] = int(presetTemp/0.5) + 128
    StatByte = orBytes(StatByte,bytes(iArr))
    
    #entrust
    if airconStat.entrust:
        StatByte = orBytes(StatByte,bytes(en_p_on))
    else:
        StatByte = orBytes(StatByte,bytes(en_p_of))
    
    if airconStat.modelNo == 1:
        StatByte = orBytes(StatByte,bytes(COMMAND_VACANT_PROPERTY_ON if airconStat.isVacantProperty else COMMAND_VACANT_PROPERTY_OFF))
        
    if airconStat.modelNo == 1 | airconStat.modelNo == 2:
        SCByte = orBytes(bytes(COMMAND_SELF_CLEAN_RESET_ON if airconStat.isSelfCleanReset else COMMAND_SELF_CLEAN_RESET_ON), \
                         bytes(COMMAND_OPERATION_MODE2_ON if airconStat.isSelfCleanOperation else COMMAND_OPERATION_MODE2_OFF))
        StatByte = orBytes(StatByte,SCByte)
    return StatByte

def RecievetoByte(airconStat):
    
    InitByte = bytes(receive_init)
    
    # On/Off
    if airconStat.operation:
        StatByte = orBytes(InitByte,bytes(op_p_on))
    else:
        StatByte = orBytes(InitByte,bytes(op_p_of))
    
    #Operating Mode
    if airconStat.operationMode == 0:
        StatByte = orBytes(StatByte,bytes(om_p_au))
    elif airconStat.operationMode == 1:
        StatByte = orBytes(StatByte,bytes(om_p_re))
    elif airconStat.operationMode == 2:
        StatByte = orBytes(StatByte,bytes(om_p_dn))
    elif airconStat.operationMode == 3:
        StatByte = orBytes(StatByte,bytes(om_p_so))
    elif airconStat.operationMode == 4:
        StatByte = orBytes(StatByte,bytes(om_p_jo))
        
    #airflow
    if airconStat.airFlow == 0:
        StatByte = orBytes(StatByte,bytes(af_p_00))
    elif airconStat.airFlow == 1:
        StatByte = orBytes(StatByte,bytes(af_p_01))
    elif airconStat.airFlow == 2:
        StatByte = orBytes(StatByte,bytes(af_p_02))
    elif airconStat.airFlow == 3:
        StatByte = orBytes(StatByte,bytes(af_p_03))
    elif airconStat.airFlow == 4:
        StatByte = orBytes(StatByte,bytes(af_p_04))        
        
    # Vertical wind direction
    if airconStat.windDirectionUD == 0:
        StatByte = orBytes(orBytes(StatByte,bytes(as_p_on)),bytes(lv_p_01))
    elif airconStat.windDirectionUD == 1:
        StatByte = orBytes(orBytes(StatByte,bytes(as_p_of)),bytes(lv_p_01))
    elif airconStat.windDirectionUD == 2:
        StatByte = orBytes(orBytes(StatByte,bytes(as_p_of)),bytes(lv_p_02))
    elif airconStat.windDirectionUD == 3:
        StatByte = orBytes(orBytes(StatByte,bytes(as_p_of)),bytes(lv_p_03))
    elif airconStat.windDirectionUD == 4:
        StatByte = orBytes(orBytes(StatByte,bytes(as_p_of)),bytes(lv_p_04))
        
    # Horizontal wind direction
    if airconStat.windDirectionLR == 0:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_on)),bytes(lh_p_01))
    elif airconStat.windDirectionLR == 1:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_01))
    elif airconStat.windDirectionLR == 2:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_02))
    elif airconStat.windDirectionLR == 3:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_03))
    elif airconStat.windDirectionLR == 4:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_04))
    elif airconStat.windDirectionLR == 5:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_05))
    elif airconStat.windDirectionLR == 6:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_06))
    elif airconStat.windDirectionLR == 7:
        StatByte = orBytes(orBytes(StatByte,bytes(av_p_of)),bytes(lh_p_07))
    
    
    #preset temp
    presetTemp = 25.0 if airconStat.operationMode == 3 else airconStat.presetTemp
    iArr = [0]*18
    iArr[4] = int(presetTemp/0.5) + 128
    StatByte = orBytes(StatByte,bytes(iArr))
    
    #entrust
    if airconStat.entrust:
        StatByte = orBytes(StatByte,bytes(en_p_on))
    else:
        StatByte = orBytes(StatByte,bytes(en_p_of))
        
    if airconStat.modelNo == 1:
        StatByte = orBytes(StatByte,bytes(STATUS_MODEL_NO_TYPE_GLOBAL_2022))
    elif airconStat.modelNo == 2:
        StatByte = orBytes(StatByte,bytes(STATUS_MODEL_NO_TYPE_SEPARATE_2021)) 
    else:
        StatByte = orBytes(StatByte,bytes(STATUS_MODEL_NO_TYPE_HIGH_END_FOR_JAPANESE_2023))
    
    if airconStat.modelNo == 1:
        StatByte = orBytes(StatByte,bytes(COMMAND_VACANT_PROPERTY_ON if airconStat.isVacantProperty else COMMAND_VACANT_PROPERTY_OFF))
        
    if airconStat.modelNo == 1 | airconStat.modelNo == 2:
        StatByte = orBytes(StatByte,bytes(COMMAND_OPERATION_MODE2_ON if airconStat.isSelfCleanOperation else COMMAND_OPERATION_MODE2_OFF))
    return StatByte

def addCommandVariableData(ByteBuffer):#, airconStat):
    #this function will need some work since it defines functionality for rule based cooling and heating. Will not implement it for now.
    ByteBufferCVD =  ByteBuffer + bytes([1, 255, 255, 255, 255])
    return ByteBufferCVD

def addRecieveVariableData(ByteBuffer):#, airconStat):
    #this function will need some work since it defines functionality for rule based cooling and heating. Will not implement it for now.
    ByteBufferRVD =  ByteBuffer + bytes([1, 255, 255, 255, 255])
    return ByteBufferRVD

def crc16ccitt(data):
    i = 65535
    for b in data[::-1]:
        for i2 in range(8):
            z = True
            z2 = ((b>> (7-i2)) & 1) == 1
            if ((( i >> 15) & 1) != 1):
                z = False
            i = i << 1
            if (z2 ^z):
                i ^= 4129
    return i & 65535

    
def addCrc16(ByteBuffer):
    # print(ByteBuffer)
    crc =  crc16ccitt(ByteBuffer)
    # print(crc)
    BBcrc16 = ByteBuffer + crc.to_bytes(2, 'big')
    
    return BBcrc16

def toBase64(airconStat):
    CB = addCrc16(addCommandVariableData(CommandtoByte(airconStat)))
    RB = addCrc16(addRecieveVariableData(RecievetoByte(airconStat)))
    Debug.BytesToFile(CB, "CB", fname)
    Debug.BytesToFile(RB, "RB", fname)
    # print(CB)
    # print(RB)
    ES = str(base64.b64encode((CB+RB)))
    return ES[2:-1]