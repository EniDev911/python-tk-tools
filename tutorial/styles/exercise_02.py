import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):

        super().__init__()

        # root window
        self.title('Theme Demo')
        self.geometry('400x300')
        self.tk.eval("""
            # base_theme_dir = path/download/theme/
            set base_theme_dir ../../assets/themes_ttk/awthemes-10.3.0/
            package ifneeded awthemes 10.3.0 \
                [list source [file join $base_theme_dir awthemes.tcl]]
            package ifneeded colorutils 4.8 \
                [list source [file join $base_theme_dir colorutils.tcl]]
            package ifneeded awdark 7.11 \
                [list source [file join $base_theme_dir awdark.tcl]]
            package ifneeded awlight 7.9 \
                [list source [file join $base_theme_dir awlight.tcl]]
            """)
        self.tk.call('package', 'require', 'awdark')

        self.style = ttk.Style(self)

        # label
        label = ttk.Label(self, text='Name:')
        label.grid(column=0, row=0, padx=10, pady=10,  sticky='w')
        # entry
        textbox = ttk.Entry(self)
        textbox.grid(column=1, row=0, padx=10, pady=10,  sticky='w')
        # button
        btn = ttk.Button(self, text='Show')
        btn.grid(column=2, row=0, padx=10, pady=10,  sticky='w')

        # radio button
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self, text='Themes')
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.change_theme)
            rb.pack(expand=True, fill='both')

    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())



if __name__ == "__main__":
    app = App()
    app.mainloop()