import tkinter as tk
from tkinter import filedialog, messagebox
from backup_handler import create_backup
from message_parser import extract_messages
import os
import subprocess

def check_device_connected():
    """
    Check if the iPhone is connected by running a libimobiledevice command.
    """
    try:
        # Run ideviceinfo to check if the device is connected
        result = subprocess.run(["ideviceinfo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            return False  # iPhone is not connected or trust dialog not accepted
        return True
    except Exception as e:
        print(f"Error checking device connection: {e}")
        return False

def start_backup():
    # Step 1: Check if iPhone is connected
    if not check_device_connected():
        messagebox.showwarning("Device Not Connected", "Please connect your iPhone and trust this computer.")
        return  # Exit if device is not connected

    # Ask the user to select a folder to store the backup
    backup_dir = filedialog.askdirectory(title="Select Folder to Store Backup")
    
    if not backup_dir:
        return  # If no folder is selected, exit the function
    
    # Step 2: Create the backup using libimobiledevice
    messagebox.showinfo("Backup Process", "Starting iPhone backup...")
    
    backup_success = create_backup(backup_dir)
    if not backup_success:
        messagebox.showerror("Backup Failed", "An error occurred while creating the backup.")
        return
    
    # Step 3: Extract messages from the backup
    messagebox.showinfo("Extracting Messages", "Extracting messages from the backup...")
    
    messages = extract_messages(backup_dir)
    
    if messages:
        # Step 4: Save the extracted messages to a CSV file
        csv_file_path = os.path.join(backup_dir, "messages.csv")
        with open(csv_file_path, "w", newline="") as file:
            file.write("Message ID,Text,Timestamp\n")
            for msg in messages:
                file.write(f"{msg[0]},{msg[1]},{msg[2]}\n")
        
        messagebox.showinfo("Success", f"Messages extracted successfully and saved to {csv_file_path}")
    else:
        messagebox.showerror("No Messages", "No messages were found in the backup.")

# GUI Setup
app = tk.Tk()
app.title("iPhone Message Extractor")
app.geometry("400x200")

label = tk.Label(app, text="Welcome to iPhone Message Extractor!", font=("Arial", 14))
label.pack(pady=10)

backup_button = tk.Button(app, text="Start Backup and Extract", command=start_backup, font=("Arial", 12))
backup_button.pack(pady=20)

app.mainloop()
