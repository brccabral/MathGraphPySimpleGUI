import PySimpleGUI as sg

table_content = []
layout = [
    [
        sg.Table(
            headings=["Observation", "Result"],
            values=table_content,
            expand_x=True,
            hide_vertical_scroll=True,
            key="-TABLE-",
        )
    ],
    [sg.Input(key="-INPUT-", expand_x=True), sg.Button("Submit", key="-SUBMIT-")],
]

window = sg.Window("Math Graph", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
