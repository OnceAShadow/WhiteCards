# someWindow.py
import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]
window = sg.Window("Demo", layout, layout,size=(1000, 600))


while True:
    event, values = window.read()
    
    if event == "OK" or event == sg.WIN_CLOSED:
   		break

window.close()
