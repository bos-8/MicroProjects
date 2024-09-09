# import subprocess

# # Define your public DNS, username, and password
# public_dns = "DESKTOP-JC5NS7P"
# username = "bos"
# password = "bos"

# subprocess.run(['cmdkey', '/generic:TERMSRV', f'/user:{username}', f'/pass:{password}'])
# subprocess.run(['mstsc', f'/v:{public_dns}'])
# subprocess.run(['cmdkey', '/delete:TERMSRV'])

# ==============================================================================
import tkinter as tk
from tkinter import ttk, PhotoImage

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
root.title("INSTANCE JUMP STARTER")
root.resizable(0, 0)
root.geometry("800x400")
root.configure(bg="#333")

style = ttk.Style()
style.theme_use('default')

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



#[root]#########################################################################
root.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
#---INSTANCES------------------------------------------------------------------
frame = tk.Frame(root, bg=Theme.background_alt)
frame.grid(row=1, rowspan=8, column=0, columnspan=10, sticky="nsew", pady=8, padx=15)
frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

canvas = tk.Canvas(frame, bg=Theme.background_alt, highlightthickness=0, border=0, height=220)
canvas.grid(row=1, column=0, columnspan=6, sticky="nsew")
# canvas.config(height=220, border=0)

# Add scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview, style="TScrollbar")
scrollbar.grid(row=1, column=6, sticky="ns")
# scrollbar.place(relx=1, rely=0, anchor="ne", relheight=1)

scrollbar1 = ttk.Scrollbar(frame, orient="horizontal", command=canvas.xview, style="TScrollbar")
scrollbar1.grid(row=2, column=0, columnspan=6, sticky="ew")
# Configure the canvas to work with the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas
instance_frame = tk.Frame(canvas, bg=Theme.background_alt)
canvas.create_window((0, 0), window=instance_frame, anchor="nw")

instance_frame.grid_columnconfigure(0, minsize=298)
for i in range(10):
    tk.Label(instance_frame, text=f"ROW {i+1}", bg=Theme.background_alt, fg="white", font=Theme.font).grid(row=i, column=0, sticky="nsew", padx=2, pady=2)

root.mainloop()