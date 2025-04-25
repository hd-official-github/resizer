import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os
import sys

selected_files = []  # To store the selected files

# Get the directory passed from the context menu (%V)
initial_directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

def choose_files():
    global selected_files
    filetypes = [("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    files = filedialog.askopenfilenames(
        title="Select Images", 
        filetypes=filetypes, 
        initialdir=initial_directory  # Open the directory passed from %V
    )
    if files:
        selected_files = files
        print("Selected files:")
        for file in files:
            print(file)
        file_count_label.config(text=f"{len(selected_files)} file(s) selected")  # Update file count label
        show_resize_options()

def update_status(message):
    """Update the status area with a new message."""
    status_area.insert(tk.END, message + "\n")
    status_area.see(tk.END)  # Auto-scroll to the latest message

def resize_images():
    global selected_files

    # Get widths and suffixes from input fields
    width_small = int(width_small_entry.get())
    suffix_small = suffix_small_entry.get()
    width_medium = int(width_medium_entry.get())
    suffix_medium = suffix_medium_entry.get()
    width_large = int(width_large_entry.get())
    suffix_large = suffix_large_entry.get()

    for file in selected_files:
        try:
            update_status(f"Processing file: {file}")
            # Open the image using PIL
            img = Image.open(file)

            # Resize for small width
            aspect_ratio = img.height / img.width
            new_height_small = int(width_small * aspect_ratio)
            img_small = img.resize((width_small, new_height_small), Image.Resampling.LANCZOS)
            output_path_small = os.path.join(
                os.path.dirname(file),
                os.path.splitext(os.path.basename(file))[0] + f"-{suffix_small}" + os.path.splitext(file)[1]
            )
            img_small.save(output_path_small)
            update_status(f"Small resized image saved to: {output_path_small}")

            # Resize for medium width
            new_height_medium = int(width_medium * aspect_ratio)
            img_medium = img.resize((width_medium, new_height_medium), Image.Resampling.LANCZOS)
            output_path_medium = os.path.join(
                os.path.dirname(file),
                os.path.splitext(os.path.basename(file))[0] + f"-{suffix_medium}" + os.path.splitext(file)[1]
            )
            img_medium.save(output_path_medium)
            update_status(f"Medium resized image saved to: {output_path_medium}")

            # Resize for large width
            new_height_large = int(width_large * aspect_ratio)
            img_large = img.resize((width_large, new_height_large), Image.Resampling.LANCZOS)
            output_path_large = os.path.join(
                os.path.dirname(file),
                os.path.splitext(os.path.basename(file))[0] + f"-{suffix_large}" + os.path.splitext(file)[1]
            )
            img_large.save(output_path_large)
            update_status(f"Large resized image saved to: {output_path_large}")

        except Exception as e:
            update_status(f"Error resizing {file}: {e}")

    update_status("Process Finished!")

def show_resize_options():
    # Show the input fields for widths, suffixes, and the resize button
    row1_frame.pack(pady=5)
    row2_frame.pack(pady=5)
    row3_frame.pack(pady=5)
    resize_button.pack(pady=20)
    status_area.pack(pady=10, fill=tk.BOTH, expand=True)

# Create the main window
root = tk.Tk()
root.title("Image Resizer")
root.geometry("400x500")  # Set the window size to fit all elements

# Create and place the "Choose Files" button
choose_button = tk.Button(
    root, 
    text="Choose Files", 
    command=choose_files, 
    font=("Arial", 14, "bold"), 
    bg="#4CAF50", 
    fg="white", 
    padx=20, 
    pady=10
)
choose_button.pack(pady=20)

# Add a label to display the number of selected files
file_count_label = tk.Label(root, text="No files selected", font=("Arial", 10))
file_count_label.pack(pady=5)

# Create frames for rows
row1_frame = tk.Frame(root)
row2_frame = tk.Frame(root)
row3_frame = tk.Frame(root)

# Row 1: Width Small and Suffix Small
width_small_label = tk.Label(row1_frame, text="Width Small:")
width_small_entry = tk.Entry(row1_frame, width=10)
suffix_small_label = tk.Label(row1_frame, text="Suffix Small:")
suffix_small_entry = tk.Entry(row1_frame, width=10)
width_small_label.pack(side=tk.LEFT, padx=5)
width_small_entry.pack(side=tk.LEFT, padx=5)
suffix_small_label.pack(side=tk.LEFT, padx=5)
suffix_small_entry.pack(side=tk.LEFT, padx=5)

# Row 2: Width Medium and Suffix Medium
width_medium_label = tk.Label(row2_frame, text="Width Medium:")
width_medium_entry = tk.Entry(row2_frame, width=10)
suffix_medium_label = tk.Label(row2_frame, text="Suffix Medium:")
suffix_medium_entry = tk.Entry(row2_frame, width=10)
width_medium_label.pack(side=tk.LEFT, padx=5)
width_medium_entry.pack(side=tk.LEFT, padx=5)
suffix_medium_label.pack(side=tk.LEFT, padx=5)
suffix_medium_entry.pack(side=tk.LEFT, padx=5)

# Row 3: Width Large and Suffix Large
width_large_label = tk.Label(row3_frame, text="Width Large:")
width_large_entry = tk.Entry(row3_frame, width=10)
suffix_large_label = tk.Label(row3_frame, text="Suffix Large:")
suffix_large_entry = tk.Entry(row3_frame, width=10)
width_large_label.pack(side=tk.LEFT, padx=5)
width_large_entry.pack(side=tk.LEFT, padx=5)
suffix_large_label.pack(side=tk.LEFT, padx=5)
suffix_large_entry.pack(side=tk.LEFT, padx=5)

# Create the "Resize Images" button
resize_button = tk.Button(
    root, 
    text="Resize Images", 
    command=resize_images, 
    font=("Arial", 14, "bold"), 
    bg="#FF5722", 
    fg="white", 
    padx=20, 
    pady=10
)
resize_button.pack_forget()  # Hide the button initially

# Create a status area to display progress
status_area = tk.Text(root, height=10, wrap=tk.WORD)
status_area.pack_forget()  # Hide the status area initially

# Run the application
root.mainloop()