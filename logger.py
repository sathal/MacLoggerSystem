import os, time
from sheetMutator import SheetMutator

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

def get_timestamp():
    # Get the local time
    localtime = time.localtime(time.time())
    print("Local current time :", localtime)

    # Get the desired parts of the local time structure
    dayWeek = daysOfWeek.get(localtime.tm_wday)
    month = monthsOfYear.get(localtime.tm_mon)
    dayName = str(localtime.tm_mday)

    dateString = dayWeek + ", " + month + " " + dayName

    return dateString

#def get_last_login_timestamp():
    #TODO

#def post_timestamp():
    #TODO

def display_timestamp(message, title):
    os.system("terminal-notifier -message \"" + message + "\" -title \"" + title + "\"")




timestamp = get_timestamp()

display_timestamp(timestamp, "Last Login")

mutator = SheetMutator()

mutator.post_timestamp(timestamp)