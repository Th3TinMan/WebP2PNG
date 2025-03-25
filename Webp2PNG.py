import os
import sys
from PIL import Image
import tkinter as tk
from tkinter import filedialog, ttk
from threading import Thread


class WebpToPngConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("WebP to PNG Converter")
        self.root.geometry("600x400")
        self.root.minsize(500, 300)

        # Create GUI components
        self.setup_ui()

        # List to store selected file paths
        self.selected_files = []

    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Top section - Select files button
        select_frame = ttk.Frame(main_frame)
        select_frame.pack(fill=tk.X, pady=(0, 10))

        select_btn = ttk.Button(select_frame, text="Select WebP Files", command=self.select_files)
        select_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.file_count_label = ttk.Label(select_frame, text="No files selected")
        self.file_count_label.pack(side=tk.LEFT, fill=tk.X)

        # Middle section - File list
        list_frame = ttk.LabelFrame(main_frame, text="Selected Files")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # Scrollbar and Listbox for files
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_listbox = tk.Listbox(list_frame)
        self.file_listbox.pack(fill=tk.BOTH, expand=True)

        # Connect scrollbar to listbox
        self.file_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.file_listbox.yview)

        # Bottom section - Output directory and Convert button
        output_frame = ttk.Frame(main_frame)
        output_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(output_frame, text="Output Directory:").pack(side=tk.LEFT, padx=(0, 5))

        self.output_dir_var = tk.StringVar()
        output_entry = ttk.Entry(output_frame, textvariable=self.output_dir_var, width=40)
        output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        browse_btn = ttk.Button(output_frame, text="Browse...", command=self.select_output_dir)
        browse_btn.pack(side=tk.LEFT)

        # Progress indicators
        progress_frame = ttk.Frame(main_frame)
        progress_frame.pack(fill=tk.X, pady=(0, 10))

        self.progress_bar = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, mode='determinate')
        self.progress_bar.pack(fill=tk.X, padx=(0, 10), side=tk.LEFT, expand=True)

        self.status_label = ttk.Label(progress_frame, text="Ready")
        self.status_label.pack(side=tk.LEFT)

        # Convert button
        convert_btn = ttk.Button(main_frame, text="Convert to PNG", command=self.start_conversion)
        convert_btn.pack(pady=(0, 5))

    def select_files(self):
        """Open file dialog to select multiple WebP files"""
        files = filedialog.askopenfilenames(
            title="Select WebP Files",
            filetypes=[("WebP files", "*.webp"), ("All files", "*.*")]
        )

        if files:
            self.selected_files = list(files)
            self.file_count_label.config(text=f"{len(self.selected_files)} files selected")

            # Update listbox
            self.file_listbox.delete(0, tk.END)
            for file in self.selected_files:
                self.file_listbox.insert(tk.END, os.path.basename(file))

    def select_output_dir(self):
        """Open directory dialog to select output folder"""
        directory = filedialog.askdirectory(title="Select Output Directory")
        if directory:
            self.output_dir_var.set(directory)

    def start_conversion(self):
        """Start the conversion process in a separate thread"""
        if not self.selected_files:
            self.status_label.config(text="No files selected")
            return

        output_dir = self.output_dir_var.get()
        if not output_dir:
            # Default to same directory as input files
            output_dir = os.path.dirname(self.selected_files[0])
            self.output_dir_var.set(output_dir)

        # Make sure output directory exists
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        # Start conversion in a separate thread to keep UI responsive
        conversion_thread = Thread(target=self.convert_files, args=(output_dir,))
        conversion_thread.daemon = True
        conversion_thread.start()

    def convert_files(self, output_dir):
        """Convert WebP files to PNG"""
        total_files = len(self.selected_files)
        self.progress_bar['maximum'] = total_files
        self.progress_bar['value'] = 0

        for i, file_path in enumerate(self.selected_files):
            try:
                # Update status
                file_name = os.path.basename(file_path)
                self.status_label.config(text=f"Converting {i + 1}/{total_files}: {file_name}")
                self.root.update_idletasks()

                # Convert file
                img = Image.open(file_path)

                # Create output file path with PNG extension
                output_filename = os.path.splitext(file_name)[0] + ".png"
                output_path = os.path.join(output_dir, output_filename)

                # Save as PNG
                img.save(output_path, "PNG")

                # Update progress
                self.progress_bar['value'] = i + 1
                self.root.update_idletasks()

            except Exception as e:
                print(f"Error converting {file_path}: {str(e)}")

        self.status_label.config(text="Conversion complete!")


if __name__ == "__main__":
    root = tk.Tk()
    app = WebpToPngConverter(root)
    root.mainloop()