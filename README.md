# WebP2PNG
python script to convert Webp files to PNG

# WebP to PNG Converter

A simple, user-friendly desktop application that allows you to convert multiple WebP images to PNG format with just a few clicks.

## Features

- **Batch Processing**: Select and convert multiple WebP files at once
- **User-friendly Interface**: Simple GUI with progress tracking
- **Custom Output**: Choose your preferred destination folder
- **Progress Tracking**: Monitor conversion progress with a visual progress bar


## Requirements

- Python 3.6 or higher
- Pillow (PIL Fork) library

## Installation

1. Clone this repository or download the source code:
 
   git clone https://github.com/yourusername/webp-to-png-converter.git
   cd webp-to-png-converter


Usage

Run the application:
bashCopypython webp_to_png.py

Click the "Select WebP Files" button to choose the WebP images you want to convert.
(Optional) Choose an output directory by clicking the "Browse..." button. If not specified, the original file's directory will be used.
Click "Convert to PNG" to start the conversion process.
Wait for the progress bar to complete and the status to show "Conversion complete!".

How It Works
The application uses Python's Tkinter library for the GUI and the Pillow library for image processing. The conversion process runs in a separate thread to keep the user interface responsive.
Troubleshooting

Missing Pillow Library: If you get an error about missing modules, make sure you've installed all requirements with pip install -r requirements.txt.
File Permission Errors: Ensure you have write permissions in the output directory.
Invalid Files: Make sure all selected files are valid WebP images.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Pillow library for image processing capabilities
Tkinter for the GUI framework
