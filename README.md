# iExtract

**iExtract** is a tool for extracting and backing up messages from iTunes into a CSV file. It supports easy extraction and offers a clean user interface with a sleek design. The app has been designed to handle backups of multiple messages efficiently, and it can generate CSV files for easy viewing.

## Features
- **Simple Interface:** The app has an intuitive, minimalistic interface with a dark theme.
- **Message Extraction:** Easily extract iTunes backup messages and save them into a CSV file.
- **Efficient Processing:** Handles a large number of messages without crashing or slowing down.
- **Custom Icon:** The app uses a custom icon for a personalized touch.

## Installation

### Prerequisites
- **Python:** Ensure Python 3.x is installed on your machine.
- **iTunes Drivers:** For iTunes-specific data extraction (not required if only CSV export is needed).

### Steps to Install
1. **Download the Installer:** 
   [Download iExtract Installer]

2. **Run the Installer:**
   - Double-click the installer `.exe` file.
   - Follow the on-screen instructions to install the app.
   - The installer will automatically install all necessary dependencies, including Python packages and iTunes drivers (if selected).

3. **Launch the App:**
   - After installation, launch the app from the desktop or start menu.

4. **Usage:**
   - Open the app and select the iTunes backup file from your system.
   - Click the “Extract Messages” button to start processing the backup.
   - The app will generate a CSV file containing all the extracted messages.
   
## File Structure

The project follows this structure:

```
iExtract/
├── assets/
│   ├── icons/
│   │   └── backup_icon.ico 
│   ├── images/
│   │   └── background.png
├── main.py
├── backup_handler.py
├── message_parser.py
├── requirements.txt
└── README.md
```

### **Important Files:**
- `main.py`: The main script responsible for handling the extraction process.
- `backup_handler.py`: Contains logic for reading and processing the iTunes backup.
- `message_parser.py`: Responsible for parsing messages from the backup file and saving them into a CSV.
- `requirements.txt`: Lists all the dependencies required to run the app.
- `README.md`: This file.

## Troubleshooting

If the app doesn't work as expected, here are some steps to help:

1. **Check Dependencies:**
   Ensure all Python dependencies are installed correctly by running:
   ```
   pip install -r requirements.txt
   ```

2. **Reinstall iTunes Drivers:** 
   If you experience issues with iTunes backup extraction, reinstall the necessary iTunes drivers.

3. **Large Backups:**
   For large backups, the app might take longer to process. Be patient, and try reducing the size of the backup by deleting unnecessary files.

## Copyright

© 2024 Nehemiya Wickramasinghe. All rights reserved.