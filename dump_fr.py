import customtkinter as ctk


class DumpFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Frame main
        self.fr_main = ctk.CTkFrame(self)
        self.fr_main.pack(fill=ctk.BOTH, expand=True)

        # Frame for Row Data
        self.fr_row_data = ctk.CTkFrame(self.fr_main)
        self.fr_row_data.pack(pady=5, padx=5, side=ctk.LEFT, anchor=ctk.N, fill=ctk.Y)

        self.lb_question = ctk.CTkLabel(self.fr_row_data, text="Question")
        self.lb_question.pack(anchor=ctk.W, padx=5)

        # Question TextBox
        self.tb_question = ctk.CTkTextbox(self.fr_row_data, width=400)
        self.tb_question.pack(anchor=ctk.W, padx=5)

        self.lb_answers = ctk.CTkLabel(self.fr_row_data, text="Answers")
        self.lb_answers.pack(anchor=ctk.W, pady=(5, 0), padx=5)

        # Answer TextBox
        self.var_answer = ctk.StringVar()
        self.var_answer.trace("w", lambda name, index, mode, var=self.var_answer: self.OnAnswerChange(self.var_answer))
        self.tb_answers = ctk.CTkTextbox(self.fr_row_data, width=400, height=100, text=self.var_answer)
        self.tb_answers.pack(anchor=ctk.W, padx=5, pady=(0, 5), expand=True, fill=ctk.Y)

        # Frame for question example
        self.fr_row_data = ctk.CTkFrame(self.fr_main)
        self.fr_row_data.pack(pady=5, padx=(0, 5), side=ctk.LEFT, fill=ctk.BOTH, expand=True)

        # Button Cancel
        self.btn_cancel = ctk.CTkButton(self, width=200, height=40, text="Cancel", command=self.cancel,
                                        fg_color="#DA3633")
        self.btn_cancel.pack(side=ctk.BOTTOM, pady=30, padx=10)

    def cancel(self):
        self.master.select_frame("MainFrame")

    def OnAnswerChange(self):
        print(self.var_answer.get())



if __name__ == "__main__":
    pass
