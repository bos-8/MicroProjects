import tkinter as tk
from tkinter import ttk
from tkinter import *

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

        style.configure('TNotebook.Tab', background=self.color.background_alt, foreground=self.color.foreground, padding=[10, 5], borderwidth=0, font=self.font.font_b)
        style.map('TNotebook.Tab', background=[("selected", self.color.background)], foreground=[("selected", self.color.foreground_alt)])

        style.configure('TFrame', background=self.color.background)

        style.configure('TButton', background=self.color.background, foreground=self.color.foreground, font=self.font.font_b, padding=[5, 5])
        style.map('TButton', background=[('active', self.color.background_alt), ('disabled', self.color.gray), ('hover', self.color.background)],
              foreground=[('disabled', self.color.foreground_alt)])

        style.configure('TMenubutton', background=self.color.background, foreground=self.color.foreground, font=self.font.font_b, borderwidth=1,  padding=[5,5], width=10, arrowcolor=self.color.foreground,
                selectbackground=self.color.background_alt,
                selectforeground=self.color.foreground_alt, relief= "raised")

        style.map('TMenubutton', background=[('active', self.color.background_alt), ('disabled', self.color.gray), ('hover', self.color.background)],
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

        style.configure('TCombobox',
                foreground=self.color.foreground,
                background=self.color.background,
                fieldbackground=self.color.background,
                arrowcolor=self.color.foreground,
                selectbackground=self.color.background_alt,
                selectforeground=self.color.foreground_alt,
                font=Font.font_b)

        style.map('TCombobox', fieldbackground=[('active', self.color.background), ('disabled', Color.dark_disabled)], arrowcolor=[('active', Color.light_active)])

        root.option_add('*TCombobox*Listbox.background', self.color.background)  # Dark background
        root.option_add('*TCombobox*Listbox.foreground', self.color.foreground)  # Light foreground
        root.option_add('*TCombobox*Listbox.font', Font.font_b)  # Font for dropdown list
        root.option_add('*TCombobox*Listbox.selectBackground', self.color.background_alt)  # Selected background
        root.option_add('*TCombobox*Listbox.selectForeground', self.color.foreground_alt)  # Selected foreground


        style.configure('TRadiobutton', background=Color.dark, foreground=Color.light, font=Font.font_b, selectcolor=Color.dark)

        root.option_add('*Menu.background', Color.dark)
        root.option_add('*Menu.foreground', Color.light)
        root.option_add('*Menu.font', Font.font_b)
        root.option_add('*Menu.selectColor', Color.light)
        root.option_add('*Menu.activeBackground', Color.dark_active)
        root.option_add('*Menu.activeForeground', Color.light)
        root.option_add('*Menu.tearOff', 0)

        style.configure('Custom.TCheckbutton', background=Color.dark, anchor='center', foreground=Color.light, font=Font.font_b)
        style.map('Custom.TCheckbutton', background=[('active', Color.dark_active)], foreground=[('selected', Color.light)])

        style.configure("Treeview",
                background=Color.dark,
                fieldbackground=Color.dark,
                foreground=Color.light,
                font=Font.font_b,
                rowheight=25,
                borderwidth=0,
                highlightthickness=0,
                selectbackground=Color.dark_active,
                selectforeground=Color.light)

        style.configure("Treeview.Heading",
                        background=Color.dark_active,
                        foreground=Color.light,
                        font=Font.font_b,
                        borderwidth=0)

        style.map("Treeview.Heading",
                background=[("active", Color.dark_hover)])

        style.map("Treeview",
                background=[("selected", Color.dark_hover)],
                foreground=[("selected", Color.light)])

        style.configure("TScrollbar", gripcount=0,
                        background="#222", darkcolor="#222", lightcolor="#333",
                        troughcolor="#1E1E1E", bordercolor="#1E1E1E", arrowcolor="#FFFFFF")

        style.map("TScrollbar",
                    background=[('active', "#333"), ('disabled', "#222")],
                    darkcolor=[('active', "#333"), ('disabled', "#222")],
                    lightcolor=[('active', "#333"), ('disabled', "#222")],
                    troughcolor=[('active', "#1E1E1E"), ('disabled', "#1E1E1E")],
                    bordercolor=[('active', "#1E1E1E"), ('disabled', "#1E1E1E")],
                    arrowcolor=[('active', "#FFFFFF"), ('disabled', "#FFFFFF")])

        style.configure("Horizontal.TScale",
                background=Color.dark, troughcolor=Color.dark_active,
                 relief="flat")

        style.map("Horizontal.TScale",
                background=[("active", Color.dark_active)],
                troughcolor=[("active", Color.dark)])

        style.configure("TProgressbar",
                        lightcolor=Color.light,
                        darkcolor=Color.dark_active,
                        troughcolor=Color.dark,
                        background=Color.dark_active,
                        thickness=20)

        style.configure("Custom.TPanedwindow",
                background=Color.dark,
                gripcolor=Color.dark_active)

        style.configure("Custom.TPanedwindow.Horizontal",
                        background=Color.dark)

        style.configure("TSeparator",
                background=Color.warning,
                troughcolor=Color.warning,
                borderwidth=5)

        style.configure("TSpinbox",
                fieldbackground=Color.dark,
                background=Color.dark,
                foreground=Color.light,
                borderwidth=1,
                relief="flat",
                arrowcolor=Color.light)
        style.map("TSpinbox",
                foreground=[("focus", Color.light)],
                background=[("focus", Color.dark_active)],
                fieldbackground=[("focus", Color.dark_active)],
                arrowcolor=[('active', "#FFFFFF"), ('disabled', "#FFFFFF")])

        style.configure("TSpinbox.field", fg=Color.light, bg=Color.dark, font=Font.font_b)

        style.configure("TSizegrip", background=Color.dark, activebackground=Color.dark_active)

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
root.geometry("854x800") # 854x480 | 1023x576 | 1280x720 | 1600x900 | 1920x1080
#-------------------------------------------------------------------------------
# Notebook setup
tabControl = ttk.Notebook(root, style='TNotebook')
tab0, tab1 = ttk.Frame(tabControl, style='TFrame'), ttk.Frame(tabControl, style='TFrame')

tabControl.add(tab1, text='TAB-1')
tabControl.add(tab0, text='TAB-0')

tabControl.pack(expand=1, fill="both")
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

ttk.Checkbutton(lf_checkbutton, text="test", style="Custom.TCheckbutton").grid(row=1, column=0, sticky="news")
tk.Checkbutton(lf_checkbutton, text="test", bg=Color.dark, fg=Color.light, selectcolor=Color.dark, font=Font.font_b).grid(row=1, column=1, sticky="news")

# RADIOBUTTON
lf_radiobutton = ttk.LabelFrame(tab0, text="RADIOBUTTONS", style='Custom.TLabelframe')
lf_radiobutton.grid(row=6, column=0, sticky="news")
lf_radiobutton.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

ttk.Radiobutton(lf_radiobutton, text="test", style="TCheckbutton").grid(row=2, column=0, sticky="news")
tk.Radiobutton(lf_radiobutton, text="test", bg=Color.dark, fg=Color.light, selectcolor=Color.dark, font=Font.font_b).grid(row=2, column=1, sticky="news")

# COMBOBOX
lf_combobox = ttk.LabelFrame(tab0, text="COMBOBOXES", style='Custom.TLabelframe')
lf_combobox.grid(row=7, column=0, sticky="news")
lf_combobox.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

ttk.Combobox(lf_combobox, values=["OPT1", "OPT2", "OPT3"], style='TCombobox').grid(row=3, column=0, sticky="news")

# MENUBTN
lf_menu = ttk.LabelFrame(tab0, text="MENUBUTTON", style='Custom.TLabelframe')
lf_menu.grid(row=8, column=0, sticky="news")
lf_menu.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

menubtn = ttk.Menubutton(lf_menu, text="MENUBTN", style='TButton')
menubtn.grid(row=4, column=0, sticky="news")

# menu = tk.Menu(menubtn, tearoff=0, bg=Color.dark, fg=Color.light, font=Font.font_b, activebackground=Color.dark_active, activeforeground=Color.light, relief="flat" )
menu = tk.Menu(menubtn)
menu.add_command(label="Option 1", command=lambda: menubtn.configure(text="Option 1"))
menu.add_command(label="Option 2", command=lambda: menubtn.configure(text="Option 2"))
menu.add_command(label="Option 3", command=lambda: menubtn.configure(text="Option 3"))
menu.add_separator()
menu.add_checkbutton(label="Check 1", onvalue=1, offvalue=0, command=lambda: print("Check 1"))

menubtn["menu"] = menu

selected_option = tk.StringVar(value="Option 1", name="selected_option", )
menuop = ttk.OptionMenu(lf_menu, selected_option, "Option 1", "Option 1", "Option 2", "Option 3", style='TMenubutton')
menuop.grid(row=4, column=2, sticky="news")


menubtn1 = ttk.Menubutton(lf_menu, text="MENUBTN2", menu=menu)
menubtn1.grid(row=4, column=3, sticky="news")

# LISTBOX
lf_listbox = ttk.LabelFrame(tab0, text="LISTBOX", style='Custom.TLabelframe')
lf_listbox.grid(row=9, column=0, sticky="news")
lf_listbox.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

listbox = tk.Listbox(lf_listbox, bg=Color.dark, fg=Color.light, font=Font.font_b, selectbackground=Color.dark_active, selectforeground=Color.light, height=3, borderwidth=0, highlightthickness=0)
listbox.grid(row=0, column=0, sticky="news")
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.insert(3, "Option 3")

# CANVAS
lf_canvas = ttk.LabelFrame(tab0, text="CANVAS", style='Custom.TLabelframe')
lf_canvas.grid(row=10, column=0, sticky="news")
lf_canvas.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

canvas = tk.Canvas(lf_canvas, bg=Color.dark, width=100, height=50, highlightthickness=0)
canvas.grid(row=0, column=0, sticky="news")

canvas.create_text(50, 25, text="CANVAS", fill=Color.light, font=Font.font_b)

# SCROLLBAR
lf_scrollbar = ttk.LabelFrame(tab0, text="SCROLLBAR", style='Custom.TLabelframe')
lf_scrollbar.grid(row=11, column=0, sticky="news")
lf_scrollbar.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

canvas1 = tk.Canvas(lf_scrollbar, bg=Color.dark, width=100, height=100, highlightthickness=0)
canvas1.grid(row=0, column=0, sticky="news")

v_scrollbar = ttk.Scrollbar(lf_scrollbar, orient="vertical", command=canvas1.yview, style='Custom.Vertical.TScrollbar')
v_scrollbar.grid(row=0, column=1, sticky="nsw")

h_scrollbar = ttk.Scrollbar(lf_scrollbar, orient="horizontal", command=canvas1.xview, style='Custom.Horizontal.TScrollbar')
h_scrollbar.grid(row=1, column=0, sticky="ew")

canvas1.config(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
canvas1.create_rectangle(10, 10, 110, 110, outline=Color.light, fill=Color.dark_active)
canvas1.create_text(20, 25, text="CAN", fill=Color.light, font=Font.font_b)
canvas1.create_text(200, 25, text="VAS", fill=Color.light, font=Font.font_b)

#[TAB1]#########################################################################
tab1.columnconfigure(0, weight=1)

treev = ttk.Treeview(tab1, selectmode ='browse')
treev.grid(row=0, column=0, sticky="news")
verscrlbar = ttk.Scrollbar(tab1, orient ="vertical", command = treev.yview)
verscrlbar.grid(row=0, column=1, sticky="wns")
treev.configure(yscrollcommand = verscrlbar.set)
# treev.bind('<Configure>', lambda e: treev.configure(scrollregion=treev.bbox("all")))
treev["columns"] = ("1", "2", "3")
treev['show'] = 'headings'
treev.column("1", anchor ='c')
treev.column("2",  anchor ='c')
treev.column("3",  anchor ='c')
treev.heading("1", text ="#")
treev.heading("2", text = "NAME")
treev.heading("3", text = "NUMBER")
for i in range(20):
    treev.insert("", 'end', text ="L1", values =(i, f"NAME{i}", f"NUMBER{i}"))


lf_labelScale = ttk.LabelFrame(tab1, text="LABELSCALE", style='Custom.TLabelframe')
lf_labelScale.grid(row=1, column=0, sticky="news")
lf_labelScale.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

ttk.LabeledScale(lf_labelScale, from_=0, to=100).grid(row=1, column=1, columnspan=3, sticky="news")

ttk.Scale(lf_labelScale, from_=0, to=100, orient="horizontal", command=lambda v: progressbar.config(value=float(v))).grid(row=2, column=1, columnspan=3, sticky="news")

ttk.Label(lf_labelScale, text="HORIZONTAL", style='TLabel').grid(row=2, column=6, sticky="news")

lf_pbar = ttk.LabelFrame(tab1, text="PROGRESSBAR", style='Custom.TLabelframe')
lf_pbar.grid(row=2, column=0, sticky="news")
lf_pbar.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

progressbar = ttk.Progressbar(lf_pbar, orient="horizontal", value=69, length=200, mode="determinate", style="TProgressbar")
progressbar.grid(row=0, column=0, sticky="news")

lf_Panedwindow = ttk.LabelFrame(tab1, text="PANEDWINDOW", style='Custom.TLabelframe')
lf_Panedwindow.grid(row=3, column=0, sticky="news")
lf_Panedwindow.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

pwindow = ttk.Panedwindow(lf_Panedwindow, orient=HORIZONTAL, style="Custom.TPanedwindow")
pwindow.grid(row=3, column=0, sticky="news")

ttk.Label(pwindow, text="Pane 1", style='TLabel').pack(side=LEFT)

lf_separator = ttk.LabelFrame(tab1, text="SEPARATOR", style='Custom.TLabelframe')
lf_separator.grid(row=4, column=0, sticky="news")
lf_separator.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

ttk.Separator(lf_separator, orient=HORIZONTAL).grid(row=0, column=0, sticky="news", pady=5, padx=5)
ttk.Separator(lf_separator, orient=VERTICAL).grid(row=0, column=1, sticky="news", pady=5, padx=5)

ttk.Label(lf_separator, text="SEPARATOR", style='TLabel').grid(row=0, column=2, sticky="news")

lf_spinbox = ttk.LabelFrame(tab1, text="SPINBOX", style='Custom.TLabelframe')
lf_spinbox.grid(row=5, column=0, sticky="news")
lf_spinbox.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

ttk.Spinbox(lf_spinbox, from_=0, to=100).grid(row=0, column=0, sticky="news")

lf_scale = ttk.LabelFrame(tab1, text="SCALE", style='Custom.TLabelframe')
lf_scale.grid(row=6, column=0, sticky="news")
lf_scale.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)

ttk.Sizegrip(lf_scale).grid(row=0, column=0, columnspan=2, sticky="news")

# [v] Button
# [v] Checkbutton
# [v] Entry
# [v] Frame
# [v] Label
# [v] LabelFrame
# [v] Menubutton
# [v] PanedWindow
# [v] Radiobutton
# [v] Scale
# [v] Scrollbar
# [v] Spinbox
# [v] ttk.Combobox
# [v] ttk.Notebook
# [v] ttk.Progressbar
# [v] ttk.Separator
# [v] ttk.Sizegrip
# [v] ttk.Treeview

#[MAIN-LOOP]####################################################################
root.mainloop()