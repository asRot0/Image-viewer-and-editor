import customtkinter as ctk
import settings
from PIL import Image


class ImageFolder(ctk.CTkButton):
    def __init__(self, parent, func):
        super().__init__(
            master=parent,
            command=func,
            width=10,
            height=10,
            text='',
            fg_color='transparent',
            hover_color=None,
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
            hover_color=None,
            hover=False,
            image=ctk.CTkImage(dark_image=Image.open(settings.editing_image)))

        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    def onEnter(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.editing_enter_image)))

    def onLeave(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.editing_image)))


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
            image=ctk.CTkImage(dark_image=Image.open('../pic/folder.png')))


class LeftImageButton(ctk.CTkButton):
    def __init__(self, parent, func):
        super().__init__(
            master=parent,
            command=func,
            width=50,
            height=10,
            text='',
            image=ctk.CTkImage(dark_image=Image.open(settings.left_image_button)),
            fg_color='transparent',
            hover_color=settings.DARK_GRAY)


class RightImageButton(ctk.CTkButton):
    def __init__(self, parent, func):
        super().__init__(
            master=parent,
            command=func,
            width=50,
            height=10,
            text='',
            image=ctk.CTkImage(dark_image=Image.open(settings.right_image_button)),
            fg_color='transparent',
            hover_color=settings.DARK_GRAY)


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent, fg_color='red')

        # General attributes
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)

        # Animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # Layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos + 0.008:  # Check if position is greater than the end position + threshold
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.pos = self.end_pos  # Ensure position reaches end position accurately
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos - 0.008:  # Check if position is less than the start position - threshold
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.pos = self.start_pos  # Ensure position reaches start position accurately
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.in_start_pos = True
