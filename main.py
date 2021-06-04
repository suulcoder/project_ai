import PySimpleGUI as sg
import os.path
import PIL 
from PIL import Image 
 
sg.theme('Topanga')
second_column = [
    [
        sg.Text("CHOSE AN IMAGE:"),
        sg.In(size=(20, 1), enable_events=True, key="folder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(45, 20), key="files"
        )
    ],
]

first_column = [
    [sg.Text(size=(40, 1), key="text")],
    [sg.Image(key="image_chosen")],
]

my_GUI = [
    [
        sg.Column(first_column),
        sg.VSeperator(),
        sg.Column(second_column),
    ]
]  

window = sg.Window("AI project", my_GUI)

while True:
    ev, val = window.read()
    if ev == "Exit" or ev == sg.WIN_CLOSED:
        break
    if ev == "folder":
        folder = val["folder"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        fnames = [
            my_file
            for my_file in file_list
            if os.path.isfile(os.path.join(folder, my_file))
            and my_file.lower().endswith((".png", ".jpg"))
        ]
        window["files"].update(fnames)
    elif ev == "files":
        try:
            filename = os.path.join(
                val["folder"], val["files"][0]
            )
            image = Image.open(filename)
            image.resize((100,100))
            image.save('chosen.jpg')
            new_file = os.path.join(
                os.getcwd(), 'chosen.jpg'
            )
            print(new_file,filename)
            window["image_chosen"].update(filename=new_file)
        except:
            pass

window.close()