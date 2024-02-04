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
    cursor : int
        Position of the cursor in the input line
    
    Methods
    -------
    setup()
        build the widgets of the calculator
    run()
        run the mainloop of Tk
    add_char(char)
        add a character at the end of the input line
    clear()
        remove all the text from the screen
    backspace()
        remove the last character of the input line
    result()
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
        self.font = f'Arial {width//21} bold'
        self.input = StringVar(value="|")
        self.output = StringVar()
        self.history = []
        self.cursor = 0

    
    def setup(self) -> None:
        """Build all the widgets in the calculator"""

        colors = {'r1': '#EF233C', 'r2': "#D90429", 
                  'g1': "#8D99AE", 'g2': "#7B879C", 
                  'w1': "#EDF2F4", 'w2': "#CED4DA", 
                  'b1': "#2B2D42"}
        
        self.root.title(self.name)
        self.root.resizable(False, False)

        frame = Frame(self.root, bg=colors["b1"], width=10*self.unit, height=16*self.unit)
        frame.grid(sticky='nsew', columnspan=10, rowspan=16)

        screen_frame = Frame(self.root, height=self.unit*3, width=self.unit*8, bg=colors['w1'])
        screen_frame.pack_propagate(0)
        screen_frame.grid(column=1, row=1, columnspan=8, rowspan=3)

        screen_input = Label(screen_frame, textvariable=self.input, padx=self.unit//3, pady=self.unit//3, justify=LEFT, anchor=NW, font=self.font)
        screen_input.pack(anchor=NW)
        screen_output = Label(screen_frame, textvariable=self.output, padx=self.unit//3, pady=self.unit//3, justify=RIGHT, anchor=SE, font=self.font)
        screen_output.pack(anchor=SE)
        

        buttons = [
            {"txt": "C", "c": ('r1', 'r2'), "cmd":lambda: self.clear()},
            {"txt": "del", "c": ('r1', 'r2'), "cmd":lambda: self.backspace()},
            {"txt": "(", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('(')},
            {"txt": ")", "c": ('g1', 'g2'), "cmd": lambda: self.add_char(')')},
            {"txt": "7", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('7')},
            {"txt": "8", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('8')},
            {"txt": "9", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('9')},
            {"txt": "/", "c": ('w1', 'w2'), "cmd": lambda: self.add_char('/')},
            {"txt": "4", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('4')},
            {"txt": "5", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('5')},
            {"txt": "6", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('6')},
            {"txt": "*", "c": ('w1', 'w2'), "cmd": lambda: self.add_char('*')},
            {"txt": "1", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('1')},
            {"txt": "2", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('2')},
            {"txt": "3", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('3')},
            {"txt": "-", "c": ('w1', 'w2'), "cmd": lambda: self.add_char('-')},
            {"txt": "0", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('0')},
            {"txt": ".", "c": ('g1', 'g2'), "cmd": lambda: self.add_char('.')},
            {"txt": "=", "c": ('r1', 'r2'), "cmd":lambda: self.result()},
            {"txt": "+", "c": ('w1', 'w2'), "cmd": lambda: self.add_char('+')}
        ]

        for i in range(len(buttons)):
            btn = buttons[i]
            c1, c2 = colors[btn["c"][0]], colors[btn["c"][1]]
            temp_btn = Button(self.root, text=btn['txt'], bg=c1, activebackground=c2, relief=FLAT, font=self.font, borderwidth=0, command=btn['cmd'])
            temp_btn.grid(row=5+(i//4)*2, column=1+(i%4)*2, columnspan=2, rowspan=2, sticky="nsew", padx=1, pady=1)
        
        key_events = [
                ('0', lambda e: self.add_char('0')),
                ('1', lambda e: self.add_char('1')),
                ('2', lambda e: self.add_char('2')),
                ('3', lambda e: self.add_char('3')),
                ('4', lambda e: self.add_char('4')),
                ('5', lambda e: self.add_char('5')),
                ('6', lambda e: self.add_char('6')),
                ('7', lambda e: self.add_char('7')),
                ('8', lambda e: self.add_char('8')),
                ('9', lambda e: self.add_char('9')),
                ('period', lambda e: self.add_char('.')),
                ('plus', lambda e: self.add_char('+')),
                ('minus', lambda e: self.add_char('-')),
                ('asterisk', lambda e: self.add_char('*')),
                ('slash', lambda e: self.add_char('/')),
                ('parenleft', lambda e: self.add_char('(')),
                ('parenright', lambda e: self.add_char(')')),
                ('Return', lambda e: self.result()),
                ('equal', lambda e: self.result()),
                ('BackSpace', lambda e: self.backspace()),
                ('Delete', lambda e: self.clear()),
                ('Up', lambda e: self.move(e.keysym)),
                ('Down', lambda e: self.move(e.keysym)),
                ('Right', lambda e: self.move(e.keysym)),
                ('Left', lambda e: self.move(e.keysym))
            ]

        for key, event in key_events:
            self.root.bind(f'<Key-{key}>', event)
    
    def run(self):
        """Run the mainloop of the calculator"""
        self.root.mainloop()


    def add_char(self, char: str):
        """Add a character at the cursor position
        
        If there was a previous calculation, it clears it
        
        Paramaters
        ---------
        char : str
            character to insert at the end of the line"""

        if len(self.output.get()) > 0:
            self.clear()

        new_input = f"{char}|".join(self.input.get().split('|'))
        self.input.set(new_input)
        self.cursor += 1


    def clear(self):
        """Clear all the texts in the calculator screen"""
        self.input.set('|')
        self.output.set('')
        self.cursor = 0


    def backspace(self):
        """Delete the last character from the input
        
        If an output is present, it clears the screen"""
        if len(self.output.get()) > 0:
            self.clear()
        if self.cursor > 0:
            self.input.set(self.input.get()[:self.cursor-1] + self.input.get()[self.cursor:])
            self.cursor -= 1


    def result(self):
        """Output the result of the input line and add it to the history"""
        calculation = "".join(self.input.get().split("|"))
        result = calculate(calculation)
        self.output.set(str(result))
        self.history.append([self.input.get(), self.output.get()])
    

    def move(self, key):
        """Move the cursor in a certain direcion"""
        if len(self.output.get()) > 0:
            self.clear()
            
        text = self.input.get()
        i = self.cursor
        if key == "Right" and self.cursor < len(text)-1:
            new_text = f"{ text[:self.cursor] }{ text[self.cursor+1] }|{ text[self.cursor+2:] }"
            self.input.set(new_text)
            self.cursor += 1

        elif key == "Left" and self.cursor > 0:
            new_text = f"{ text[:self.cursor-1] }|{ text[self.cursor-1] }{ text[self.cursor+1:] }"
            self.input.set(new_text)
            self.cursor -= 1
