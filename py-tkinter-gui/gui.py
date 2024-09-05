import tkinter as tk
from tkinter import ttk

class Font:
    font_b = ('Consolas', 12, 'bold')
    font_i = ('Consolas', 12, 'italic')
    font_bi = ('Consolas', 12, 'bold italic')
    font_n = ('Consolas', 12, 'normal')

class LightTheme:
    background = "#f8f9fa"
    background_alt = "#e2e6ea"
    foreground = "#212529"
    foreground_alt = "#495057"
    white = "#fff"
    gray = "#ccc"
    black = "#000"

class DarkTheme:
    background = "#212529"
    background_alt = "#1d2024"
    foreground = "#f8f9fa"
    foreground_alt = "#ced4da"
    white = "#fff"
    gray = "#ccc"
    black = "#000"

class Theme:
    def __init__(self, name, color, font):
        self.name = name
        self.color = color
        self.font = font
    def apply(self, style):
        root.configure(bg=self.color.background)

        style.configure('TNotebook', background=self.color.background_alt, borderwidth=0)
        # style.configure('TNotebook', background=Color.background_alt, borderwidth=0)

        style.configure('TNotebook.Tab', background=self.color.background_alt, foreground=self.color.foreground, padding=[10, 5], borderwidth=0, font=self.font.font_b)
        style.map('TNotebook.Tab', background=[("selected", self.color.background)], foreground=[("selected", self.color.foreground_alt)])

        style.configure('TFrame', background=self.color.background)

        style.configure('TButton', background=self.color.background, foreground=self.color.foreground, font=self.font.font_b, padding=[5, 5])
        style.map('TButton', background=[('active', self.color.background_alt), ('disabled', self.color.gray), ('hover', self.color.background)],
              foreground=[('disabled', self.color.foreground_alt)])

        style.configure("Custom.TLabelframe",
                    font=Font.font_b,
                    foreground=self.color.foreground,
                    background=self.color.background,
                    borderwidth=1,
                    relief="groove")

        style.configure("Custom.TLabelframe.Label",
                    font=Font.font_b,
                    foreground=self.color.foreground,
                    background=self.color.background)

        style.configure('TLabel', background=self.color.background, foreground=self.color.foreground, font=self.font.font_b)

        style.configure('TEntry', fieldbackground=self.color.background, foreground=self.color.foreground, font=self.font.font_b)

        # style.configure('TCheckbutton', background=self.color.background, foreground=self.color.foreground, font=self.font.font_b)
        # style.map('TCheckbutton', background=[('active', self.color.background_alt)], foreground=[('selected', self.color.foreground)])

class Color:
    primary = "#0d6efd"
    primary_hover = "#0b5ed7"
    primary_active = "#0a58ca"
    primary_disabled = "#8db9be"

    secondary = "#6c757d"
    secondary_hover = "#5c636a"
    secondary_active = "#565e64"
    secondary_disabled = "#aeb3b7"

    success = "#198754"
    success_hover = "#157347"
    success_active = "#146c43"
    success_disabled = "#82b593"

    info = "#0dcaf0"
    info_hover = "#31d2f2"
    info_active = "#3dd5f3"
    info_disabled = "#97e2ea"

    warning = "#ffc107"
    warning_hover = "#e0a800"
    warning_active = "#d39e00"
    warning_disabled = "#ffe499"

    danger = "#dc3545"
    danger_hover = "#c82333"
    danger_active = "#bd2130"
    danger_disabled = "#e99ea3"

    light = "#f8f9fa"
    light_hover = "#e2e6ea"
    light_active = "#d7dbdf"
    light_disabled = "#fdfdfe"

    dark = "#343a40"
    dark_hover = "#23272b"
    dark_active = "#1d2124"
    dark_disabled = "#6c757d"

    white = "#fff"
    gray = "#ccc"
    black = "#000"

def toggle_theme():
    global current_theme
    if current_theme == dark_theme:
        current_theme = light_theme
    else:
        current_theme = dark_theme
    current_theme.apply(style)

root = tk.Tk()
#[STYLE]########################################################################
style = ttk.Style()
style.theme_use('default')

light_theme = Theme('light', LightTheme(), Font())
dark_theme = Theme('dark', DarkTheme(), Font())

current_theme = dark_theme # dark_theme | light_theme
current_theme.apply(style)

all_styles = {
    'primary': (Color.primary, Color.primary_hover, Color.primary_active, Color.primary_disabled, Color.white),
    'secondary': (Color.secondary, Color.secondary_hover, Color.secondary_active, Color.secondary_disabled, Color.white),
    'success': (Color.success, Color.success_hover, Color.success_active, Color.success_disabled, Color.white),
    'info': (Color.info, Color.info_hover, Color.info_active, Color.info_disabled, Color.white),
    'warning': (Color.warning, Color.warning_hover, Color.warning_active, Color.warning_disabled, Color.black),
    'danger': (Color.danger, Color.danger_hover, Color.danger_active, Color.danger_disabled, Color.black),
    'light': (Color.light, Color.light_hover, Color.light_active, Color.light_disabled, Color.black),
    'dark': (Color.dark, Color.dark_hover, Color.dark_active, Color.dark_disabled, Color.white)
}

for style_name, colors in all_styles.items():
    style.configure(f'{style_name}.TButton', background=colors[0], foreground=colors[4], font=Font.font_b, padding=[5, 5])
    style.map(f'{style_name}.TButton',
              background=[('active', colors[2]), ('disabled', colors[3]), ('hover', colors[1])],
              foreground=[('disabled', Color.gray)])
    style.configure(f'{style_name}.TLabel', background=colors[0], foreground=colors[4], font=Font.font_b)
    style.configure(f'{style_name}.TFrame', background=colors[0])
    style.configure(f'{style_name}.TEntry', fieldbackground=colors[0], foreground=colors[4], font=Font.font_b)

#[ROOT]#########################################################################
#-------------------------------------------------------------------------------
root.title("Tkinter GUI")
root.resizable(0, 0)
root.geometry("854x480") # 854x480 | 1023x576 | 1280x720 | 1600x900 | 1920x1080
# root.configure(bg=Color.background)
#-------------------------------------------------------------------------------
# Notebook setup
tabControl = ttk.Notebook(root, style='TNotebook')
tab0, tab1 = ttk.Frame(tabControl, style='TFrame'), ttk.Frame(tabControl, style='TFrame')
tabControl.add(tab0, text='TAB-0')
tabControl.add(tab1, text='TAB-1')
tabControl.pack(expand=1, fill="both")
# ('secondary.TButton' if current_theme == light_theme else 'light.TButton')
btn_theme = ttk.Button(root, text="THEME", style=('dark.Tbutton' if current_theme.name == 'light' else 'light.TButton'), command=toggle_theme)
btn_theme.place(relx=1, rely=0, anchor="ne")

ttk.Button(root, text="THEME", style='TButton', command=toggle_theme).place(relx=1, rely=0, anchor="ne")

#[TAB0]#########################################################################
tab0.columnconfigure(0, weight=1)

# LABEL
lf_label = ttk.LabelFrame(tab0, text="LABELS", style='Custom.TLabelframe')
lf_label.grid(row=0, column=0, sticky="news")
lf_label.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

ttk.Label(lf_label, text="STANDARD", style='TLabel').grid(row=0, column=0, sticky="news", pady=5)
ttk.Label(lf_label, text="PRIMARY", style='primary.TLabel').grid(row=0, column=1, sticky="news", pady=5)
ttk.Label(lf_label, text="SECONDARY", style='secondary.TLabel').grid(row=0, column=2, sticky="news", pady=5)
ttk.Label(lf_label, text="SUCCESS", style='success.TLabel').grid(row=0, column=3, sticky="news", pady=5)
ttk.Label(lf_label, text="INFO", style='info.TLabel').grid(row=0, column=4, sticky="news", pady=5)
ttk.Label(lf_label, text="WARNING", style='warning.TLabel').grid(row=0, column=5, sticky="news", pady=5)
ttk.Label(lf_label, text="DANGER", style='danger.TLabel').grid(row=0, column=6, sticky="news", pady=5)
ttk.Label(lf_label, text="LIGHT", style='light.TLabel').grid(row=0, column=7, sticky="news", pady=5)
ttk.Label(lf_label, text="DARK", style='dark.TLabel').grid(row=0, column=8, sticky="news", pady=5)

# BTN
lf_btn = ttk.LabelFrame(tab0, text="BUTTONS", style='Custom.TLabelframe')
lf_btn.grid(row=1, column=0, sticky="news")
lf_btn.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

ttk.Button(lf_btn, text="STANDARD", style='TButton').grid(row=0, column=0, sticky="news")
ttk.Button(lf_btn, text="PRIMARY", style='primary.TButton').grid(row=0, column=1, sticky="news")
ttk.Button(lf_btn, text="SECONDARY", style='secondary.TButton').grid(row=0, column=2, sticky="news")
ttk.Button(lf_btn, text="SUCCESS", style='success.TButton').grid(row=0, column=3, sticky="news")
ttk.Button(lf_btn, text="INFO", style='info.TButton').grid(row=0, column=4, sticky="news")
ttk.Button(lf_btn, text="WARNING", style='warning.TButton').grid(row=0, column=5, sticky="news")
ttk.Button(lf_btn, text="DANGER", style='danger.TButton').grid(row=0, column=6, sticky="news")
ttk.Button(lf_btn, text="LIGHT", style='light.TButton').grid(row=0, column=7, sticky="news")
ttk.Button(lf_btn, text="DARK", style='dark.TButton').grid(row=0, column=8, sticky="news")

ttk.Button(lf_btn, text="DISABLED", style='TButton', state="disabled").grid(row=1, column=0, sticky="news")
ttk.Button(lf_btn, text="DISABLED", style='primary.TButton', state="disabled").grid(row=1, column=1, sticky="news")
ttk.Button(lf_btn, text="DISABLED", style='secondary.TButton', state="disabled").grid(row=1, column=2, sticky="news")
ttk.Button(lf_btn, text="DISABLED", style='success.TButton', state="disabled").grid(row=1, column=3, sticky="news")
ttk.Button(lf_btn, text="DISABLED", style='info.TButton', state="disabled").grid(row=1, column=4, sticky="news")
ttk.Button(lf_btn, text="DISABLED", style='warning.TButton', state="disabled").grid(row=1, column=5, sticky="news")
ttk.Button(lf_btn, text="DISABLED", style='danger.TButton', state="disabled").grid(row=1, column=6, sticky="news")
ttk.Button(lf_btn, text="DISABLED", style='light.TButton', state="disabled").grid(row=1, column=7, sticky="news")
ttk.Button(lf_btn, text="DISABLED", style='dark.TButton', state="disabled").grid(row=1, column=8, sticky="news")

# FRAME
lf_frame = ttk.LabelFrame(tab0, text="FRAMES", style='Custom.TLabelframe')
lf_frame.grid(row=2, column=0, sticky="news")
lf_frame.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

standard_f = ttk.Frame(lf_frame, style='TFrame')
standard_f.grid(row=0, column=0, sticky="news")
ttk.Label(standard_f, text="STANDARD", style='TLabel').pack(pady=5)
primary_f = ttk.Frame(lf_frame, style='primary.TFrame')
primary_f.grid(row=0, column=1, sticky="news")
ttk.Label(primary_f, text="PRIMARY", style='primary.TLabel').pack(pady=5)
secondary_f = ttk.Frame(lf_frame, style='secondary.TFrame')
secondary_f.grid(row=0, column=2, sticky="news")
ttk.Label(secondary_f, text="SECONDARY", style='secondary.TLabel').pack(pady=5)
success_f = ttk.Frame(lf_frame, style='success.TFrame')
success_f.grid(row=0, column=3, sticky="news")
ttk.Label(success_f, text="SUCCESS", style='success.TLabel').pack(pady=5)
info_f = ttk.Frame(lf_frame, style='info.TFrame')
info_f.grid(row=0, column=4, sticky="news")
ttk.Label(info_f, text="INFO", style='info.TLabel').pack(pady=5)
warning_f = ttk.Frame(lf_frame, style='warning.TFrame')
warning_f.grid(row=0, column=5, sticky="news")
ttk.Label(warning_f, text="WARNING", style='warning.TLabel').pack(pady=5)
danger_f = ttk.Frame(lf_frame, style='danger.TFrame')
danger_f.grid(row=0, column=6, sticky="news")
ttk.Label(danger_f, text="DANGER", style='danger.TLabel').pack(pady=5)
light_f = ttk.Frame(lf_frame, style='light.TFrame')
light_f.grid(row=0, column=7, sticky="news")
ttk.Label(light_f, text="LIGHT", style='light.TLabel').pack(pady=5)
dark_f = ttk.Frame(lf_frame, style='dark.TFrame')
dark_f.grid(row=0, column=8, sticky="news")
ttk.Label(dark_f, text="DARK", style='dark.TLabel').pack(pady=5)

# ENTRY
lf_entry = ttk.LabelFrame(tab0, text="ENTRIES", style='Custom.TLabelframe')
lf_entry.grid(row=3, column=0, sticky="news")
lf_entry.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

ttk.Entry(lf_entry, style='TEntry').grid(row=0, column=0, sticky="news")
ttk.Entry(lf_entry, style='primary.TEntry').grid(row=0, column=1, sticky="news")
ttk.Entry(lf_entry, style='secondary.TEntry').grid(row=0, column=2, sticky="news")
ttk.Entry(lf_entry, style='success.TEntry').grid(row=0, column=3, sticky="news")
ttk.Entry(lf_entry, style='info.TEntry').grid(row=0, column=4, sticky="news")
ttk.Entry(lf_entry, style='warning.TEntry').grid(row=0, column=5, sticky="news")
ttk.Entry(lf_entry, style='danger.TEntry').grid(row=0, column=6, sticky="news")
ttk.Entry(lf_entry, style='light.TEntry').grid(row=0, column=7, sticky="news")
ttk.Entry(lf_entry, style='dark.TEntry').grid(row=0, column=8, sticky="news")


# CHECKBUTTON
lf_checkbutton = ttk.LabelFrame(tab0, text="CHECKBUTTONS", style='Custom.TLabelframe')
lf_checkbutton.grid(row=5, column=0, sticky="news")
lf_checkbutton.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

# Configure the style for the TCheckbutton to mimic tk.Checkbutton
style.configure('Custom.TCheckbutton',
                activebackground= 'SystemButtonFace',
activeforeground= 'SystemWindowText',
anchor= 'center',
background= '#343a40',
bd= 2,
bg= '#343a40',
bitmap='',
border= 2,
borderwidth= 2,
command='',
compound= 'none',
cursor='',
disabledforeground= 'SystemDisabledText',
fg= '#f8f9fa',
font= 'Consolas 12 bold',
foreground= '#f8f9fa',
height= 0,
highlightbackground= 'SystemButtonFace',
highlightcolor= 'SystemWindowFrame',
highlightthickness= 1,
image='',
indicatoron= 1,
justify= 'center',
offrelief= 'raised',
offvalue= 0,
onvalue= 1,
overrelief='',
padx= 1,
pady= 1,
relief= 'flat',
selectcolor='#343a40',
selectimage='',
state= 'normal',
takefocus='',
# text= test,
textvariable='',
tristateimage='',
tristatevalue='',
underline= -1,
# variable= !checkbutton-1,
width= 0,
wraplength= 0)


# style.configure('Custom.TCheckbutton.TButton',
#                 background=Color.dark,              # Background color for the button
#                 foreground=Color.light,             # Foreground (text) color
#                 font=Font.font_b)                    # Position of the indicator relative to the text

cbtn = ttk.Checkbutton(lf_checkbutton, text="test", style="Custom.TCheckbutton")
cbtn.grid(row=1, column=0, sticky="news")

cbtn1 = tk.Checkbutton(lf_checkbutton, text="test", bg=Color.dark, fg=Color.light, selectcolor=Color.dark, font=Font.font_b)
cbtn1.grid(row=1, column=1, sticky="news")

print("Checkbutton Attributes:")
attributes = [
    'text', 'bg', 'fg', 'selectcolor', 'font', 'anchor', 'bd', 'bitmap',
    'borderwidth', 'command', 'compound', 'cursor', 'disabledforeground',
    'highlightbackground', 'highlightcolor', 'highlightthickness', 'image',
    'indicatoron', 'justify', 'offrelief', 'offvalue', 'onvalue', 'overrelief',
    'padx', 'pady', 'relief', 'state', 'takefocus', 'textvariable', 'tristateimage',
    'tristatevalue', 'underline', 'variable', 'width', 'wraplength'
]
params = [
    # "master",
    # "cnf",
    "activebackground",
    "activeforeground",
    "anchor",
    "background",
    "bd",
    "bg",
    "bitmap",
    "border",
    "borderwidth",
    "command",
    "compound",
    "cursor",
    "disabledforeground",
    "fg",
    "font",
    "foreground",
    "height",
    "highlightbackground",
    "highlightcolor",
    "highlightthickness",
    "image",
    "indicatoron",
    "justify",
    # "name",
    "offrelief",
    "offvalue",
    "onvalue",
    "overrelief",
    "padx",
    "pady",
    "relief",
    "selectcolor",
    "selectimage",
    "state",
    "takefocus",
    "text",
    "textvariable",
    "tristateimage",
    "tristatevalue",
    "underline",
    "variable",
    "width",
    "wraplength"
]


for attr in attributes:
    print(f"{attr}: {cbtn1.cget(attr)}")
print ("===================")
for attr in params:
    print(f"{attr}: {cbtn1.cget(attr)}")


root.mainloop()
