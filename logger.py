import os, time

daysOfWeek = {
    0:"Monday",
    1:"Tuesday",
    2:"Wednesday",
    3:"Thursday",
    4:"Friday",
    5:"Saturday",
    6:"Sunday"
}

monthsOfYear = {
    0:"January",
    1:"February",
    2:"March",
    3:"April",
    4:"May",
    5:"June",
    6:"July",
    7:"August",
    8:"September",
    9:"October",
    10:"November",
    11:"December"
}

#def getTimeStamp():
    #TOD

#def getLastLoginTimeStamp():
    #TODO

#def postTimeStamp():
    #TODO

def displayTimeStamp(message, title):
    os.system("terminal-notifier -message \"" + message + "\" -title \"" + title + "\"")


localtime = time.localtime(time.time())
print("Local current time :", localtime)

dayWeek = daysOfWeek.get(localtime.tm_wday)
month = monthsOfYear.get(localtime.tm_mon)
dayName = str(localtime.tm_mday)

messageString = dayWeek + ", " + month + " " + dayName

displayTimeStamp(messageString, "Last Login")