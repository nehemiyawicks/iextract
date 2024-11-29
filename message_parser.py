import os
import sqlite3

def extract_messages(backup_path):
    """
    Extract messages from the iPhone backup.
    """
    # The device ID folder is inside the backup path.
    # We need to look for the "Library/SMS" folder under the device ID folder.
    device_id_folder = os.path.join(backup_path, os.listdir(backup_path)[0])  # First subfolder is the device ID folder
    sms_folder = os.path.join(device_id_folder, "Library", "SMS")

    # Check if the SMS folder exists and search for sms.db in it
    if os.path.exists(sms_folder):
        db_path = os.path.join(sms_folder, "sms.db")
        if os.path.exists(db_path):
            # Connect to the SMS database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Query to fetch message details
            cursor.execute("SELECT rowid, text, date FROM message")
            messages = cursor.fetchall()
            conn.close()
            return messages
        else:
            print(f"Error: sms.db not found in {sms_folder}")
            return []
    else:
        print(f"Error: SMS folder not found at {sms_folder}")
        return []
