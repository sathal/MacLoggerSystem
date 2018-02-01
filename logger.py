import os, time, socket, sys
from sheetMutator import SheetMutator


timeout = 25 #seconds

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

# Returns the current timestamp for this session
def get_current_timestamp():
    # Get the local time
    localtime = time.localtime(time.time())

    # Get the desired parts of the local time structure
    dayWeek = daysOfWeek.get(localtime.tm_wday)
    month = monthsOfYear.get(localtime.tm_mon)
    dayName = str(localtime.tm_mday)
    hour = str(localtime.tm_hour)
    minute = str(localtime.tm_min)
    second = str(localtime.tm_sec)

    dateString = dayWeek + ", " + month + " " + dayName + " at " + hour + ":" + minute + ":" + second

    return dateString

# Displays a notification to the user
def display_notification(message, title):
    os.system("terminal-notifier -message \"" + message + "\" -title \"" + title + "\"")

# Checks for an internet connection
def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

# Wait for an internet connection before proceeding - abort if timeout is reached
while is_connected() == False:
    time.sleep(1)
    timeout -= 1
    if timeout == 0:
        message = "Unable to retreive last login timestamp\nThis login session will not be recorded"
        title = "LOGGER ERROR"
        display_notification(message, title)
        sys.exit()

# Create the google sheet mutator
mutator = SheetMutator()

# Get the current date/time - we will post this to the google sheet
currentTimestamp = get_current_timestamp()

# Get the previous timestamp
previousTimestamp = mutator.get_previous_timestamp()

# Display the last login session's timestamp
display_notification(previousTimestamp, "Last Login")

# Record the timestamp of the current login session
mutator.post_timestamp(currentTimestamp)

