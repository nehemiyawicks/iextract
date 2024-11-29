import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from backup_handler import create_backup
from message_parser import extract_messages
import subprocess

def resource_path(relative_path):
    """ 
    Get the absolute path to a resource, works for both development and PyInstaller 
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Fallback to the current working directory if not bundled with PyInstaller
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def check_device_connected():
    """
    Check if the iPhone is connected by running a libimobiledevice command.
    """
    try:
        # Run ideviceinfo command to check if the device is connected
        result = subprocess.run(["ideviceinfo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # If the return code is non-zero, the device is not connected or trust dialog is not accepted
        if result.returncode != 0:
            return False
        return True
    except Exception as e:
        # Print error if any issue occurs while checking device connection
        print(f"Error checking device connection: {e}")
        return False

def start_backup(progress_bar, progress_label):
    """
    Handle the entire backup and message extraction process:
    - Check device connection
    - Ask user for backup directory
    - Perform the backup
    - Extract messages from the backup
    - Save messages to a CSV file
    """
    # Step 1: Check if iPhone is connected
    if not check_device_connected():
        # Show a warning if the device is not connected
        messagebox.showwarning("Device Not Connected", "Please connect your iPhone and trust this computer.")
        return  # Exit if device is not connected

    # Ask the user to select a folder to store the backup
    backup_dir = filedialog.askdirectory(title="Select Folder to Store Backup")
    
    if not backup_dir:
        return  # If no folder is selected, exit the function
    
    # Step 2: Create the backup using libimobiledevice
    messagebox.showinfo("Backup Process", "Starting iPhone backup...")
    progress_bar['value'] = 0
    progress_label.config(text="Starting backup...")

    # Call create_backup function from the backup_handler module to perform the backup
    backup_success = create_backup(backup_dir, progress_bar)
    
    # Show error message if backup fails
    if not backup_success:
        messagebox.showerror("Backup Failed", "An error occurred while creating the backup.")
        return

    # Step 3: Extract messages from the backup
    messagebox.showinfo("Extracting Messages", "Extracting messages from the backup...")
    progress_label.config(text="Extracting messages...")

    # Call extract_messages function from the message_parser module to retrieve messages
    messages = extract_messages(backup_dir)

    if messages:
        # Step 4: Save the extracted messages to a CSV file
        csv_file_path = os.path.join(backup_dir, "messages.csv")
        with open(csv_file_path, "w", newline="") as file:
            file.write("Message ID,Text,Timestamp\n")
            for msg in messages:
                file.write(f"{msg[0]},{msg[1]},{msg[2]}\n")
        
        # Update the progress bar and label
        progress_bar['value'] = 100
        progress_label.config(text=f"Messages extracted successfully and saved to {csv_file_path}")
    else:
        # If no messages are found, show a message in the progress label
        progress_bar['value'] = 100
        progress_label.config(text="No messages found.")

# GUI Setup
app = tk.Tk()
app.title("iExtract - iPhone Message Extractor")
app.geometry("500x300")

# Set the application icon
app_icon = resource_path("assets/icons/backup_icon.ico")
app.wm_iconbitmap(app_icon)  # This will use the bundled icon

# Set background color
app.configure(bg="lightblue")  # Set the background color to light blue

# Title Label for the main window
label = tk.Label(app, text="Welcome to iExtract!", font=("Arial", 14), bg="lightblue")
label.pack(pady=10)

# Progress bar and progress label for displaying the backup and extraction process
progress_bar = ttk.Progressbar(app, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)
progress_label = tk.Label(app, text="", font=("Arial", 10), bg="lightblue")
progress_label.pack()

# Backup Button to start the backup and extraction process
backup_button = tk.Button(app, text="Start Backup and Extract", command=lambda: start_backup(progress_bar, progress_label), font=("Arial", 12))
backup_button.pack(pady=20)

# Start the main GUI loop
app.mainloop()
