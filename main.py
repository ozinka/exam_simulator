from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
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

        self.frames = {"MainFrame": ctk.CTkFrame(self),
                       "DumpFrame": DumpFrame(self),
                       "ExamSettingsFrame": ExamSettingsFrame(self),
                       "ExamFrame": ExamFrame(self),
                       }

        # Button Appearance
        self.btn_appearance = ctk.CTkOptionMenu(self.frames['MainFrame'], values=["Light", "Dark", "System"],
                                                command=self.change_appearance_mode_event,
                                                width=150)
        self.btn_appearance.pack(side=ctk.TOP, pady=10, anchor=ctk.E, padx=10)

        # Buttons Frame
        self.fr_buttons = ctk.CTkFrame(self.frames['MainFrame'], height=300, width=300)
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
        self.btn_exit = ctk.CTkButton(self.frames['MainFrame'], width=200, height=40, text="Exit",
                                      command=self.app_close,
                                      fg_color="#DA3633")
        self.btn_exit.pack(side=ctk.BOTTOM, pady=30)

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
            self.btn_appearance.set(config.get('GENERAL', 'theme'))
        else:
            self.btn_appearance.set("System")

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

    def open_exam_settings(self):
        self.select_frame("ExamSettingsFrame")

    def open_dump(self):
        self.select_frame("DumpFrame")

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
