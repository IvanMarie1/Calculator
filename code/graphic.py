from tkinter import *
from functools import partial
from calc import calculate



# functions for buttons
def change_screen(txt_input: StringVar, txt_output: StringVar, char: str):
    """Add a character at the end of the input
    
    If there was a previous calculation, it clears it"""

    if len(txt_output.get()) > 0:
        clear_screen(txt_input, txt_output)
    txt_input.set(txt_input.get() + char)


def clear_screen(*texts: list[StringVar] ):
    """Clear all the texts passed in arguments"""
    for txt in texts:
        txt.set('')


def del_screen(txt_input: StringVar, txt_output):
    """Delete the last character from the input
    
    If an output is present, it clears the screen"""
    if len(txt_output.get()) > 0:
        clear_screen(txt_input, txt_output)
    txt_input.set(txt_input.get()[:-1])


def output_result(txt_input: StringVar, txt_output: StringVar):
    """Output the result of the input line and add it to the history"""

    result = calculate(txt_input.get())
    txt_output.set(str(result))
    history.append([txt_input.get(), txt_output])



def create_calc() -> tuple[Tk, StringVar, StringVar]:
    """Create a calculator with Tkinter
        
    Returns the top-window widget and the text-variable displayed in the calculator screen"""
    global history
    history = []

    # setting up the top-window
    root = Tk()
    root.title("Calculator")
    root.resizable(False, False)


    # frame with the size
    UNIT = 35
    frame = Canvas(root, bg="#2b2d42", width=10*UNIT, height=16*UNIT)
    frame.grid(sticky='nsew', columnspan=10, rowspan=16)


    # calculator screen
    text_input = StringVar()
    text_output = StringVar()
    my_font = 'Courier 16 bold'

    screen_frame = Frame(root, height=UNIT*3, width=UNIT*8)
    screen_frame.pack_propagate(0)
    screen_frame.grid(column=1, row=1, columnspan=8, rowspan=3)

    screen_input = Label(screen_frame, textvariable=text_input, bg="#edf2f4", padx=UNIT//2, pady=UNIT//2, justify=LEFT, font=my_font)
    screen_input.pack(anchor=NW)
    screen_output = Label(screen_frame, textvariable=text_output, bg="#edf2f4", padx=UNIT//2, pady=UNIT//2, justify=RIGHT, font=my_font)
    screen_output.pack(anchor=SE)



    # all the buttons
    my_buttons = [
        {"text": "C", "bg": "#ef233c", "act-bg": "#d90429", "cmd":partial(clear_screen, text_input, text_output)},
        {"text": "del", "bg": "#ef233c", "act-bg": "#d90429", "cmd":partial(del_screen, text_input, text_output)},
        {"text": "(", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '(')},
        {"text": ")", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, ')')},
        {"text": "7", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '7')},
        {"text": "8", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '8')},
        {"text": "9", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '9')},
        {"text": "/", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": partial(change_screen, text_input, text_output, '/')},
        {"text": "4", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '4')},
        {"text": "5", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '5')},
        {"text": "6", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '6')},
        {"text": "*", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": partial(change_screen, text_input, text_output, '*')},
        {"text": "1", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '1')},
        {"text": "2", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '2')},
        {"text": "3", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '3')},
        {"text": "-", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": partial(change_screen, text_input, text_output, '-')},
        {"text": "0", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '0')},
        {"text": ".", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text_input, text_output, '.')},
        {"text": "=", "bg": "#ef233c", "act-bg": "#d90429", "cmd":partial(output_result, text_input, text_output)},
        {"text": "+", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": partial(change_screen, text_input, text_output, '+')}
    ]

    for i in range(len(my_buttons)):
        btn = my_buttons[i]
        temp_btn = Button(root, text=btn['text'], bg=btn['bg'], activebackground=btn['act-bg'], font=my_font, command=btn['cmd'])
        temp_btn.grid(row=5+(i//4)*2, column=1+(i%4)*2, columnspan=2, rowspan=2, sticky="nsew")


    return (root, text_input, text_output)
