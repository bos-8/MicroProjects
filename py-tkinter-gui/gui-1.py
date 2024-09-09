import tkinter as tk
from tkinter import ttk

# Define colors (similar to the Tcl theme)
colors = {
    "-frame": "#2e2e2e",
    "-window": "#1e1e1e",
    "-activebg": "#3e3e3e",
    "-troughbg": "#3e3e3e",
    "-selectbg": "#4e4e4e",
    "-selectfg": "#ffffff",
    "-disabledfg": "#7e7e7e",
    "-indicator": "#4e9a9a",
    "-altindicator": "#4e7a7a",
}

def apply_classic_theme(style):
    # Base settings for all widgets
    style.configure('.',
        font='TkDefaultFont',
        background=colors["-frame"],
        foreground='black',
        selectbackground=colors["-selectbg"],
        selectforeground=colors["-selectfg"],
        troughcolor=colors["-troughbg"],
        indicatorcolor=colors["-frame"],
        highlightcolor=colors["-frame"],
        highlightthickness=1,
        selectborderwidth=1,
        insertwidth=2
    )

    # Map background and foreground for general state changes
    style.map('.',
        background=[('disabled', colors["-frame"]), ('active', colors["-activebg"])],
        foreground=[('disabled', colors["-disabledfg"])],
        highlightcolor=[('focus', 'black')]
    )

    # TButton styles
    style.configure('TButton',
        anchor='center',
        padding="3 1",
        relief='raised',
        shiftrelief=1
    )
    style.map('TButton',
        relief=[('!disabled', 'pressed', 'sunken')]
    )

    # TCheckbutton styles
    style.configure('TCheckbutton',
        indicatorrelief='raised'
    )
    style.map('TCheckbutton',
        indicatorcolor=[('pressed', colors["-frame"]),
                        ('alternate', colors["-altindicator"]),
                        ('selected', colors["-indicator"])],
        indicatorrelief=[('alternate', 'raised'), ('selected', 'sunken'), ('pressed', 'sunken')]
    )

    # TRadiobutton styles
    style.configure('TRadiobutton',
        indicatorrelief='raised'
    )
    style.map('TRadiobutton',
        indicatorcolor=[('pressed', colors["-frame"]),
                        ('alternate', colors["-altindicator"]),
                        ('selected', colors["-indicator"])],
        indicatorrelief=[('alternate', 'raised'), ('selected', 'sunken'), ('pressed', 'sunken')]
    )

    # TMenubutton styles
    style.configure('TMenubutton',
        relief='raised',
        padding="3 1"
    )

    # TEntry styles
    style.configure('TEntry',
        relief='sunken',
        padding=1,
        font='TkTextFont'
    )
    style.map('TEntry',
        fieldbackground=[('readonly', colors["-frame"]),
                         ('disabled', colors["-frame"])]
    )

    # TCombobox styles
    style.configure('TCombobox',
        padding=1
    )
    style.map('TCombobox',
        fieldbackground=[('readonly', colors["-frame"]),
                         ('disabled', colors["-frame"])]
    )

    # Combobox popdown frame style
    style.configure('ComboboxPopdownFrame',
        relief='solid',
        borderwidth=1
    )

    # TSpinbox styles
    style.configure('TSpinbox',
        arrowsize=10,
        padding=(2, 0, 10, 0)
    )
    style.map('TSpinbox',
        fieldbackground=[('readonly', colors["-frame"]),
                         ('disabled', colors["-frame"])]
    )

    # TLabelframe styles
    style.configure('TLabelframe',
        borderwidth=2,
        relief='groove'
    )

    # TScrollbar styles
    style.configure('TScrollbar',
        relief='raised'
    )
    style.map('TScrollbar',
        relief=[('pressed', '!disabled', 'sunken')]
    )

    # TScale styles
    style.configure('TScale',
        sliderrelief='raised'
    )
    style.map('TScale',
        sliderrelief=[('pressed', '!disabled', 'sunken')]
    )

    # TProgressbar styles
    style.configure('TProgressbar',
        background='SteelBlue'
    )

    # TNotebook.Tab styles
    style.configure('TNotebook.Tab',
        padding=(3, 1),
        background=colors["-troughbg"]
    )
    style.map('TNotebook.Tab',
        background=[('selected', colors["-frame"])]
    )

    # Treeview styles
    style.configure('Heading',
        font='TkHeadingFont',
        relief='raised'
    )
    style.configure('Treeview',
        background=colors["-window"]
    )
    style.map('Treeview',
        background=[('disabled', colors["-frame"]),
                    ('selected', colors["-selectbg"])],
        foreground=[('disabled', colors["-disabledfg"]),
                    ('selected', colors["-selectfg"])]
    )

    # Toolbutton styles
    style.configure('Toolbutton',
        padding=2,
        relief='flat',
        shiftrelief=2
    )
    style.map('Toolbutton',
        relief=[('disabled', 'flat'),
                ('selected', 'sunken'),
                ('pressed', 'sunken'),
                ('active', 'raised')],
        background=[('pressed', colors["-troughbg"]),
                    ('active', colors["-activebg"])]
    )


# Tkinter app setup
root = tk.Tk()

# Apply theme
style = ttk.Style(root)
apply_classic_theme(style)

# Example widgets to test the theme
ttk.Button(root, text="Test Button").pack(padx=20, pady=20)
ttk.Checkbutton(root, text="Checkbutton").pack(padx=20, pady=20)
ttk.Radiobutton(root, text="Radiobutton").pack(padx=20, pady=20)
ttk.Entry(root).pack(padx=20, pady=20)
ttk.Combobox(root, values=["Option 1", "Option 2"]).pack(padx=20, pady=20)
ttk.Spinbox(root, from_=0, to=10).pack(padx=20, pady=20)
ttk.LabelFrame(root, text="Label Frame").pack(padx=20, pady=20)
ttk.Scrollbar(root).pack(padx=20, pady=20, side="right", fill="y")
ttk.Scale(root, from_=0, to=100).pack(padx=20, pady=20)
ttk.Progressbar(root).pack(padx=20, pady=20)
ttk.Treeview(root).pack(padx=20, pady=20)
ttk.Notebook(root).pack(padx=20, pady=20)

# Run the application
root.mainloop()
