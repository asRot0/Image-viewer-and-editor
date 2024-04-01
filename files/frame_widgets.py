import customtkinter as ctk
import settings


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
