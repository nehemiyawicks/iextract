import os
import sqlite3

def extract_messages(backup_path):
    """
    Extract messages from an iPhone backup stored at the given path.
    """
    # Identify the device ID folder, which is the first subfolder in the backup path.
    device_id_folder = os.path.join(backup_path, os.listdir(backup_path)[0])  # First subfolder corresponds to device ID
    sms_folder = os.path.join(device_id_folder, "Library", "SMS")  # Path to the SMS folder within the device backup

    # Check if the SMS folder exists
    if os.path.exists(sms_folder):
        db_path = os.path.join(sms_folder, "sms.db")  # Path to the database containing messages
        
        # Check if the sms.db file exists
        if os.path.exists(db_path):
            # Connect to the sms.db SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Fetch message details (rowid, text, date)
            cursor.execute("SELECT rowid, text, date FROM message")
            messages = cursor.fetchall()
            conn.close()  # Close the database connection
            return messages  # Return the list of messages
        else:
            # Error: sms.db is not found in the SMS folder
            print(f"Error: sms.db not found in {sms_folder}")
            return []
    else:
        # Error: SMS folder not found
        print(f"Error: SMS folder not found at {sms_folder}")
        return []
