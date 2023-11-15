import customtkinter as ctk
from tkinter import filedialog
import settings
import os


class Frame(ctk.CTkFrame):
    def __init__(self, parent, flag_fun, path):
        super().__init__(master=parent, fg_color='red')
        self.pack(expand=True, fill='both')
        self.flag_fun = flag_fun
        self.path = path

        # image navigation
        header_frame = ctk.CTkFrame(self, fg_color='lightgrey')
        header_frame.grid(row=0, column=0, columnspan=3, sticky='ew')

        inner_frame = ctk.CTkFrame(header_frame, fg_color='lightgrey')
        inner_frame.pack(expand=True)

        left_button = ctk.CTkButton(inner_frame, text='Edit')
        left_button.pack(pady=5, side='left')
        img_num_text = ctk.CTkLabel(inner_frame, text='Button 2', fg_color='black')
        img_num_text.pack(pady=5, side='left')
        right_button = ctk.CTkButton(inner_frame, text='Button 3')
        right_button.pack(pady=5, side='left')

        # Vertical Frame on the Left
        left_vertical_frame = ctk.CTkFrame(self, fg_color='lightgrey', width=50)
        left_vertical_frame.grid(row=1, column=0, sticky='ns', pady=10)

        inner_frame = ctk.CTkFrame(left_vertical_frame, fg_color='lightgrey')
        inner_frame.pack(expand=True)

        button1 = ctk.CTkButton(inner_frame, text='open', width=10, command=self.open_image)
        button1.pack(padx=2, pady=10)
        button2 = ctk.CTkButton(inner_frame, text='Edit', width=10, command=self.edit_flag)
        button2.pack(padx=2, pady=10)
        button3 = ctk.CTkButton(inner_frame, text='Button 3', width=10)
        button3.pack(padx=2, pady=10)

        # Canvas for Image Viewer
        canvas = ctk.CTkCanvas(self, bg='white')
        canvas.grid(row=1, column=1, columnspan=2, sticky='nsew', padx=1, pady=2)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def open_image(self):
        # Open a file dialog to select a directory
        directory = filedialog.askdirectory()

        if directory:
            # Get a list of image files in the selected directory
            image_files = [file for file in os.listdir(directory) if
                           file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.jfif', '.bmp', '.tiff', '.ico'))]

            if image_files:
                # Sort the image files alphabetically
                image_files.sort()

                # Load and store the images
                self.images = []

                for file in image_files:
                    # Construct the full file path
                    file_path = os.path.join(directory, file)
                    self.images.append(file_path)
        self.path(self.images)

    def edit_flag(self):
        self.flag_fun(True)
