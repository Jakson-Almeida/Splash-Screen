import tkinter as tk
from tkinter.ttk import Progressbar
import threading
import time

def load_main_window():
    """Simulates a task and opens the main window."""
    # Simulate a task (e.g., loading resources)
    time.sleep(5)  # Replace with your actual loading logic

    # Destroy the splash screen and show the main window
    splash.destroy()
    main_window = tk.Tk()
    main_window.title("Main Application")
    main_window.geometry("600x400")
    tk.Label(main_window, text="Main Application Loaded!", font=("Arial", 16)).pack(pady=20)
    main_window.mainloop()

def start_loading():
    """Starts the loading process and runs the main application in a separate thread."""
    threading.Thread(target=load_main_window, daemon=True).start()

# Create the splash screen
splash = tk.Tk()
splash.title("Splash Screen")
splash.overrideredirect(True)
splash.geometry("400x300")
splash.attributes("-transparentcolor", "gray")
splash.configure(bg="gray")

# Center the splash screen
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
x = (screen_width - 400) // 2
y = (screen_height - 300) // 2
splash.geometry(f"400x300+{x}+{y}")

# Add a logo (optional)
logo = tk.PhotoImage(file="data/UFJF-logo.png")  # Replace with your logo file
tk.Label(splash, image=logo, bg="gray").pack(pady=20)

# Add an indeterminate progress bar
progress = Progressbar(splash, orient=tk.HORIZONTAL, length=300, mode="indeterminate")
progress.pack(pady=20)

# Start the progress bar animation
progress.start(10)  # Speed of the animation (lower value = faster)

# Start the loading process
splash.after(100, start_loading)

# Run the splash screen
splash.mainloop()
