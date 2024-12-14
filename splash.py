import tkinter as tk
from tkinter.ttk import Progressbar
import time

def load_main_window():
    """Function to display the main application window."""
    splash.destroy()  # Destroy the splash screen
    
    # Main window
    main_window = tk.Tk()
    main_window.title("Main Application")
    main_window.geometry("600x400")
    
    # Example content for the main window
    tk.Label(main_window, text="Welcome to the Main Application!", font=("Arial", 16)).pack(pady=20)
    main_window.mainloop()


# Create the splash screen
splash = tk.Tk()
splash.title("Splash Screen")

# Remove window border and buttons
splash.overrideredirect(True)

# Set the size and center the splash window
splash.geometry("400x300")
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
x = (screen_width - 400) // 2
y = (screen_height - 300) // 2
splash.geometry(f"400x300+{x}+{y}")

# Make the window transparent (background color with alpha)
splash.attributes("-transparentcolor", "gray")

# Set background color to match transparency
splash.configure(bg="gray")

# Add a logo (transparent PNG)
logo = tk.PhotoImage(file="your_logo.png")  # Replace with your logo file path
tk.Label(splash, image=logo, bg="gray").pack(pady=20)

# Add a progress bar
progress = Progressbar(splash, orient=tk.HORIZONTAL, length=300, mode="determinate")
progress.pack(pady=20)

# Simulate loading process
def update_progress():
    for i in range(101):
        time.sleep(0.03)  # Simulate loading time
        progress["value"] = i
        splash.update_idletasks()
    load_main_window()

# Call the loading process
splash.after(100, update_progress)

# Run the splash screen
splash.mainloop()
