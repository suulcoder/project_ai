import PySimpleGUI as sg
import os.path
import PIL 
from PIL import Image
from model import * 
 
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
    [sg.Text("Nearest Neighbor:")],
    [sg.Image(key="image_chosen")],
    [
        sg.Image(key="image_0"),
        sg.Image(key="image_1"),
        sg.Image(key="image_2")
    ],
    [
        sg.Image(key="image_3"),
        sg.Image(key="image_4"),
        sg.Image(key="image_5")
    ],
    [
        sg.Image(key="image_6"),
        sg.Image(key="image_7"),
        sg.Image(key="image_8")
    ],
    [sg.Image(key="image_9")],
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
        filename = os.path.join(
            val["folder"], val["files"][0]
        )
        image = Image.open(filename)
        ratio = image.size[1]/image.size[0]
        new_image = image.resize((100,int(100*ratio)), Image.ANTIALIAS)
        new_image.save('chosen.png')
        new_file = os.path.join(
            os.getcwd(), 'chosen.png'
        )
        window["image_chosen"].update(filename=new_file)
        index = 0
        for image in get_related(filename):
            key_image = "image_" + str(index)
            filepath = os.path.join(
                os.getcwd(), 'Data/train'
            )
            filename_ = os.path.join(
                filepath, image
            )
            image_ = Image.open(filename_)
            new_image_ = image_.resize((100,int(100*ratio)), Image.ANTIALIAS)
            new_image_.save(str(index) + '.png')
            new_file_ = os.path.join(
                os.getcwd(), str(index) + '.png'
            )
            window[key_image].update(filename=new_file_)
            index+=1

window.close()