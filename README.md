## Synopsis

This system tracks user logins. When a user logs in to the computer the previous login timestamp is retrieved from the 
Google Sheet and displayed to the user and the current login timestamp is posted to the Google Sheet.

## Dependency

This program was created to run with Python 3

## Motivation

Practice using Google Sheets Python API.

## Getting Python application to fire on login

I created an app in AppleScript using the Automator.app utiliy and set this app to be called on Login by going to 
SYSTEM PREFERENCES -> USERS & GROUPS -> LOGIN ITEMS and adding my custom AppleScript app to the list of login items.

The AppleScript app is used to call the python code. The AppleScript code can be seen in the AppleScriptCode.txt file.
