import customtkinter as ctk
import settings


class LeftImageButton(ctk.CTkButton):
    def __init__(self, parent, func,  col, row, image, text='', color='dark-gray'):
        super().__init__(
            master=parent,
            command=func,
            width=10,
            height=10,
            text=text,
            image=image,
            corner_radius=settings.styling['corner_radius'],
            fg_color='transparent',
            hover_color=settings.COLORS[color]['fg'])
        self.grid(column=col, row=row, sticky='se', padx=settings.styling['gap'], pady=settings.styling['gap'])


class RightImageButton(ctk.CTkButton):
    def __init__(self, parent, func,  col, row, image, text='', color='dark-gray'):
        super().__init__(
            master=parent,
            command=func,
            width=10,
            height=10,
            text=text,
            image=image,
            corner_radius=settings.styling['corner_radius'],
            fg_color='transparent',
            hover_color=settings.COLORS[color]['fg'])
        self.grid(column=col, row=row, sticky='se', padx=settings.styling['gap'], pady=settings.styling['gap'])