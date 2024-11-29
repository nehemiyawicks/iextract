import subprocess
import os
import time  # For simulating progress

def create_backup(output_dir, progress_bar):
    """
    Creates a backup of the connected iPhone and updates the progress bar.
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        # Start the backup process using idevicebackup2
        # Using subprocess.Popen to capture output and simulate progress
        process = subprocess.Popen(
            ["idevicebackup2", "backup", output_dir],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        
        # Simulating backup progress for now (remove this part in real use)
        total_steps = 100
        for step in range(total_steps):
            # Update progress bar
            progress_bar['value'] = step
            progress_bar.update_idletasks()
            time.sleep(0.1)  # Simulating work done by the backup process (remove in real code)

        # If you can read progress from idevicebackup2, do it like this:
        # for line in process.stdout:
        #     # Check the output from the process and parse it to update the progress bar
        #     if "Progress" in line:  # Hypothetical example, adjust based on actual output
        #         progress_percentage = parse_progress(line)
        #         progress_bar['value'] = progress_percentage
        #         progress_bar.update_idletasks()

        # Wait for the process to complete
        process.communicate()

        print(f"Backup created at {output_dir}")
        return True
    except Exception as e:
        print(f"Error creating backup: {e}")
        return False
