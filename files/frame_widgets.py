import customtkinter as ctk
import settings
from PIL import Image
import os
from datetime import datetime
from CTkToolTip import CTkToolTip


class TooltipHandler:
    def __init__(self, widget, message, hide_after_ms=2000):
        self.widget = widget
        self.message = message
        self.hide_after_ms = hide_after_ms
        self.tooltip = CTkToolTip(widget, message=message, follow=False, bg_color=settings.MENU_BG, alpha=0.7)
        self.tooltip_permanently_hidden = False

        # Bind the hover events to the widget
        self.widget.bind("<Enter>", self.on_enter)
        self.widget.bind("<Leave>", self.on_leave)

    def hide_tooltip(self):
        if not self.tooltip_permanently_hidden:
            self.tooltip.hide()

    def on_enter(self, event):
        if not self.tooltip_permanently_hidden:
            self.tooltip.show()
            self.widget.after(self.hide_after_ms, self.hide_tooltip)  # hide the tooltip after specified ms

    def on_leave(self, event):
        self.tooltip.hide()

    def hide_permanently(self):
        self.tooltip.hide()
        self.tooltip_permanently_hidden = True  # Set flag to hide tooltip permanently


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
            self.attached_window = ctk.CTkToplevel(master=self, width=20, height=10, fg_color=settings.DARK_GRAY)
            self.attached_window.overrideredirect(True)  # Remove title bar
            self.attached_window.wm_attributes("-topmost", True)  # Keep on top
            self.attached_window.wm_attributes('-alpha', 0.6)

            frame = ctk.CTkFrame(self.attached_window, fg_color='transparent')
            frame.pack(side='top')
            ctk.CTkLabel(frame, image=ctk.CTkImage(Image.open(settings.title_ico)), text='').pack(side='left')
            ctk.CTkLabel(frame, text=settings.about['title']).pack(side='left', padx=5)

            ctk.CTkLabel(self.attached_window, text=f"{'Developer:'} {settings.about['developer']}", height=20).pack(anchor='w', padx=2)
            ctk.CTkLabel(self.attached_window, text=f"{'Version:'} {settings.about['version']}", height=20).pack(anchor='w', padx=2)
            ctk.CTkLabel(self.attached_window, text=f"{'Released:'} {settings.about['released']}", height=20).pack(anchor='w', padx=2)
            ctk.CTkLabel(self.attached_window, text=f"{'License:'} {settings.about['license']}", height=20).pack(anchor='w', padx=2)
            ctk.CTkLabel(self.attached_window, text=f"{'Copyright:'} {settings.about['copyright']}", height=20).pack(anchor='w', padx=2)

            # Calculate attached window position
            x = self.winfo_rootx() + self.winfo_width()
            y = self.winfo_rooty()

            # Set geometry and show the window
            self.attached_window.geometry(f"+{x+10}+{y-100}")
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
            self.attached_window = ctk.CTkToplevel(master=self, width=20, height=10, fg_color=settings.BUTTON_COLOR)
            self.attached_window.overrideredirect(True)  # Remove title bar
            self.attached_window.wm_attributes("-topmost", True)  # Keep on top
            self.attached_window.wm_attributes('-alpha', 0.6)

            # Create content within the window
            for idx, content_text in enumerate(self.window_content):
                ctk.CTkButton(self.attached_window, text=content_text, command=self.operation(idx),
                              fg_color='transparent', hover_color=settings.BLUE_BG).pack(pady=2)

            # Calculate attached window position
            x = self.winfo_rootx() + self.winfo_width()
            y = self.winfo_rooty()

            # Set geometry and show the window
            self.attached_window.geometry(f"+{x+8}+{y}")
            self.attached_window.deiconify()  # Ensure it's visible
        else:
            self.attached_window.destroy()

    def operation(self, idx):
        def inner_operation():
            if idx:
                print('Lockscreen')
            else:
                print('Wallpaper')
                print(settings.image_info['image_path'])

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
