from CTkMessagebox import CTkMessagebox
import customtkinter as ctk

# System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Exam Simulator")
        self.geometry("720x480+600+400")
        self.minsize(400, 300)
        # Left frame
        self.fr_left = ctk.CTkFrame(self, width=150, corner_radius=0)
        self.fr_left.pack(fill=ctk.Y, side=ctk.LEFT)

        self.lb_title = ctk.CTkLabel(self.fr_left, text="Exam Simulator (developed by Ozi)", text_color="#bbb")
        self.lb_title.pack(side=ctk.TOP, fill=ctk.X)
        # # Button Open file
        self.btn_open_file = ctk.CTkButton(self.fr_left, text="Open Exam", command=self.open_file)
        self.btn_open_file.pack()

        # # Middle frame
        self.fr_middle = ctk.CTkFrame(self, height=400, fg_color="#777")
        self.fr_middle.pack(fill=ctk.BOTH, expand=1)

        # Working Frame
        self.fr_work = ctk.CTkFrame(self.fr_middle, fg_color="#bbb", height=50)
        self.fr_work.pack(fill=ctk.BOTH, expand=True)

        # Button Exit
        self.btn_exit = ctk.CTkButton(self.fr_left, width=200, height=50, text="Exit",
                                      command=self.app_close, fg_color="#DA3633")
        self.btn_exit.pack(side=ctk.BOTTOM)

    def open_file(self):
        ftypes = [('JSON files', '*.jsn'), ('All files', '*')]
        dlg_open = ctk.filedialog.Open(self, filetypes=ftypes)
        fl = dlg_open.show()
        print(fl)

    def app_close(self):
        msg = CTkMessagebox(master=self, title="Exit?", message="Do you want to close the program?",
                            icon="question", option_1="No", option_2="Yes")
        response = msg.get()
        if response == "Yes":
            self.quit()