from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from main_fr import MainFrame
from dump_fr import DumpFrame
from exam_settings import ExamSettingsFrame
from exam import ExamFrame
import configparser

ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Exam Simulator")
        self.minsize(600, 500)
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
        self.select_frame("DumpFrame")
        self.restore_settings()

    def restore_settings(self):
        config = configparser.ConfigParser()
        config.read('main.ini')
        if config.has_option('GENERAL', 'position'):
            self.geometry(config.get('GENERAL', 'position'))
        else:
            self.geometry("500x500+500+200")

        if config.has_option('GENERAL', 'theme'):
            ctk.set_appearance_mode(config.get('GENERAL', 'theme'))
        else:
            ctk.set_appearance_mode("System")

    def save_settings(self):
        config = configparser.ConfigParser()
        config['GENERAL'] = {
            'position': f'{self.geometry()}',
            'theme': ctk.get_appearance_mode()
        }
        with open('main.ini', 'w') as configfile:  # save
            config.write(configfile)

    def select_frame(self, fr=None):
        for k in self.frames:
            self.frames[k].pack_forget()
        if fr:
            self.frames[fr].pack(fill=ctk.BOTH, expand=True)
        else:
            self.frames["MainFrame"].pack(fill=ctk.BOTH, expand=True)

    def app_close(self):
        self.save_settings()
        self.destroy()
        # msg = CTkMessagebox(master=self, title="Exit?", message="Do you want to close the program?",
        #                     icon="question", option_1="No", option_2="Yes")
        # response = msg.get()
        # if response == "Yes":
        #     self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
