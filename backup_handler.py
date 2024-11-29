import subprocess
import os
import time  # For simulating progress

def create_backup(output_dir, progress_bar):
    """
    Creates a backup of the connected iPhone and updates the progress bar.
    """
    try:
        # Ensure the output directory exists, create it if not
        os.makedirs(output_dir, exist_ok=True)
        
        # Start the backup process using idevicebackup2
        # subprocess.Popen is used to run the backup process and capture its output
        process = subprocess.Popen(
            ["idevicebackup2", "backup", output_dir],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        
        # Simulating backup progress (this part should be removed in real use)
        total_steps = 100
        for step in range(total_steps):
            # Update the progress bar for each step
            progress_bar['value'] = step
            progress_bar.update_idletasks()  # Ensure the GUI updates the progress bar
            time.sleep(0.1)  # Simulating the time it takes for the backup process (remove in real use)

        # Example code for handling real-time progress updates from idevicebackup2
        # Uncomment and adjust this section when actual progress can be read from the process
        # for line in process.stdout:
        #     # Check the output from the backup process and parse it to update the progress bar
        #     if "Progress" in line:  # Example condition, adjust based on actual output format
        #         progress_percentage = parse_progress(line)
        #         progress_bar['value'] = progress_percentage
        #         progress_bar.update_idletasks()

        # Wait for the backup process to complete (stderr and stdout are captured but not used here)
        process.communicate()

        # Print success message and return True if the backup was created successfully
        print(f"Backup created at {output_dir}")
        return True
    except Exception as e:
        # Print error message if something goes wrong during the backup process
        print(f"Error creating backup: {e}")
        return False
