from datetime import datetime
import backend
#import sqlite3
import sqlite3
global StartList
global EndList
global StartListInt
global EndListInt
import MySQLdb

con = MySQLdb.connect(host="pf.parsl.dev", user="hacc", passwd="hacc2019", db='hacc')
#con = sqlite3.connect('shc.db')
con = sqlite3.connect('shc.db')
cursorObj = con.cursor()

global StartList
global EndList

def sql_fetch_StartTimes(con):
    global StartList
"""<<<<<<< HEAD
    cursorObj.execute('SELECT "Start Time" FROM raw')
    StartTime = cursorObj.fetchall()
    StartList = []
    for row in StartTime:
        StartList += row




def sql_fetch_EndTimes(con):
    global EndList
    cursorObj.execute('SELECT "End Time" FROM raw')
    EndTime = cursorObj.fetchall()
    EndList = []
    for row in EndTime:
        EndList += row


#sql_fetch_StartTimes(con)
#sql_fetch_EndTimes(con)
print(StartList)
print(EndList)
#print(sql_fetch_EndTimes(con))
#print(sql_fetch_StartTimes(con))

def convertStartTime():
    global StartList
    for i in StartList:
        ConvertedStart_List = []
        UnixStartTime = datetime.strptime(i, '%m-%d-%Y" "%I:%M:%S')
        UnixStartTime += ConvertedStart_List
        # return int(UnixStartTime.timestamp())
        print(ConvertedStart_List)



"""
    con.query('SELECT Start_Time FROM raw')
    StartTimeResult=con.store_result()
    StartTime=StartTimeResult.fetch_row(maxrows=0)
    StartList=[]
    for row in StartTime:
        StartList.append(str(row))
def sql_fetch_EndTimes(con):
    global EndList
    #EndTime = cursorObj.execute('SELECT End_Time FROM raw')
    con.query('SELECT End_Time FROM raw')
    EndTimeResult = con.store_result()
    EndTime=EndTimeResult.fetch_row(maxrows=0)
    EndList=[]
    for row in EndTime:
        EndList.append(str(row))

sql_fetch_StartTimes(con)
sql_fetch_EndTimes(con)

def unix_Converter():
    global StartListInt
    global EndListInt
    StartListInt=[]
    EndListInt=[]
    for date in StartList:
        try:
            utc = datetime.strptime(date, "('%m-%d-%y %H:%M:%S',)")
            #print(int(utc.timestamp()) - 36000)
            utcint = int(utc.timestamp()) - 36000
            print (utcint)
        except ValueError:
            utc = datetime.strptime(date, "('%m/%d/%Y %H:%M:%S',)")
            #print(int(utc.timestamp()) - 36000)
            utcint = int(utc.timestamp()) - 36000
            print (utcint)
        StartListInt.append(utcint)

    for date in EndList:
        try:
            utc = datetime.strptime(date, "('%m-%d-%y %H:%M:%S',)")
            #print(int(utc.timestamp()) - 36000)
            utcint = int(utc.timestamp()) - 36000
            print (utcint)
        except ValueError:
            utc = datetime.strptime(date,"('%m/%d/%Y %H:%M:%S',)")
            #print(int(utc.timestamp()) - 36000)
            utcint = int(utc.timestamp()) - 36000
            print (utcint)
        EndListInt.append(utcint)
"""(inputtime - starttime)/Unixdays"""
def FindDayIntervals():
    maxTime = backend.findMaxTime(con)
    minTime = backend.findMinTime(con)
    UnixDayValue=86400
    indexes=int((maxTime-minTime)/UnixDayValue)
    TimeIndexes=[]
    for i in range(indexes+1):
        x=minTime+i*UnixDayValue
        TimeIndexes.append(x)
    TimeIndexes.append(maxTime)
    print(TimeIndexes)

unix_Converter()
print(StartListInt)
print(EndListInt)
FindDayIntervals()
