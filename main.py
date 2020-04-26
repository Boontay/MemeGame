import os
import sys
import csv
import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [
    [sg.Text('Some text on row 1')],
    [sg.Text('Enter something on Row 2'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')]
]
window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    print('You entered ', values[0])

window.close()
# entries = os.listdir("data/")
# i = 0
# for entry in entries:
#     i += 1
#     print(i, ":", entry[0:entry.index('.csv')])
#
# try:
#     fileOption = int(input("Type in the number relating to the character that you would like to play. [Press ENTER to continue after entering the value]: "))
#     filename = "data/" + entries[fileOption - 1]
#     with open(filename, "r") as csvfile:
#         csvreader = csv.reader(csvfile, delimiter=',')
#         j = 0
#         for lines in csvreader:
#             j += 1
#             print(j, ":", lines[0])
#     option = int(input("Type in the number relating to the option that you would like to play. [Press ENTER to continue after entering the value]: "))
#     with open(filename, "r") as csvfile:
#         csvreader = csv.reader(csvfile, delimiter=',')
#         rows = list(csvreader)
#         print(rows[option - 1][1])
# except:
#     e = sys.exc_info()[0]
#     print(e)
