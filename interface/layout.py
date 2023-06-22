import PySimpleGUI as  sg




title = "File Converter"
options = (".JPG", ".PNG", ".WebP", ".JPEG")




sg.theme("DarkGray9")
sg.set_options(font="Calibri")



layout = [

            [
                sg.Column([
                    [sg.Text("Select the file", key="-FileSelect-", justification="center")],
                    [sg.Input(visible=False, key="-InputFileBrowse-")],
                    [sg.FileBrowse(size=(10, 2), key="-FileBrowse-")],
                    [sg.Text("", text_color="black", visible=False, key="-FilePath-", font=("Consolas", 8))],
                    ],
                    ),
                sg.Stretch(),
                sg.Text("Select the new format", key="-NewFormat-", justification="center"),
            ],





            [
                sg.Column([
                    [sg.Text("Or select a path for\nmultiple files", key="-FilesFolderSelect-", justification="center")],
                    [sg.Input(visible=False, key="-InputFilesFolderSelect-")],
                    [sg.FolderBrowse(size=(10, 2), key="-FilesFolderBrowse-")],
                    [sg.Text("", text_color="black", visible=False, key="-FilesFolderPath-", font=("Consolas", 8))],

                    ],
                    ),


                sg.Stretch(),
                sg.Listbox(options, size=(40, 40), highlight_background_color="#987FA2", background_color="#626567", text_color="black", font=("Consolas", 12), key="-NewFormatList-"),
                sg.Stretch(),



                sg.Column([
                    [sg.Input(visible=False, key="-InputFolderBrowse-")],
                    [sg.FolderBrowse(key="-FolderBrowse-",size=(15, 2), button_text="Seleccionar\nruta de destino"),  sg.Button("GO!", key="-Submit-", button_color="white on green")],
                        ],
                        ),
            ],

        ]




window = sg.Window(title, layout, size=(850,450))