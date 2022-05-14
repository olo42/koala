"""
Track and area planner main file
"""
from tkinter import *
from tkinter import ttk
import tkintermapview as mv

WIDTH = 1024
HEIGHT = 768

root = Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Koala - Tracks and Areas")

address = StringVar()

def set_location(map_view):
    try:
        value = address.get()
        map_view.set_address(value, marker=True)
        print(value)
    except ValueError:
        pass    

def build():
    
    mf = ttk.Frame(root, padding="3 3 12 12")
    mf.grid(column=0, row=0, sticky=(N, W, S, E))
    mf.columnconfigure(0, weight=1)
    mf.rowconfigure(0, weight=1)

    map_view = mv.TkinterMapView(mf, width=800, height=600, corner_radius=5)
    map_view.grid(columnspan=4, row=2, sticky=(W, E))

    ttk.Label(mf, text="Adress").grid(column=1, row=1, sticky=W)
    adr_entry = ttk.Entry(mf, width=50, textvariable=address)
    adr_entry.grid(column=2, row=1, sticky=W)
    ttk.Button(mf, text="Go", command=lambda:set_location(map_view)).grid(row=1, column=3, sticky=W)

    for child in mf.winfo_children(): child.grid_configure(padx=5, pady=5)

    return mf


def main():
    mf = build()
    #map_view = mf.children["map_view"]
    
    
    root.mainloop()




if __name__ == "__main__":
    main()