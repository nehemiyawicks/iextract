import sqlite3

def extract_messages(backup_path):
    """
    Extracts messages from the iPhone backup database.
    """
    messages = []
    db_path = os.path.join(backup_path, "Library", "SMS", "sms.db")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, text, date FROM message WHERE text IS NOT NULL;")
        messages = cursor.fetchall()
        conn.close()
        print(f"Extracted {len(messages)} messages.")
    except Exception as e:
        print(f"Error extracting messages: {e}")
    return messages
