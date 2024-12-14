import tkinter as tk
import ctypes

# Get the handle for the console window
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 0  # Constant to hide the window
SW_SHOW = 5  # Constant to show the window

console_handle = kernel32.GetConsoleWindow()  # Get console window handle


def toggle_console():
    """Toggle the console window visibility."""
    if user32.IsWindowVisible(console_handle):
        user32.ShowWindow(console_handle, SW_HIDE)  # Hide the console
    else:
        user32.ShowWindow(console_handle, SW_SHOW)  # Show the console


# Create a Tkinter window
root = tk.Tk()
root.title("Toggle Console Example")
root.geometry("300x150")

# Add a button to toggle the console visibility
toggle_button = tk.Button(root, text="Toggle Console", command=toggle_console)
toggle_button.pack(pady=20)

# Run the Tkinter application
root.mainloop()
