from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from main_fr import MainFrame
from dump_fr import DumpFrame
from exam_settings import ExamSettingsFrame
from exam import ExamFrame

# System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Exam Simulator")
        self.geometry("720x480+600+400")
        self.minsize(600, 400)
        # Stay Always On top
        self.wm_attributes("-topmost", 1)
        # Exit confirmation
        self.protocol("WM_DELETE_WINDOW", self.app_close)
        # Exit on Escape
        self.bind('<Escape>', lambda x: self.app_close())

        self.frames = {"MainFrame": MainFrame(self),
                       "DumpFrame": DumpFrame(self),
                       "ExamSettingsFrame": ExamSettingsFrame(self),
                       "ExamFrame": ExamFrame(self),
                       }
        self.select_frame()

    def select_frame(self, fr=None):
        for k in self.frames:
            self.frames[k].pack_forget()
        if fr:
            self.frames[fr].pack(fill=ctk.BOTH, expand=True)
        else:
            self.frames["ExamSettingsFrame"].pack(fill=ctk.BOTH, expand=True)

    def app_close(self):
        self.destroy()
        # msg = CTkMessagebox(master=self, title="Exit?", message="Do you want to close the program?",
        #                     icon="question", option_1="No", option_2="Yes")
        # response = msg.get()
        # if response == "Yes":
        #     self.destroy()
