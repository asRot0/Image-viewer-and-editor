import customtkinter as ctk
import settings


class ImageInfo(ctk.CTkButton):
    def __init__(self, parent, text, image_info):
        super().__init__(
            master=parent,
            command=image_info,
            width=10,
            height=10,
            text=text,
            fg_color='transparent',
            hover_color=None)


class LeftImageButton(ctk.CTkButton):
    def __init__(self, parent, func, image, text=''):
        super().__init__(
            master=parent,
            command=func,
            width=50,
            height=10,
            text=text,
            image=image,
            fg_color='transparent',
            hover_color=settings.DARK_GRAY)


class RightImageButton(ctk.CTkButton):
    def __init__(self, parent, func, image, text=''):
        super().__init__(
            master=parent,
            command=func,
            width=50,
            height=10,
            text=text,
            image=image,
            fg_color='transparent',
            hover_color=settings.DARK_GRAY)
