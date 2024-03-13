import tkinter as tk
import time
import math

def update_clock():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Calculate angles for hour, minute, and second hands
    hour_angle = (hour % 12) * 30 + minute * 0.5
    minute_angle = minute * 6 + second * 0.1
    second_angle = second * 6

    # Update clock hands
    canvas.delete("hands")
    draw_hand(hour_angle, 50, "black", 6)
    draw_hand(minute_angle, 75, "black", 4)
    draw_hand(second_angle, 90, "red", 2)

    # Update every 1000 milliseconds (1 second)
    root.after(1000, update_clock)

def draw_hand(angle, length, color, width):
    x = center_x + length * math.sin(math.radians(angle))
    y = center_y - length * math.cos(math.radians(angle))
    canvas.create_line(center_x, center_y, x, y, width=width, fill=color, tags="hands")

root = tk.Tk()
root.title("Analog Clock")

# Set canvas size
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Calculate center of the canvas
center_x = 150
center_y = 150

# Draw clock outline
canvas.create_oval(center_x - 100, center_y - 100, center_x + 100, center_y + 100, width=2, outline="black")

# Draw clock numbers
for i in range(1, 13):
    angle = math.radians(30 * i)
    x = center_x + 90 * math.sin(angle)
    y = center_y - 90 * math.cos(angle)
    canvas.create_text(x, y, text=str(i), font=("Arial", 12), fill="black")

# Update clock
update_clock()

root.mainloop()
