import tkinter as tk
from tkinter import messagebox
import os

def start_streamlit():
    os.system("streamlit run chatbot_web.py")
    root.quit()

def show_tooltip(event):
    messagebox.showinfo("Info", "Klicka för att starta AI-assistenten")

root = tk.Tk()
root.title("AI-assistent")

# Set an icon for the window using a .png file
icon = tk.PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, icon)

# Change the button style
start_button = tk.Button(root, text="AI-assistent", command=start_streamlit, bg="#00bfff", font=('Helvetica', 12, 'bold'))
start_button.pack(pady=10, padx=20)

# Add a tooltip to the button
start_button.bind("<Enter>", show_tooltip)

root.mainloop()
