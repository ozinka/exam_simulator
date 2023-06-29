import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class ExamSettingsFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.lb_title = ctk.CTkLabel(self, text="Exam Simulator (developed by Ozi)", text_color="#bbb")
        self.lb_title.pack(side=ctk.TOP, fill=ctk.X, padx=10)

        # Radiobutton frame
        self.radiobutton_frame = ctk.CTkFrame(self, width=500)
        self.radiobutton_frame.pack(pady=5, side=ctk.LEFT, anchor=ctk.N)

        self.rd_timer = ctk.IntVar(value=1)
        self.label_radio_group = ctk.CTkLabel(master=self.radiobutton_frame, text="Timer")
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

        # Checkbox Frame
        self.checkbox_frame = ctk.CTkFrame(self, width=500)
        self.checkbox_frame.pack()
        self.chb_show_ans_var = ctk.IntVar()
        self.chb_show_stat_var = ctk.IntVar()
        self.chb_two_students_var = ctk.IntVar()
        self.checkbox_1 = ctk.CTkCheckBox(master=self.checkbox_frame, text="Show Answer immediately",
                                          variable=self.chb_show_ans_var)
        self.checkbox_1.pack(pady=5, anchor=ctk.W, padx=10)
        self.checkbox_2 = ctk.CTkCheckBox(master=self.checkbox_frame, text="Show Stats immediately",
                                          variable=self.chb_show_stat_var)
        self.checkbox_2.pack(pady=5, anchor=ctk.W, padx=10)
        self.checkbox_3 = ctk.CTkCheckBox(master=self.checkbox_frame, text="Two Students",
                                          variable=self.chb_two_students_var)
        self.checkbox_3.pack(pady=5, anchor=ctk.W, padx=10)

        # Button Open file
        self.btn_open_file = ctk.CTkButton(self, text="Open Exam", width=200, height=40,
                                           command=self.open_file)
        self.btn_open_file.pack(pady=20, padx=20)

        # Button Start Exam
        self.btn_start_exam = ctk.CTkButton(self, text="Start Exam", width=200, height=40, fg_color="#00cc6a",
                                            command=self.start_exam, state="disabled")
        self.btn_start_exam.pack(pady=(0, 20), padx=20)

        # Button Cancel
        self.btn_cancel = ctk.CTkButton(self, width=200, height=40, text="Cancel", command=self.cancel,
                                        fg_color="#DA3633")
        self.btn_cancel.pack(side=ctk.BOTTOM, pady=30, padx=10, anchor=ctk.E)

    def cancel(self):
        self.master.select_frame("MainFrame")

    def start_exam(self):
        self.master.select_frame("ExamFrame")

    def open_file(self):
        ftypes = [('JSON files', '*.jsn'), ('All files', '*')]
        dlg_open = ctk.filedialog.Open(self, filetypes=ftypes)
        fl = dlg_open.show()
        print(fl)

if __name__ == "__main__":
    pass
