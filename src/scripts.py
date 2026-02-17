import tkinter as tk, shutil, os
from tkinter import filedialog

def add_timer():
    result = {}

    def select_song():
        path = filedialog.askopenfilename(
            title="Select song",
            filetypes=[("Audio files", "*.mp3 *.wav"), ("All files", "*.*")]
        )
        if path:
            song_label.config(text=path)
            result["song"] = path

    def save():
        try:
            result["name"] = name_entry.get()
            min = int(min_entry.get())
            sec = int(sec_entry.get())
            result["duration"] = min*60+sec
        except:
            print("Error")
            return
        
        original = result["song"]

        os.makedirs("assets/sounds", exist_ok=True)

        filename = os.path.basename(original)
        new_path = os.path.join("assets/sounds", filename)

        shutil.copy(original, new_path)

        result["song"] = filename
        
        root.destroy()

    root = tk.Tk()
    root.title("Add new timer")
    root.geometry("400x250")

    tk.Label(root, text="Name: ").pack(anchor="w", padx=10, pady=(10, 0))
    name_entry = tk.Entry(root)
    name_entry.pack(fill="x", padx=10)

    tk.Label(root, text="Duration time: ").pack(anchor="w", padx=10, pady=(10, 0))
    time_frame = tk.Frame(root)
    time_frame.pack(padx=10, anchor="w")

    min_entry = tk.Entry(time_frame, width=5)
    min_entry.pack(side="left")
    tk.Label(time_frame, text="min").pack(side="left", padx=5)

    sec_entry = tk.Entry(time_frame, width=5)
    sec_entry.pack(side="left")
    tk.Label(time_frame, text="sec").pack(side="left", padx=5)

    tk.Button(root, text="Select song", command=select_song).pack(pady=15)
    song_label = tk.Label(root, text="No song selected", wraplengt=350)
    song_label.pack()

    tk.Button(root, text="SAVE", command=save).pack()

    root.mainloop()

    return result


import tkinter as tk


def choose_preset(presets):
    selected = {"value": None}
    index = 0

    root = tk.Tk()
    root.title("Choose preset")
    root.geometry("350x200")
    root.resizable(False, False)

    name_label = tk.Label(root, font=("Arial", 14))
    duration_label = tk.Label(root)
    song_label = tk.Label(root)

    name_label.pack(pady=10)
    duration_label.pack()
    song_label.pack()

    def update():
        p = presets[index]
        name_label.config(text=p["name"])
        min = p["duration"]//60
        sec = p["duration"]%60
        h = min//60
        if h!=0:
            min-=h*60
            duration_label.config(text=f"Duration: {h}:{min}:{sec}")
        else:
            duration_label.config(text=f"Duration: {min}:{sec}")
        song_label.config(text=f"Song: {p['song']}")

    def up(event=None):
        nonlocal index
        index = (index - 1) % len(presets)
        update()

    def down(event=None):
        nonlocal index
        index = (index + 1) % len(presets)
        update()

    def add():
        selected["value"] = presets[index]
        root.destroy()

    tk.Button(root, text="Add", command=add).pack(pady=15)

    root.bind("<Up>", up)
    root.bind("<Down>", down)

    update()
    root.mainloop()

    return selected["value"]
