import backend
import MySQLdb

def chargeCHADUsages(db, startTime, endTime, stationName):
    rowDataList = backend.gatherRows(startTime, endTime, db)

    CHADData = 0
    for row in rowDataList:
        if row[0] == stationName:
            if row[6] == 'CHADEMO':
                CHADData += 1
            elif row[6] == 'DCCOMBOTYP1':
                pass
            else:
                print("new charger type: {}".format(row[6]))
    #print(CHADData)
    return CHADData

def chargeDCCUsages(db, startTime, endTime, stationName):
    rowDataList = backend.gatherRows(startTime, endTime, db)

    DCCData = 0
    for row in rowDataList:
        if row[0] == stationName:
            if row[6] == 'DCCOMBOTYP1':
                DCCData += 1
            elif row[6] == 'CHADEMO':
                pass
            else:
                print("new charger type: {}".format(row[6]))
    #print(DCCData)
    return DCCData


#startTime = backend.findMinTime(backend.con)[0][0]
#endTime = backend.findMaxTime(backend.con)[0][0]


def findUsageAverage(starttime, endtime, stationName):
    timeInterval=endtime-starttime
    if (chargeCHADUsages(backend.con, starttime, endtime, stationName) == 0) and (chargeDCCUsages(backend.con, starttime, endtime, "B") == 0):
        print("From " + str(starttime) + " to " + str(endtime) + " (" + str(round(timeInterval/86400.0, 3)) + " days), both chargers appear to be broken.")
    elif chargeCHADUsages(backend.con, starttime, endtime, stationName) == 0:
        print("From " + str(starttime) + " to " + str(endtime) + " (" + str(round(timeInterval/86400.0, 3)) + " days), the CHADEMO charger appears to be broken.")
    elif chargeDCCUsages(backend.con, starttime, endtime, stationName) == 0:
        print("From " + str(starttime) + " to " + str(endtime) + " (" + str(round(timeInterval/86400.0, 3)) + " days), the DCCOMBOTYP1 charger appears to be broken.")
    else:
        print("From " + str(starttime) + " to " + str(endtime) + " (" + str(round(timeInterval/86400.0, 3)) + " days), both chargers are being used.")


findUsageAverage(1535872308, 1538139261, "B")