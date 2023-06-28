import customtkinter as ctk

# System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class DumpFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



if __name__ == "__main__":
    app = ctk.CTk()
    dump_fr = DumpFrame(app, bg_color="blue")
    # dump_fr = ctk.CTkFrame(app)
    dump_fr.pack(fill=ctk.BOTH)
    app.mainloop()
