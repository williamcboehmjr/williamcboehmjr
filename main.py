# live_ocr.py
import cv2
import pytesseract
import pandas as pd
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

# Set up Tesseract path
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # Update this path based on your system

# Initialize DataFrame for storing data
df = pd.DataFrame(columns=['Serial Number', 'Issue Month', 'Issue Year'])

# Function to capture data from webcam
def capture_data():
    # Your code to capture a frame from the webcam goes here
    # For example, using OpenCV:
    # _, frame = webcam.read()

    # Perform OCR on the defined bounding box
    # For demonstration, let's assume you've defined a bounding box (x, y, w, h)
    # Adjust these coordinates based on your setup
    bounding_box = (100, 100, 300, 200)
    roi = frame[bounding_box[1]:bounding_box[1]+bounding_box[3], bounding_box[0]:bounding_box[0]+bounding_box[2]]
    text = pytesseract.image_to_string(roi, config='--psm 8')

    # Process the OCR output and update the DataFrame
    # Your code to parse the text and extract serial number, issue month, and year goes here
    # Update df.loc[index] with the extracted values

    # Refresh the GUI with updated data
    update_gui()

# Function to update GUI with DataFrame content
def update_gui():
    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, df.to_string(index=False))

# Function to select a webcam
def select_webcam():
    # Your code to select a webcam goes here
    # For example, using OpenCV:
    # webcam = cv2.VideoCapture(0)
    # Adjust the index based on your setup
    # Make sure to release the webcam when done

# GUI setup
root = tk.Tk()
root.title("Live OCR for Savings Bonds")

# Button to start capturing data
capture_button = tk.Button(root, text="Capture Data", command=capture_data)
capture_button.pack()

# Text widget to display DataFrame content
text_widget = tk.Text(root, height=10, width=40)
text_widget.pack()

# Button to select a webcam
select_webcam_button = tk.Button(root, text="Select Webcam", command=select_webcam)
select_webcam_button.pack()

# Start GUI
root.mainloop()