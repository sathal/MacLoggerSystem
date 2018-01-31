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

def get_current_timestamp():
    # Get the local time
    localtime = time.localtime(time.time())
    print("Local current time :", localtime)

    # Get the desired parts of the local time structure
    dayWeek = daysOfWeek.get(localtime.tm_wday)
    month = monthsOfYear.get(localtime.tm_mon)
    dayName = str(localtime.tm_mday)
    hour = str(localtime.tm_hour)
    minute = str(localtime.tm_min)
    second = str(localtime.tm_sec)

    dateString = dayWeek + ", " + month + " " + dayName + " at " + hour + ":" + minute + ":" + second

    return dateString

def display_timestamp(message, title):
    os.system("terminal-notifier -message \"" + message + "\" -title \"" + title + "\"")

# Create the google sheet mutator
mutator = SheetMutator()

# Get the current date/time - we will post this to the google sheet
currentTimestamp = get_current_timestamp()

# Get the previous timestamp
previousTimestamp = mutator.get_previous_timestamp()

display_timestamp(previousTimestamp, "Last Login")

mutator.post_timestamp(currentTimestamp)

