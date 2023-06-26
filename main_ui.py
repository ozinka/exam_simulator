from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import tkinter

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
        # Stay Always On top
        self.wm_attributes("-topmost", 1)
        # Exit confirmation
        self.protocol("WM_DELETE_WINDOW", self.app_close)
        # Exit on Escape
        self.bind('<Escape>', lambda x: self.app_close())

        # Navigation frame
        self.fr_nav = ctk.CTkFrame(self, width=150, corner_radius=0)
        self.fr_nav.pack(fill=ctk.Y, side=ctk.LEFT)

        self.lb_title = ctk.CTkLabel(self.fr_nav, text="Exam Simulator (developed by Ozi)", text_color="#bbb")
        self.lb_title.pack(side=ctk.TOP, fill=ctk.X, padx=10)

        # Radiobutton frame
        self.radiobutton_frame = ctk.CTkFrame(self.fr_nav)
        self.radiobutton_frame.pack(fill=ctk.X, pady=5)
        self.rd_timer = tkinter.IntVar(value=1)
        self.label_radio_group = ctk.CTkLabel(master=self.radiobutton_frame, text="Timer:")
        self.label_radio_group.pack(anchor=ctk.W, padx=10, pady=5)
        self.radio_button_1 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.rd_timer,
                                                 value=0, text="30 sec per question")
        self.radio_button_1.pack(anchor=ctk.W, padx=10, pady=5)
        self.radio_button_2 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.rd_timer,
                                                 value=1, text="60 sec per question")
        self.radio_button_2.pack(anchor=ctk.W, padx=10, pady=5)
        self.radio_button_3 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.rd_timer,
                                                 value=2, text="90 sec per question")
        self.radio_button_3.pack(anchor=ctk.W, padx=10, pady=5)
        self.radio_button_4 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.rd_timer,
                                                 value=3, text="No timer")
        self.radio_button_4.pack(anchor=ctk.W, padx=10, pady=5)

        self.checkbox_slider_frame = ctk.CTkFrame(self.fr_nav)
        self.checkbox_slider_frame.pack(fill=ctk.X)
        self.chb_var_show_ans = ctk.IntVar()
        self.chb_var_ = ctk.IntVar()
        self.checkbox_1 = ctk.CTkCheckBox(master=self.checkbox_slider_frame, text="Show Answer immediately",
                                          variable=self.chb_var_show_ans)
        self.checkbox_1.pack(pady=5, anchor=ctk.W, padx=10)
        self.checkbox_2 = ctk.CTkCheckBox(master=self.checkbox_slider_frame, text="Show Stat immediately",
                                          variable=self.chb_var_)
        self.checkbox_2.pack(pady=5, anchor=ctk.W, padx=10)

        # Button Exit
        self.btn_exit = ctk.CTkButton(self.fr_nav, width=200, height=40, text="Exit", command=self.app_close,
                                      fg_color="#DA3633")
        self.btn_exit.pack(side=ctk.BOTTOM)

        # Button Appearance
        self.btn_appearance = ctk.CTkOptionMenu(self.fr_nav, values=["Light", "Dark", "System"],
                                                command=self.change_appearance_mode_event)
        self.btn_appearance.pack(side=ctk.BOTTOM, pady=40, anchor=ctk.W, padx=10, fill=ctk.X)

        # ======== Right frame ========
        self.fr_right = ctk.CTkFrame(self, fg_color="transparent")
        self.fr_right.pack(fill=ctk.BOTH, expand=True)
        # Working Frame
        self.fr_open = ctk.CTkFrame(self.fr_right, fg_color="transparent")
        self.fr_open.pack(fill=ctk.BOTH, expand=True)
        # Buttons Frame
        self.fr_buttons = ctk.CTkFrame(self.fr_open, height=300, width=300)
        self.fr_buttons.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        # Button Open file
        self.btn_open_file = ctk.CTkButton(self.fr_buttons, text="Open Exam", command=self.open_file)
        self.btn_open_file.pack(pady=20, padx=20, )
        # Button Create a dump
        self.btn_create_dump = ctk.CTkButton(self.fr_buttons,text="Create Dump")
        self.btn_create_dump.pack(pady=20, padx=20)

    def open_file(self):
        ftypes = [('JSON files', '*.jsn'), ('All files', '*')]
        dlg_open = ctk.filedialog.Open(self, filetypes=ftypes)
        fl = dlg_open.show()
        print(fl)

    def app_close(self):
        self.destroy()
        # msg = CTkMessagebox(master=self, title="Exit?", message="Do you want to close the program?",
        #                     icon="question", option_1="No", option_2="Yes")
        # response = msg.get()
        # if response == "Yes":
        #     self.destroy()

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)
