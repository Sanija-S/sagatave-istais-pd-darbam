#pielagoti logrīki ar pysimplegui
import PySimpleGUI as sg
sg.theme("LightBlue2")
layout=[
  
   [sg.InputText(key="Display", size= (20,1),justification="right", readonly=True)],
   [sg.Text("Ievadi vārdu:"), sg.InputText(key="IN")],
   [sg.Text("Ievadi uzvārdu:"), sg.InputText(key="INN")],
   [sg.Button("OK")],
   [sg.Text("",key="OUTPUT")],
   [sg.Button("EXIT", key="EXIT"),sg.Button("click")],
   [sg.Button("Ziema"),sg.Button("Pavasaris")],
   [sg.Button("Vasara"),sg.Button("Rudens")],
   
]
window= sg.Window("Ziema", layout) # mainigais ka pamats kas atradisies uz ta loga

while True:
    event, values=window.read()
    if event==sg.WIN_CLOSED or event=="EXIT":
      break
    if event=="click":
       print("Poga tika nospiesta :)")
    if event=="Ziema":
       print("Brrr auksti-")
    if event=="Pavasaris":
       print("Visapkārt smukas puķes un biki dubļains")
    if event=="Vasara":
       print("Arā tik silts, odi kožs")
    if event=="Rudens":
       print("Rudenī lapas man krīt kā nauda")
    if event=="OK":
       window["OUTPUT"].update(f"Mani sauc {values['IN']} {values['INN']}.")
    else:
       sg.popup_error("Lūdzu, ievadier vārdu un uzvārdu!")


