from tkinter import *
from calc import calculate



class Calculator:
    """A class used to represent a calculator

    Attributes
    ----------
    name : str
        Name of the calculator window
    root: Tk
        Top-window of the calculator
    unit: int
        Unit size used to build the calculator 
    font : str
        Font used in the calculator text (in tkinter format)
    input : StringVar
        text in the input line
    output : StringVar
        text in the output line
    history : list
        List of all the previous calculations
    
    Methods
    -------
    setup()
        build the widgets of the calculator
    run()
        run the mainloop of Tk
    change_screen(char)
        add a character at the end of the input line
    clear_screen()
        remove all the text from the screen
    del_screen()
        remove the last character of the input line
    output_result()
        output the result of the calculation in the input line"""

    def __init__(self, name:str ='Calculator', width:int =350):
        """Parameters
        ---------
        name : str, optional
            Name of the calculator window (default "Calculator")
        width : int, optional
            Width of the calcultor window (default 350px)"""
        self.root = Tk()
        self.name = name
        self.unit = width // 10
        self.font = f'Courier {width//21} bold'
        self.input = StringVar()
        self.output = StringVar()
        self.history = []

    
    def setup(self) -> None:
        """Build all the widgets in the calculator"""
        self.root.title(self.name)
        self.root.resizable(False, False)

        frame = Frame(self.root, bg="#2b2d42", width=10*self.unit, height=16*self.unit, relief=RAISED, borderwidth=self.unit//3)
        frame.grid(sticky='nsew', columnspan=10, rowspan=16)

        screen_frame = Frame(self.root, height=self.unit*3, width=self.unit*8)
        screen_frame.pack_propagate(0)
        screen_frame.grid(column=1, row=1, columnspan=8, rowspan=3)

        screen_input = Label(screen_frame, textvariable=self.input, padx=self.unit//3, pady=self.unit//3, justify=LEFT, anchor=NW, font=self.font)
        screen_input.pack(anchor=NW)
        screen_output = Label(screen_frame, textvariable=self.output, padx=self.unit//3, pady=self.unit//3, justify=RIGHT, anchor=SE, font=self.font)
        screen_output.pack(anchor=SE)
        

        buttons = [
            {"text": "C", "bg": "#ef233c", "act-bg": "#d90429", "cmd":lambda: self.clear_screen()},
            {"text": "del", "bg": "#ef233c", "act-bg": "#d90429", "cmd":lambda: self.del_screen()},
            {"text": "(", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('(')},
            {"text": ")", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen(')')},
            {"text": "7", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('7')},
            {"text": "8", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('8')},
            {"text": "9", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('9')},
            {"text": "/", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": lambda: self.change_screen('/')},
            {"text": "4", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('4')},
            {"text": "5", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('5')},
            {"text": "6", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('6')},
            {"text": "*", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": lambda: self.change_screen('*')},
            {"text": "1", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('1')},
            {"text": "2", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('2')},
            {"text": "3", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('3')},
            {"text": "-", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": lambda: self.change_screen('-')},
            {"text": "0", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('0')},
            {"text": ".", "bg": "#8d99ae", "act-bg": "#79869c", "cmd": lambda: self.change_screen('.')},
            {"text": "=", "bg": "#ef233c", "act-bg": "#d90429", "cmd":lambda: self.output_result()},
            {"text": "+", "bg": "#edf2f4", "act-bg": "#ced4da", "cmd": lambda: self.change_screen('+')}
        ]

        for i in range(len(buttons)):
            btn = buttons[i]
            temp_btn = Button(self.root, text=btn['text'], bg=btn['bg'], activebackground=btn['act-bg'], borderwidth=self.unit//7, font=self.font, command=btn['cmd'])
            temp_btn.grid(row=5+(i//4)*2, column=1+(i%4)*2, columnspan=2, rowspan=2, sticky="nsew")
        
        key_events = [
                ('0', lambda e: self.change_screen('0')),
                ('1', lambda e: self.change_screen('1')),
                ('2', lambda e: self.change_screen('2')),
                ('3', lambda e: self.change_screen('3')),
                ('4', lambda e: self.change_screen('4')),
                ('5', lambda e: self.change_screen('5')),
                ('6', lambda e: self.change_screen('6')),
                ('7', lambda e: self.change_screen('7')),
                ('8', lambda e: self.change_screen('8')),
                ('9', lambda e: self.change_screen('9')),
                ('period', lambda e: self.change_screen('.')),
                ('plus', lambda e: self.change_screen('+')),
                ('minus', lambda e: self.change_screen('-')),
                ('asterisk', lambda e: self.change_screen('*')),
                ('slash', lambda e: self.change_screen('/')),
                ('parenleft', lambda e: self.change_screen('(')),
                ('parenright', lambda e: self.change_screen(')')),
                ('Return', lambda e: self.output_result()),
                ('equal', lambda e: self.output_result()),
                ('BackSpace', lambda e: self.del_screen()),
                ('Delete', lambda e: self.clear_screen())
            ]

        for key, event in key_events:
            self.root.bind(f'<Key-{key}>', event)
    
    def run(self):
        """Run the mainloop of the calculator"""
        self.root.mainloop()


    def change_screen(self, char: str):
        """Add a character at the end of the input
        
        If there was a previous calculation, it clears it
        
        Paramaters
        ---------
        char : str
            character to insert at the end of the line"""

        if len(self.output.get()) > 0:
            self.clear_screen()
        self.input.set(self.input.get() + char)


    def clear_screen(self):
        """Clear all the texts in the calculator screen"""
        self.input.set('')
        self.output.set('')


    def del_screen(self):
        """Delete the last character from the input
        
        If an output is present, it clears the screen"""
        if len(self.output.get()) > 0:
            self.clear_screen()
        self.input.set(self.input.get()[:-1])


    def output_result(self):
        """Output the result of the input line and add it to the history"""

        result = calculate(self.input.get())
        self.output.set(str(result))
        self.history.append([self.input.get(), self.output.get()])
