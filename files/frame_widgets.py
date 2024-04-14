import customtkinter as ctk
import settings
from PIL import Image
import os
from datetime import datetime


class AlertMsg(ctk.CTkToplevel):
    def __init__(self, parent, x, y):
        super().__init__(master=parent, width=100, height=50, fg_color=settings.ALERT)

        self.x = x
        self.y = y

        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)

        ctk.CTkLabel(self, text='at first open your image folder').pack(padx=2, pady=2)

        self.geometry(f"+{x-222}+{y-45}")
        self.deiconify()

        self.after(1000, lambda: self.destroy())


class AboutInfo(ctk.CTkButton):
    def __init__(self, parent):
        super().__init__(master=parent,
                         command=self.on_click,
                         width=10,
                         height=10,
                         text='',
                         fg_color='transparent',
                         hover=False,
                         image=ctk.CTkImage(dark_image=Image.open(settings.dots_image)))

        self.attached_window = None  # Flag to track window existence

        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    def onEnter(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.dots_enter_image)))

    def onLeave(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.dots_image)))
        if self.attached_window:
            self.attached_window.destroy()

    def on_click(self):
        if not self.attached_window or not self.attached_window.winfo_exists():
            # Create a new window
            self.attached_window = ctk.CTkToplevel(master=self, width=20, height=10, fg_color='black')
            self.attached_window.overrideredirect(True)  # Remove title bar
            self.attached_window.wm_attributes("-topmost", True)  # Keep on top

            ctk.CTkLabel(self.attached_window, text='this is the about of the \n image. where \n\n all of the things '
                                                    'are stay.').pack(pady=2)

            # Calculate attached window position
            x = self.winfo_rootx() + self.winfo_width()
            y = self.winfo_rooty()

            # Set geometry and show the window
            self.attached_window.geometry(f"+{x+10}+{y-22}")
            self.attached_window.deiconify()  # Ensure it's visible
        else:
            self.attached_window.destroy()


class ClickAttachedWindowButton(ctk.CTkButton):
    def __init__(self, parent, func, window_content):
        super().__init__(master=parent,
                         command=func,
                         width=10,
                         height=10,
                         text='',
                         fg_color='transparent',
                         hover=False,
                         image=ctk.CTkImage(dark_image=Image.open(settings.wallpaper_image)))

        self.window_content = window_content
        self.attached_window = None  # Flag to track window existence

        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    def onEnter(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.wallpaper_enter_image)))

    def onLeave(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.wallpaper_image)))

        if self.attached_window:
            self.attached_window.after(2000, lambda: self.attached_window.destroy())

    def on_click(self):
        if not self.attached_window or not self.attached_window.winfo_exists():
            # Create a new window
            self.attached_window = ctk.CTkToplevel(master=self, width=20, height=10)
            self.attached_window.overrideredirect(True)  # Remove title bar
            self.attached_window.wm_attributes("-topmost", True)  # Keep on top

            # Create content within the window
            for idx, content_text in enumerate(self.window_content, start=1):
                ctk.CTkButton(self.attached_window, text=content_text, command=self.operation(idx)).pack(pady=2)

            # Calculate attached window position
            x = self.winfo_rootx() + self.winfo_width()
            y = self.winfo_rooty()

            # Set geometry and show the window
            self.attached_window.geometry(f"+{x}+{y}")
            self.attached_window.deiconify()  # Ensure it's visible
        else:
            self.attached_window.destroy()

    def operation(self, idx):
        def inner_operation():
            if idx == 1:
                print('Wallpaper')
                # print(self.image_path)
            elif idx == 2:
                print('Lockscreen')
                # print(self.image_path)

        return inner_operation


class ImageFolder(ctk.CTkButton):
    def __init__(self, parent, func):
        super().__init__(
            master=parent,
            command=func,
            width=10,
            height=10,
            text='',
            fg_color='transparent',
            hover=False,
            image=ctk.CTkImage(dark_image=Image.open(settings.folder_image)))

        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    def onEnter(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.folder_enter_image)))

    def onLeave(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.folder_image)))


class EditImage(ctk.CTkButton):
    def __init__(self, parent, func):
        super().__init__(
            master=parent,
            command=func,
            width=10,
            height=10,
            text='',
            fg_color='transparent',
            hover=False,
            image=ctk.CTkImage(dark_image=Image.open(settings.editing_image)))

        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    def onEnter(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.editing_enter_image)))

    def onLeave(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.editing_image)))


class ImageRotate(ctk.CTkButton):
    def __init__(self, parent, func):
        super().__init__(
            master=parent,
            command=func,
            width=10,
            height=10,
            text='',
            fg_color='transparent',
            corner_radius=0,
            hover=False,
            image=ctk.CTkImage(dark_image=Image.open(settings.rotate_image)))

        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    def onEnter(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.rotate_enter_image)))

    def onLeave(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.rotate_image)))


class ImageInfo(ctk.CTkButton):
    def __init__(self, parent, func):
        super().__init__(
            master=parent,
            command=func,
            width=10,
            height=10,
            text='',
            fg_color='transparent',
            corner_radius=0,
            hover=False,
            image=ctk.CTkImage(dark_image=Image.open(settings.info_image)))

        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    def onEnter(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.info_enter_image)))

    def onLeave(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.info_image)))


class LeftImageButton(ctk.CTkButton):
    def __init__(self, parent, func):
        super().__init__(
            master=parent,
            command=func,
            width=50,
            height=10,
            text='',
            image=ctk.CTkImage(dark_image=Image.open(settings.left_image)),
            fg_color='transparent',
            hover=False)

        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    def onEnter(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.left_enter_image)))

    def onLeave(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.left_image)))


class RightImageButton(ctk.CTkButton):
    def __init__(self, parent, func):
        super().__init__(
            master=parent,
            command=func,
            width=50,
            height=10,
            text='',
            image=ctk.CTkImage(dark_image=Image.open(settings.right_image)),
            fg_color='transparent',
            hover=False)

        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    def onEnter(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.right_enter_image)))

    def onLeave(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.right_image)))


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # General attributes
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)

        # Animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # Close button
        ctk.CTkButton(self, text='', width=10, height=10, command=self.animate,
                      fg_color='transparent', hover_color=settings.DARK_GRAY,
                      image=ctk.CTkImage(dark_image=Image.open('../pic/close.png'))).place(relx=0.89, rely=0.005)

        # Image info
        self.image_info_label = ctk.CTkLabel(self, text='Image Info')
        self.image_info_label.pack(side='top')

        frame = ctk.CTkFrame(self, fg_color='transparent')
        frame.pack(expand=True, fill='both', padx=5, pady=10)

        ctk.CTkLabel(frame, text='Image Name').pack(anchor='w')
        frame_box = ctk.CTkFrame(frame, fg_color=settings.DARK_GRAY)
        frame_box.pack(fill='both', padx=5)
        self.image_name = ctk.CTkLabel(frame_box, text='', wraplength=200)
        self.image_name.pack(fill='both', padx=5, pady=1)

        ctk.CTkLabel(frame, text='Date').pack(anchor='w')
        frame_box = ctk.CTkFrame(frame, fg_color=settings.DARK_GRAY)
        frame_box.pack(fill='both', padx=5)
        self.image_date = ctk.CTkLabel(frame_box, text='')
        self.image_date.pack(fill='both', padx=5, pady=1)

        self.image_size = ctk.CTkLabel(frame, text='')
        self.image_size.pack(anchor='w')

        self.image_format = ctk.CTkLabel(frame, text='')
        self.image_format.pack(anchor='w')

        self.image_mode = ctk.CTkLabel(frame, text='')
        self.image_mode.pack(anchor='w')

        self.image_pixel = ctk.CTkLabel(frame, text='')
        self.image_pixel.pack(anchor='w')

        ctk.CTkLabel(frame, text='Path').pack(anchor='w')
        frame_box = ctk.CTkFrame(frame, fg_color=settings.DARK_GRAY)
        frame_box.pack(fill='both', padx=5)
        self.image_path = ctk.CTkLabel(frame_box, text='', wraplength=200)
        self.image_path.pack(fill='both', padx=5, pady=1)

        # Layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def set_image_info(self, image_path):
        # Extract image name and size
        image_name = os.path.basename(image_path)
        image_size = os.path.getsize(image_path)

        modified_time = os.path.getmtime(image_path)
        modified_date = datetime.fromtimestamp(modified_time)

        # Open the image to get additional metadata
        try:
            with Image.open(image_path) as img:
                image_format = img.format
                image_mode = img.mode
                image_dimensions = img.size
        except Exception as e:
            print(f"Error opening image: {e}")
            image_format = "Unknown"
            image_mode = "Unknown"
            image_dimensions = (0, 0)

        # Set the image info text
        self.image_name.configure(text=image_name)
        self.image_date.configure(text=modified_date)
        self.image_size.configure(text=f'Size:    {image_size} bytes')
        self.image_format.configure(text=f'Format:   {image_format}')
        self.image_mode.configure(text=f'Mode:    {image_mode}')
        self.image_pixel.configure(text=f'Resolution:  {image_dimensions[0]} x {image_dimensions[1]} pixels')
        self.image_path.configure(text=image_path)

    def animate(self):
        if self.in_start_pos:
            # self.image_path.configure(text=settings.image_info['image_path'])
            self.set_image_info(settings.image_info['image_path'])
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos + 0.09:  # Check if position is greater than the end position + threshold
            self.pos -= 0.09
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.pos = self.end_pos  # Ensure position reaches end position accurately
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos - 0.9:  # Check if position is less than the start position - threshold
            self.pos += 0.9
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.pos = self.start_pos  # Ensure position reaches start position accurately
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.in_start_pos = True
