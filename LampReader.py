#simple server_data.php reader
#coded by Lamp (c) numex
import PySimpleGUI as sg
import requests
import webbrowser

sg.theme("BlueMono")

layout = [  [sg.Text('Hey There!! Welcome to LampReader')],
            [sg.Text('With This tool you can read any server_data.php')],
            [sg.Text('')],
            [sg.Text('Enter Server IP '), sg.InputText()],
            [sg.Text('')],
            [sg.Button('Read', button_color="orange", size=(7)), sg.Button('About', button_color="green", size=(7)), sg.Button('Exit', button_color="red", size=(7))] ]

window = sg.Window('server_data.php reader by Lamp#1442', layout)

def about():
    layoutabout = [[sg.Text("Simple server_data.php reader by Lamp      ")],
    [sg.Button("Discord", button_color="gray"), sg.Button("Close", button_color="red")]]
    windowabout = sg.Window('About LampReader', layoutabout)
    eventa, valuesa = windowabout.read()
    if eventa == "Discord":
        webbrowser.open("https://discord.gg/wTNWHwWbSW")
        windowabout.close()
    elif eventa == "Close":
        windowabout.close()

def mainlol():
    read1 = requests.post("http://"+values[0]+"/growtopia/server_data.php")
    sg.popup("Result : ", read1.text, "")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break
    elif event == 'Read':
        if values[0] == "":
            sg.popup("Please Enter Correct IP! Dont Leave it Blank", title="Error!")
        else :
            mainlol()
    elif event == 'About':
        about()

window.close()
