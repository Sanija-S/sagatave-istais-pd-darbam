import PySimpleGUI as sg
sg.theme("LightGreen2")
layout=[
   [sg.InputText(key="Display", size= (20,1),justification="right", readonly=True)],
   [sg.Button("EXIT", key="EXIT"),sg.Button("click")],
   [sg.Button("1"),sg.Button("2"),sg.Button("3")],
   [sg.Button("4"),sg.Button("5"),sg.Button("6")],
   [sg.Button("7"),sg.Button("8"),sg.Button("9")],
   sg
 

]

 # hover over to see options
window= sg.Window("Loga nosaukums", layout) # mainigais ka pamats kas atradisies uz ta loga

while True:
    event, values=window.read()
    if event==sg.WIN_CLOSED or event=="EXIT":
      break
    if event=="click":
       print("Poga tika nospiesta :)")



window.close() 