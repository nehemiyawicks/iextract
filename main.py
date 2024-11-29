import tkinter as tk
from tkinter import filedialog, messagebox
from backup_handler import create_backup
from message_parser import extract_messages

def start_backup():
    backup_dir = filedialog.askdirectory(title="Select Backup Folder")
    if not backup_dir:
        return
    if create_backup(backup_dir):
        messages = extract_messages(backup_dir)
        if messages:
            with open("messages.csv", "w", newline="") as file:
                file.write("Message ID,Text,Timestamp\n")
                for msg in messages:
                    file.write(f"{msg[0]},{msg[1]},{msg[2]}\n")
            messagebox.showinfo("Success", "Messages extracted and saved as messages.csv")

# GUI
app = tk.Tk()
app.title("iPhone Message Extractor")
app.geometry("400x200")

label = tk.Label(app, text="Welcome to iPhone Message Extractor!", font=("Arial", 14))
label.pack(pady=10)

backup_button = tk.Button(app, text="Start Backup and Extract", command=start_backup, font=("Arial", 12))
backup_button.pack(pady=20)

app.mainloop()
