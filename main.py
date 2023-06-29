from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from main_fr import MainFrame
from dump_fr import DumpFrame
from exam_settings import ExamSettingsFrame
from exam import ExamFrame
import configparser

# System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Exam Simulator")
        self.restore_settings()
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

    def restore_settings(self):
        with open('main.ini', 'w') as configfile:  # create file if not exist
            pass
        config = configparser.ConfigParser()
        config.read('main.ini')
        print(self.wm_geometry())
        if config.has_option('GENERAL', 'position'):
            self.geometry(str(config.get('GENERAL', 'position')))
            print(self.wm_geometry())
            self.update()
            print(self.wm_geometry())
        else:
            self.geometry("500x500+1500+800")
            self.update()
            print(self.wm_geometry())

    def save_settings(self):
        config = configparser.ConfigParser()
        config['GENERAL'] = {
            'position': f'{self.wm_geometry()}'
            # 'position': f'{self.winfo_width()}x{self.winfo_height()}+{self.winfo_x()}+{self.winfo_y()}'
        }
        print(self.wm_geometry())
        with open('main.ini', 'w') as configfile:  # save
            config.write(configfile)

    def select_frame(self, fr=None):
        for k in self.frames:
            self.frames[k].pack_forget()
        if fr:
            self.frames[fr].pack(fill=ctk.BOTH, expand=True)
        else:
            self.frames["ExamSettingsFrame"].pack(fill=ctk.BOTH, expand=True)

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
