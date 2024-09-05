import tkinter as tk
from tkinter import ttk

class Theme:
    font = ('Consolas', 12, 'bold')
    background = "#333"
    background_alt = "#222"
    foreground = "#fff"
    foreground_alt = "#ccc"
    success = "#080"
    warning = "#bb0"
    failure = "#800"
    primary = "#00a"

root = tk.Tk()
root.title("Tkinter GUI")
root.resizable(0, 0)
root.geometry("800x400")
root.configure(bg=Theme.background)

# Create and configure ttk Style
style = ttk.Style()
style.theme_use('default')

# Notebook style
style.configure('TNotebook', background=Theme.background_alt, borderwidth=0)
style.configure('TNotebook.Tab', background=Theme.background_alt, foreground=Theme.foreground_alt,
                padding=[10, 5], borderwidth=0, font=Theme.font)
style.map('TNotebook.Tab', background=[("selected", Theme.background)],
          foreground=[("selected", Theme.foreground)])

# Scrollbar style
style.configure("Vertical.TScrollbar", gripcount=0,
                background=Theme.background_alt, darkcolor=Theme.background_alt,
                lightcolor=Theme.background, troughcolor="#1E1E1E",
                bordercolor="#1E1E1E", arrowcolor=Theme.foreground)

# Button style
style.configure('TButton', background=Theme.primary, foreground=Theme.foreground,
                font=Theme.font, padding=[5, 5])
style.map('TButton', background=[('active', Theme.success), ('disabled', Theme.failure)],
          foreground=[('disabled', Theme.foreground_alt)])

# Label style
style.configure('TLabel', background=Theme.background, foreground=Theme.foreground,
                font=Theme.font)

# Frame style
style.configure('TFrame', background=Theme.background)

# Entry style
style.configure('TEntry', fieldbackground=Theme.background_alt, foreground=Theme.foreground,
                insertcolor=Theme.foreground, font=Theme.font)

# Checkbutton style
style.configure('TCheckbutton', background=Theme.background, foreground=Theme.foreground,
                font=Theme.font)
style.map('TCheckbutton', background=[('active', Theme.background_alt)],
          foreground=[('selected', Theme.success)])

# Radiobutton style
style.configure('TRadiobutton', background=Theme.background, foreground=Theme.foreground,
                font=Theme.font)
style.map('TRadiobutton', background=[('active', Theme.background_alt)],
          foreground=[('selected', Theme.success)])

# Combobox style
style.configure('TCombobox', fieldbackground=Theme.background_alt, background=Theme.background,
                foreground=Theme.foreground, selectbackground=Theme.background, selectforeground=Theme.foreground,
                font=Theme.font)

# Scale style
style.configure('TScale', background=Theme.background, foreground=Theme.foreground)

# Spinbox style
style.configure('TSpinbox', fieldbackground=Theme.background_alt, background=Theme.background,
                foreground=Theme.foreground, font=Theme.font)

# Progressbar style
style.configure('TProgressbar', background=Theme.primary, troughcolor=Theme.background_alt)

# Notebook setup
tabControl = ttk.Notebook(root, style='TNotebook')
tab1 = ttk.Frame(tabControl, style='TFrame')
tab2 = ttk.Frame(tabControl, style='TFrame')
tabControl.add(tab1, text='INSTANCES')
tabControl.add(tab2, text='USER CREDENTIALS & API KEY')
tabControl.pack(expand=1, fill="both")

# Add sample widgets to tab1
label1 = ttk.Label(tab1, text="Sample Label", style='TLabel')
label1.pack(pady=10)

button1 = ttk.Button(tab1, text="Sample Button", style='TButton')
button1.pack(pady=10)

entry1 = ttk.Entry(tab1, style='TEntry')
entry1.pack(pady=10)

checkbutton1 = ttk.Checkbutton(tab1, text="Sample Checkbutton", style='TCheckbutton')
checkbutton1.pack(pady=10)

radiobutton1 = ttk.Radiobutton(tab1, text="Sample Radiobutton", style='TRadiobutton')
radiobutton1.pack(pady=10)

combobox1 = ttk.Combobox(tab1, values=["Option 1", "Option 2", "Option 3"], style='TCombobox')
combobox1.pack(pady=10)

scale1 = ttk.Scale(tab1, from_=0, to=100, style='TScale')
scale1.pack(pady=10)

spinbox1 = ttk.Spinbox(tab1, from_=0, to=10, style='TSpinbox')
spinbox1.pack(pady=10)

progressbar1 = ttk.Progressbar(tab1, style='TProgressbar', length=200)
progressbar1.pack(pady=10)
progressbar1['value'] = 50  # Set the initial value of the progress bar

# Run the application
root.mainloop()
