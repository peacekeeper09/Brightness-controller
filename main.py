import tkinter as tk
import screen_brightness_control as sbc

class BrightnessController:
    def __init__(self, master):
        self.master = master
        master.title("Brightness Controller")

        # Add a label that displays the current brightness value
        self.brightness_label = tk.Label(master, text="Brightness: {}%".format(sbc.get_brightness()))
        self.brightness_label.pack()

        # Use a horizontal slider instead of a vertical slider
        self.scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.update_brightness)
        self.scale.set(sbc.get_brightness())
        self.scale.pack(fill=tk.X, padx=10)

        # Add keyboard shortcuts to increase/decrease brightness
        master.bind("<Control-Shift-Left>", self.decrease_brightness)
        master.bind("<Control-Shift-Right>", self.increase_brightness)

        # Add a button to reset the brightness to its default value
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_brightness)
        self.reset_button.pack(pady=10)

    def update_brightness(self, value):
        sbc.set_brightness(int(value))
        self.brightness_label.config(text="Brightness: {}%".format(sbc.get_brightness()))

    def increase_brightness(self, event=None):
        current_value = self.scale.get()
        if current_value < 100:
            new_value = current_value + 1
            self.scale.set(new_value)
            self.update_brightness(new_value)

    def decrease_brightness(self, event=None):
        current_value = self.scale.get()
        if current_value > 0:
            new_value = current_value - 1
            self.scale.set(new_value)
            self.update_brightness(new_value)

    def reset_brightness(self):
        sbc.set_brightness(50)
        self.scale.set(50)
        self.brightness_label.config(text="Brightness: {}%".format(sbc.get_brightness()))

root = tk.Tk()
app = BrightnessController(root)
root.geometry("500x100")
root.mainloop()
