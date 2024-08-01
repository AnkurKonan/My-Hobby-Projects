import customtkinter
from PIL import Image, ImageOps

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("College Database Management System")
        self.geometry("1200x700")
        self.resizable(False, False)
        self.grid_rowconfigure(5)
        self.grid_columnconfigure(3)

        original_image = Image.open("right_arrow.png")
        mirrored_image = ImageOps.mirror(original_image)
        self.button_image_mirrored = customtkinter.CTkImage(mirrored_image, size=(20, 20))
        self.button_image = customtkinter.CTkImage(original_image, size=(20, 20))

        self.sidebar_frame = customtkinter.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsw", padx=(0, 10), pady=(0, 0))

        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="", fg_color="#0598ed", height=40, width=40,
                                               image=self.button_image_mirrored, compound="right")
        self.welcome.grid(row=0, column=0, padx=(15, 10), pady=(20, 10))

        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="", fg_color="#0598ed", height=40, width=40,
                                               image=self.button_image, compound="right")
        self.welcome.grid(row=0, column=1, padx=(5, 15), pady=(20, 10))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, width=95, anchor="sw",
                                                                       fg_color="#0598ed",
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.apperance)
        self.appearance_mode_optionemenu.grid(row=11, column=0, padx=10, pady=(10, 10), columnspan=2)

        self.welcome_label = customtkinter.CTkLabel(self, text="Chandigarh College of Engineering & Technology",
                                                    font=("Helvetica", 35))
        self.welcome_label.grid(row=0, column=1, padx=(40, 20), pady=(20, 10), columnspan=2)
        self.subtitle = customtkinter.CTkLabel(self, text="College Database Management System",
                                                     font=("Helvetica", 30))
        self.subtitle.grid(row=1, column=1, padx=(40, 10), pady=(0, 50), columnspan=3)

        self.subtitle = customtkinter.CTkLabel(self, text="Who's Database you want to Access",
                                               font=("Helvetica", 25))
        self.subtitle.grid(row=2, column=1, padx=(10, 10), pady=(0, 50), columnspan=2)

        self.button = customtkinter.CTkButton(self, text="Student",
                                                       font=("Helvetica", 18), width=150, height=100,
                                                       fg_color="#0598ed", command=lambda: self.show_frame("Stu"))
        self.button.grid(row=3, column=2, padx=(20, 20), pady=(20, 20))
        self.button = customtkinter.CTkButton(self, text="Staff",
                                              font=("Helvetica", 18), width=150, height=100,
                                              fg_color="#0598ed", command=lambda: self.show_frame("Staff"))
        self.button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20))

    def apperance(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
