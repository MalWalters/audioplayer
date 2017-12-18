from classes.books import Book
import time, datetime
import json
#import RPI.GPIO as GPIO

def start():
    #read current bookID
    #print URL
    #print last datetime stamp
    print(currentBookID[0]['currentBookID'])
    currentBookID[0]['currentBookID'] = currentBookID[0]['currentBookID'] + " again|"
    return

def stop():
    #write current date time to library.json (current book)
    return

def switch():
    #update new bookID
    newBook = input("ID of new book: ")
    print(currentBookID)
    with open('json/currentbook.json','w') as outfile:
        json.dump(newBook,outfile)
    return

#load libray, rfid reference table and current book ID from json
with open('json/rfid.json') as data_file:
    rfid = json.load(data_file)

with open('json/library.json') as data_file:
    library = json.load(data_file)

with open('json/currentbook.json') as data_file:
    currentBookID = json.load(data_file)

while True:
    n = input ("Start, Stop, Switch: ")
    if n == "break":
        break
    elif n == "switch":
        switch()
    elif n == "start":
        start()
    elif n == "stop":
        stop()


