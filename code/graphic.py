from tkinter import *
from functools import partial
from calc import calculate



# functions for buttons
def change_screen(screen_text: StringVar, char: str):
    screen_text.set(screen_text.get() + char)

def clear_screen(screen_text: StringVar):
    screen_text.set('')

def del_screen(screen_text: StringVar):
    screen_text.set(screen_text.get()[:-1])

def output_result(text: StringVar):
    result = calculate(text.get())
    text.set(str(result))



def create_calc() -> tuple[Tk, StringVar]:
    """Create a calculator with Tkinter
        
    Returns the top-window widget and the text-variable displayed in the calculator screen"""

    # setting up the top-window
    root = Tk()
    root.title("Calculator")
    root.resizable(False, False)


    # frame with the size
    UNIT = 35
    frame = Canvas(root, bg="#2b2d42", width=10*UNIT, height=16*UNIT)
    frame.grid(sticky='nsew', columnspan=10, rowspan=16)


    # calculator screen
    text = StringVar()
    my_font = 'Courier 16 bold'
    screen = Label(root, textvariable=text, bg="#edf2f4", relief=FLAT, padx=UNIT, anchor=W, font=my_font, width=1, name="screen")
    screen.grid(column=1, row=1, columnspan=8, rowspan=3, sticky="nsew")


    # all the buttons
    my_buttons = [
        {"text": "C", "bg": "#ef233c", "act-bg": "#d90429", "cmd":partial(clear_screen, text)},
        {"text": "del", "bg": "#ef233c", "act-bg": "#d90429", "cmd":partial(del_screen, text)},
        {"text": "(", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '(')},
        {"text": ")", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, ')')},
        {"text": "7", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '7')},
        {"text": "8", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '8')},
        {"text": "9", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '9')},
        {"text": "/", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": partial(change_screen, text, '/')},
        {"text": "4", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '4')},
        {"text": "5", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '5')},
        {"text": "6", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '6')},
        {"text": "*", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": partial(change_screen, text, '*')},
        {"text": "1", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '1')},
        {"text": "2", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '2')},
        {"text": "3", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '3')},
        {"text": "-", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": partial(change_screen, text, '-')},
        {"text": "0", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '0')},
        {"text": ".", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": partial(change_screen, text, '.')},
        {"text": "=", "bg": "#ef233c", "act-bg": "#d90429", "cmd":partial(output_result, text)},
        {"text": "+", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": partial(change_screen, text, '+')}
    ]

    for i in range(len(my_buttons)):
        btn = my_buttons[i]
        temp_btn = Button(root, text=btn['text'], bg=btn['bg'], activebackground=btn['act-bg'], font=my_font, command=btn['cmd'])
        temp_btn.grid(row=5+(i//4)*2, column=1+(i%4)*2, columnspan=2, rowspan=2, sticky="nsew")


    return (root, text)



if __name__ == "__main__":
    calc, text = create_calc()
    calc.mainloop()
