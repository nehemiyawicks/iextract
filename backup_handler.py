import subprocess
import os

def create_backup(output_dir):
    """
    Creates a backup of the connected iPhone.
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        # Run the libimobiledevice backup command
        subprocess.run(["idevicebackup2", "backup", output_dir], check=True)
        print(f"Backup created at {output_dir}")
        return True
    except Exception as e:
        print(f"Error creating backup: {e}")
        return False
