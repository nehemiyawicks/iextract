import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from backup_handler import create_backup
from message_parser import extract_messages
import os
import subprocess
from PIL import Image, ImageTk  # Importing Pillow for image support

def check_device_connected():
    """Check if the iPhone is connected by running a libimobiledevice command."""
    try:
        result = subprocess.run(["ideviceinfo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            return False
        return True
    except Exception as e:
        print(f"Error checking device connection: {e}")
        return False

def start_backup(progress_bar, progress_label):
    """Start the backup process and show progress updates."""
    if not check_device_connected():
        messagebox.showwarning("Device Not Connected", "Please connect your iPhone and trust this computer.")
        return

    backup_dir = filedialog.askdirectory(title="Select Folder to Store Backup")
    if not backup_dir:
        return

    progress_label.config(text="Starting Backup...")
    progress_bar.start()

    backup_success = create_backup(backup_dir, progress_bar)
    if not backup_success:
        messagebox.showerror("Backup Failed", "An error occurred while creating the backup.")
        progress_bar.stop()
        return
    
    progress_label.config(text="Extracting Messages...")
    messages = extract_messages(backup_dir)
    
    if messages:
        csv_file_path = os.path.join(backup_dir, "messages.csv")
        with open(csv_file_path, "w", newline="") as file:
            file.write("Message ID,Text,Timestamp\n")
            for msg in messages:
                file.write(f"{msg[0]},{msg[1]},{msg[2]}\n")
        
        messagebox.showinfo("Success", f"Messages extracted successfully and saved to {csv_file_path}")
    else:
        messagebox.showerror("No Messages", "No messages were found in the backup.")
    
    progress_bar.stop()

# GUI Setup
app = tk.Tk()
app.title("iExtract - iPhone Message Extractor")

# Set the window and taskbar icon (use .ico format)
app.iconbitmap("assets/icons/backup_icon.ico")

# Make the app wider
app.geometry("800x400")

# Load background image (now a PNG file)
bg_image = Image.open("assets/images/background.png")  # Adjust the image path and extension
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(app, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Set background color for widgets
app.configure(bg="#f0f0f0")

# Title Label
label = tk.Label(app, text="Welcome to iExtract!", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333333")
label.pack(pady=20)

# Progress Label
progress_label = tk.Label(app, text="", font=("Arial", 14), bg="#f0f0f0", fg="#333333")
progress_label.pack(pady=5)

# Progress Bar
progress_bar = ttk.Progressbar(app, orient="horizontal", length=600, mode="determinate")
progress_bar.pack(pady=20)

# Load Button Icon (for .ico support)
backup_icon = Image.open("assets/icons/backup_icon.ico")
backup_icon = ImageTk.PhotoImage(backup_icon)

# Start Backup Button with Icon
backup_button = tk.Button(
    app, 
    text="Start Backup and Extract", 
    command=lambda: start_backup(progress_bar, progress_label), 
    font=("Arial", 12),
    bg="#4CAF50",  # Green background
    fg="white",  # White text
    relief="raised",  # Raised effect for button
    padx=10, pady=5,
    image=backup_icon,  # Adding the icon to the button
    compound="left"  # Position icon to the left of the text
)
backup_button.pack(pady=20)

# Footer Label
footer_label = tk.Label(
    app, 
    text="iExtract - v1.0.0", 
    font=("Arial", 10), 
    bg="#f0f0f0", 
    fg="#777777"
)
footer_label.pack(side="bottom", pady=10)

# Run the GUI
app.mainloop()
