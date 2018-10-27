import tkinter as tk
from tkinter import ttk

# constant colors and fonts using in this GUI
HEADER_FONT = ('Open Sans', 15)
BUTTON_FONT = ('Open Sans', 12)
LABEL_FONT = ('Open Sans light', 10)
ENTRY_FONT = ('Open Sans', 10)
DARK_GRAY_COlOR = '#393E41'
GRAY_COLOR = '#D3D0CB'
LIGHT_GRAY_COLOR = '#E7E5DF'
YELLOW_COLOR = '#E7BB41'
BLUE_COLOR = '#44BBA4'


class CryptApp(tk.Tk):
    """
        Main class for initializing multiple windows and handle it.
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(600, 400)
        self.geometry('600x400+300+250')
        self.title('Cryptograpthy lab #2')
        container = ttk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = dict()

        frame = MainPage(container, self)

        self.frames[MainPage] = frame

        frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(MainPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()


class MainPage(ttk.Frame):
    """
        Main page of cryptographer. Containing GUI (buttons, labels and inputs)
        for input file, input decryption key, handle file (encrypt or decrypt)
        and save it to another file.
    """
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        style = ttk.Style()
        style.configure('TFrame', background=DARK_GRAY_COlOR)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=3)
        self.rowconfigure(6, weight=2)

        style.configure('TButton', font=BUTTON_FONT, padding=10, relief='flat',
                        foreground=DARK_GRAY_COlOR)
        style.configure('open.TButton', background=YELLOW_COLOR)
        style.configure('encrypt.TButton', background=YELLOW_COLOR)
        style.configure('key.TEntry', font=ENTRY_FONT, background=GRAY_COLOR, foreground=DARK_GRAY_COlOR,
                        padding='10 2 2 2')
        style.configure('TLabel', font=LABEL_FONT, background=DARK_GRAY_COlOR, foreground=LIGHT_GRAY_COLOR)
        style.configure("Vertical.TScrollbar", gripcount=0,
                        background=GRAY_COLOR, darkcolor=DARK_GRAY_COlOR, lightcolor=LIGHT_GRAY_COLOR,
                        troughcolor=LIGHT_GRAY_COLOR, bordercolor=GRAY_COLOR, arrowcolor=DARK_GRAY_COlOR,
                        relief='flat')

        header_label = tk.Label(self, text="Stream Encryption", font=HEADER_FONT,
                                background=DARK_GRAY_COlOR, foreground=BLUE_COLOR, justify='center')
        header_label.grid(padx=10, pady=10, column=0, row=0, columnspan=4, sticky='n e s w')

        open_file_button = ttk.Button(self, text='Open file...', style='open.TButton')
        open_file_button.grid(padx=10, pady=0, column=0, row=2, sticky='n w e s ')

        open_file_status_label = ttk.Label(self, text='Status: File is not opened!')
        open_file_status_label.grid(padx=10, column=0, row=3, sticky='n w')

        encrypt_decrypt_key_label = ttk.Label(self, text='Encryption/ Decryption key:')
        encrypt_decrypt_key_label.grid(padx=10, column=2, row=1, sticky='n w')

        self.encrypt_decrypt_key_entry = ttk.Entry(self, style='key.TEntry')
        self.encrypt_decrypt_key_entry.grid(padx=10, column=2, row=2, sticky='n w e s')

        encrypt_decrypt_key_label_len = ttk.Label(self, text='0/23')
        encrypt_decrypt_key_label_len.grid(padx=10, column=2, row=3, sticky='n w')

        encrypt_button = ttk.Button(self, text='Encrypt', style='encrypt.TButton')
        encrypt_button.grid(padx=10, pady=25, column=0, columnspan=2, row=4, sticky='n w e s')

        decrypt_button = ttk.Button(self, text='Decrypt', style='encrypt.TButton')
        decrypt_button.grid(padx=10, pady=25, column=2, columnspan=2, row=4, sticky='n w e s')

        input_file_bytes_label = ttk.Label(self, text='Input file bytes:')
        input_file_bytes_label.grid(padx=10, column=0, row=5, sticky='n w')

        output_file_bytes_label = ttk.Label(self, text='Output file bytes:')
        output_file_bytes_label.grid(padx=10, column=2, row=5, sticky='n w')

        input_file_bytes = tk.Text(self, font=ENTRY_FONT, background=LIGHT_GRAY_COLOR,
                                   foreground=DARK_GRAY_COlOR, relief='flat')
        input_file_bytes.grid(padx=10, pady=10, column=0, columnspan=2, row=6, sticky='n w e s')

        input_scroll = ttk.Scrollbar(input_file_bytes, orient='vertical')
        input_scroll.pack(side='right', fill='y')

        output_file_bytes = tk.Text(self, font=ENTRY_FONT, background=LIGHT_GRAY_COLOR,
                                    foreground=DARK_GRAY_COlOR, relief='flat')
        output_file_bytes.grid(padx=10, pady=10, column=2, columnspan=2, row=6, sticky='n w e s')

        output_scroll = ttk.Scrollbar(output_file_bytes)
        output_scroll.pack(side='right', fill='y')


app = CryptApp()
app.mainloop()
