import customtkinter as ctk


class DumpFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Frame main
        self.fr_main = ctk.CTkFrame(self)
        self.fr_main.pack(fill=ctk.BOTH, expand=True)

        # Frame tool box
        self.fr_tool_box = ctk.CTkFrame(self.fr_main, height=50)
        self.fr_tool_box.pack(side=ctk.TOP, fill=ctk.X, padx=5, pady=(5,0))

        # Frame for raw Data
        self.fr_raw_data = ctk.CTkFrame(self.fr_main)
        self.fr_raw_data.pack(pady=5, padx=5, side=ctk.LEFT, anchor=ctk.N, fill=ctk.Y)

        # Question TextBox
        self.lb_raw_question = ctk.CTkLabel(self.fr_raw_data, text="Question")
        self.lb_raw_question.pack(anchor=ctk.W, padx=5)

        self.tb_raw_question = ctk.CTkTextbox(self.fr_raw_data, width=500)
        self.tb_raw_question.pack(anchor=ctk.W, padx=5)
        self.tb_raw_question.bind("<<Modified>>", self.on_tb_answer_change)

        # Answer TextBox
        self.lb_raw_answers = ctk.CTkLabel(self.fr_raw_data, text="Answers")
        self.lb_raw_answers.pack(anchor=ctk.W, pady=(5, 0), padx=5)

        self.tb_raw_answers = ctk.CTkTextbox(self.fr_raw_data, width=500, height=100)
        self.tb_raw_answers.pack(anchor=ctk.W, padx=5, pady=(0, 5), expand=True, fill=ctk.Y)

        # Frame for Question Final
        self.fr_fin_data = ctk.CTkFrame(self.fr_main)
        self.fr_fin_data.pack(pady=5, padx=(0, 5), side=ctk.LEFT, fill=ctk.BOTH, expand=True)

        # Question Final
        self.lb_fin_question = ctk.CTkLabel(self.fr_fin_data, text="Preview")
        self.lb_fin_question.pack(anchor=ctk.W, padx=5)

        self.tb_fin_question = ctk.CTkTextbox(self.fr_fin_data, state="disabled")  #, fg_color="transparent"
        self.tb_fin_question.pack(anchor=ctk.W, padx=5, fill=ctk.X)

        # Answer final
        self.lb_fin_answers = ctk.CTkLabel(self.fr_fin_data, text="Answers")
        self.lb_fin_answers.pack(anchor=ctk.W, pady=(5, 0), padx=5)

        self.tb_fin_answers = ctk.CTkTextbox(self.fr_fin_data, width=500, height=100)
        self.tb_fin_answers.pack(anchor=ctk.W, padx=5, pady=(0, 5), expand=True, fill=ctk.BOTH)

        # Button Close
        self.btn_close = ctk.CTkButton(self, width=200, height=40, text="Close", command=self.close,
                                        fg_color="#DA3633")
        self.btn_close.pack(side=ctk.BOTTOM, pady=30, padx=10)

    def on_tb_answer_change(self, event):
        flag = self.tb_raw_question.edit_modified()
        if flag:
            self.tb_fin_question.configure(state="normal")
            self.tb_fin_question.delete("0.0", "end")
            self.tb_fin_question.insert("0.0", text=str(self.tb_raw_question.get("0.0", "end")).strip())
            self.tb_fin_question.edit_modified(False)
            self.tb_fin_question.configure(state="disabled")

    def close(self):
        self.master.select_frame("MainFrame")


if __name__ == "__main__":
    pass
