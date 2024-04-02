import customtkinter as ctk
from tkinter import filedialog
import settings
from PIL import Image


class FirstFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')

        # layout
        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')


class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(master=parent)
        self.grid(column=0, columnspan=2, row=0, sticky='nsew')
        self.import_func = import_func

        ctk.CTkButton(self, text='open image', command=self.open_dialog, fg_color=settings.BUTTON_COLOR,
                      hover_color=settings.BUTTON_HOVER_COLOR).pack(expand=True)

    def open_dialog(self):
        path = filedialog.askopenfilename()
        self.import_func(path)


class ImageOutput(ctk.CTkCanvas):
    def __init__(self, parent, resize_image):
        super().__init__(master=parent, background=settings.BACKGROUND_COLOR,  relief='ridge',
                         bd=0, highlightthickness=0)
        self.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        self.bind('<Configure>', resize_image)


class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_func):
        super().__init__(master=parent, command=close_func, text='', text_color=settings.WHITE,
                         fg_color='transparent', width=40, height=40, corner_radius=0, hover=False,
                         image=ctk.CTkImage(dark_image=Image.open(settings.close_image)))

        self.place(relx=0.99, rely=0.02, anchor='ne')
        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    def onEnter(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.close_enter_image)))

    def onLeave(self, event):
        self.configure(image=ctk.CTkImage(Image.open(settings.close_image)))
