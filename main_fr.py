import customtkinter as ctk


class MainFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Button Appearance
        self.btn_appearance = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                command=self.change_appearance_mode_event,
                                                width=150)
        self.btn_appearance.pack(side=ctk.TOP, pady=10, anchor=ctk.E, padx=10)

        # Buttons Frame
        self.fr_buttons = ctk.CTkFrame(self, height=300, width=300)
        self.fr_buttons.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)
        # Button Open file
        self.btn_open_file = ctk.CTkButton(self.fr_buttons, text="Open Exam", width=200, height=40,
                                           command=self.open_exam_settings)
        self.btn_open_file.pack(pady=20, padx=20)
        # Button Create a dump
        self.btn_create_dump = ctk.CTkButton(self.fr_buttons, text="Create Dump", width=200, height=40,
                                             command=self.open_dump)
        self.btn_create_dump.pack(pady=(0, 20), padx=20)

        # Button Exit
        self.btn_exit = ctk.CTkButton(self, width=200, height=40, text="Exit", command=self.master.app_close,
                                      fg_color="#DA3633")
        self.btn_exit.pack(side=ctk.BOTTOM, pady=30)

    def open_exam_settings(self):
        self.master.select_frame("ExamSettingsFrame")


    def open_dump(self):
        self.master.select_frame("DumpFrame")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    pass
