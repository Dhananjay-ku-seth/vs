import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S %p')  # %p for AM/PM
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Update every second

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150")
root.configure(bg='black')

clock_label = tk.Label(root, font=('Helvetica', 36, 'bold'), bg='black', fg='white')
clock_label.pack(expand=True)

update_clock()

root.mainloop()
