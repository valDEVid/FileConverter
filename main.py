from scripts.file_conversion import main_file, path_conversion, file_conversion
from interface.layout import window
import PySimpleGUI as  sg



def start_conversion(event, values):
    if values["-FileBrowse"] is not None:
        is_ok = main_file(values["-FileBrowse-"], values["-FolderBrowse-"], values["-NewFormatList-"].lower())
    elif values:
        is_ok = main_file(values["-FilesFolderBrowse-"], values["-FolderBrowse-"], values["-NewFormatList-"].lower())
    return is_ok


while True:
    event, values = window.read()

    print(values["-NewFormatList-"])

    print(values["-FolderBrowse-"])

    if event == "-Submit-":
        try:
            start_conversion(event, values)
        except (NameError, PermissionError, KeyError):
            sg.popup("¡Oops!", "You forgot something...", title="Something went wrong", button_color="red")
            
        if values["-FileBrowse"] is not None:
            main_file(values["-FileBrowse-"], values["-FolderBrowse-"], values["-NewFormatList-"].lower())
        elif values:
            main_file(values["-FilesFolderBrowse-"], values["-FolderBrowse-"], values["-NewFormatList-"].lower())


        try:
            try:
                file_conversion(values["-FileBrowse-"], values["-FolderBrowse-"], values["-NewFormatList-"].lower())
                if file_conversion():
                    sg.popup("Conversion completed", title="Nice!", button_color="green")
            except AttributeError:
                path_conversion(values["-FilesFolderBrowse-"], values["-FolderBrowse-"], values["-NewFormatList-"].lower())
        except (NameError, PermissionError, KeyError):
            sg.popup("¡Oops!", "You forgot something...", title="Something went wrong", button_color="red")



    if event == sg.WIN_CLOSED:
        break
