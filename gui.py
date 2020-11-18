import csv
import PySimpleGUI as sg

def GUI():
    sg.theme('Dark Brown')
    sg.set_options(auto_size_buttons=True)

    # Reading .csv
    filename = "HCAkey.csv"
    with open(filename) as f:
        reader = csv.reader(f)
        data = [row for row in reader]
        header = data[0]

    # Windows layout
    layout = [
        [sg.Text('Select the target folder for conversion and the HCA key to be used')],
        [sg.Text('Target Folder', size=(10, 1)), sg.Input(), sg.FolderBrowse('Select Folder', key='inputFilePath')],
        [sg.Text('')],
        [sg.Table(values=data[1:],
                    headings = header,
                    def_col_width=28,
                    display_row_numbers=True,
                    auto_size_columns=False,
                    num_rows=min(100, len(data)-1))],
        [sg.Text('')],
        [sg.Text('Row number of the HCA key to be used', size=(30, 1)), sg.InputText('', size=(5, 1), key='rows')],
        [sg.Text('')],
        [sg.Button('OK', key='do')],
    ]

    window = sg.Window('acb2wavs4both', layout, grab_anywhere=False)
    event,values = window.read()
    HCAkey = data[int(values['rows'])+1][0]
    dir = values['inputFilePath']
    window.close()
    return HCAkey,dir
