import PySimpleGUI as sg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sg.theme("DarkTeal6")
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
    [sg.Canvas(key="-CANVAS-")],
]

# finalize is need because we are adding the graph to the window before calling window.read()
window = sg.Window("Math Graph", layout, finalize=True)

# matplotlib setup
fig = Figure(figsize=(5, 4))
fig.add_subplot(111).plot([], [])
figure_canvas_agg = FigureCanvasTkAgg(fig, window["-CANVAS-"].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-SUBMIT-":
        new_value: str = values["-INPUT-"]
        if new_value.isnumeric():
            table_content.append([len(table_content) + 1, float(new_value)])
            window["-TABLE-"].update(table_content)
            window["-INPUT-"].update("")

window.close()
