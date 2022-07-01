# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:35:15 2022

@author: Marco
"""
import time, requests
import AirconStatCoder
import PrintAirconStat
import Config

ipWFRAC = Config.ipWFRAC
deviceID = Config.deviceID
operatorId = Config.operatorId
airconID = Config.airconID

BaseURL = "http://" + ipWFRAC + ":51443" + "/beaver/command/"
apiVer = "1.0"

API_GET_AIRCON_STAT                 = BaseURL + "command/getAirconStat"
API_SET_AIRCON_STAT                 = BaseURL + "command/setAirconStat"
API_GET_CALENDAR_STAT               = BaseURL + "server/getCalendarInfo"
API_GET_WEEKLY_TIMER                = BaseURL + "server/getWeeklyTimer"
API_SET_WEEKLY_TIMER                = BaseURL + "server/setWeeklyTimer";
API_CHECK_CALENDAR                  = BaseURL + "server/checkCalendar";
API_SET_CALENDAR_STAT               = BaseURL + "server/setCalendarInfo";
API_REG_AIRCON_ACCOUNT              = BaseURL + "server/setAirconAccount";
API_GET_ELECTRICITY_INFORMATION_ACCOUNT = BaseURL + "server/getConsumption";
API_GET_AIRCON_SETTING              = BaseURL + "server/getAirconSetting";
API_SET_OPTION_SETTING              = BaseURL + "server/setOptionSetting";
API_SET_AIRCON_ACCOUNT              = BaseURL + "server/setAirconAccount";
API_DEL_AIRCON_ACCOUNT              = BaseURL + "server/delAirconAccount";
API_GET_ENDPOINT                    = BaseURL + "wirelesskit/getEndpoint";
API_SEND_FORGOTTEN_MANAGEMENT       = BaseURL + "server/sendForgottenManagement";
API_SET_DEVICE_TOKEN                = BaseURL + "server/setDeviceToken";
API_GET_NOTIFICATION_STAT           = BaseURL + "server/getInformation";
API_GET_DEVICE_INFO                 = BaseURL + "server/getDeviceInfo";
API_GET_FIRMWARE                    = BaseURL + "server/getFirmware";
API_GET_CONSUMPTION                 = BaseURL + "server/getConsumption";
API_SET_AIRCON_NAME                 = BaseURL + "server/setAirconName"
API_MAKE_ACCOUNT                    = BaseURL + "server/makeAccount"
ApiGetAppVersion                    = BaseURL + "server/getAppVersion"
API_GET_AIRCON_FOR_MOVING           = BaseURL + "server/getAirconForMoving"
API_SET_ACCOUNT                     = BaseURL + "server/setAccount";


COMMAND_DELETE_ACCOUNT_INFO = "deleteAccountInfo"
COMMAND_GET_AIRCON_STAT = "getAirconStat"
COMMAND_GET_DEVICE_INFO = "getDeviceInfo"
COMMAND_SET_AIRCON_STAT = "setAirconStat"
COMMAND_SET_NETWORK_INFO = "setNetworkInfo"
COMMAND_SET_OPTION_SETTING = "setOptionSetting"
COMMAND_UPDATE_ACCOUNT_INFO = "updateAccountInfo"
COMMAND_UPDATE_FIRMWARE = "updateFirmware"



def getDeviceInfo():
    treq = int(time.time())
    data = {
        'apiVer' : apiVer,
        'operatorId' : operatorId,
        'timestamp' : treq,
        'command' : COMMAND_GET_DEVICE_INFO,
        'deviceId' : deviceID
    }
    resp = requests.post(url=API_GET_DEVICE_INFO,json=data)
    return resp.json()

def getAirconStat():
    treq = int(time.time())
    contents = {'airconId' : airconID}
    data = {
        'apiVer' : apiVer,
        'operatorId' : operatorId,
        'timestamp' : treq,
        'command' : COMMAND_GET_AIRCON_STAT,
        'deviceId' : deviceID,
        'contents' : contents
    }
    resp = requests.post(url=API_GET_AIRCON_STAT,json=data)
    return resp.json()

DeviceInfo = getDeviceInfo()
airconId = DeviceInfo["contents"]["airconId"]

JSAirconStat = getAirconStat()

PrintAirconStat.PrintAirconStat(AirconStatCoder.StringtoStat(JSAirconStat["contents"]["airconStat"]))
