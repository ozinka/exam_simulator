import customtkinter as ctk
from qa_parser import *


class DumpFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # # Frame main
        self.fr_main = ctk.CTkFrame(self, fg_color="transparent")
        self.fr_main.pack(fill=ctk.BOTH, expand=True)

        # # Frame tool box
        self.fr_tool_box = ctk.CTkFrame(self.fr_main, height=50)
        self.fr_tool_box.pack(side=ctk.TOP, fill=ctk.X, padx=5, pady=(5, 0))

        # # Frame for Buttons
        self.fr_tool_box = ctk.CTkFrame(self.fr_tool_box, height=50)
        self.fr_tool_box.pack(side=ctk.TOP, fill=ctk.X, padx=5, pady=(5, 0))

        # # Frame for raw Data
        self.fr_raw_data = ctk.CTkFrame(self.fr_main, fg_color="transparent")
        self.fr_raw_data.pack(pady=5, padx=5, side=ctk.LEFT, anchor=ctk.N, fill=ctk.Y)

        # Question TextBox
        self.lb_raw_question = ctk.CTkLabel(self.fr_raw_data, text="Question")
        self.lb_raw_question.pack(anchor=ctk.W, padx=5)

        self.tb_raw_question = ctk.CTkTextbox(self.fr_raw_data, width=500)
        self.tb_raw_question.pack(anchor=ctk.W, padx=5, side=ctk.LEFT, fill=ctk.BOTH)
        self.tb_raw_question.bind("<<Modified>>", self.on_tb_question_change)

        # # Frame Middle
        self.fr_middle = ctk.CTkFrame(self.fr_main, width=20, fg_color="transparent")
        self.fr_middle.pack(side=ctk.LEFT, fill=ctk.Y, anchor=ctk.W, padx=(0, 5), pady=5)

        self.bt_move_right = ctk.CTkButton(self.fr_middle, text=">>", width=10)
        self.bt_move_right.pack(pady=(120, 0), padx=5)

        # # Frame Final
        self.fr_fin_data = ctk.CTkFrame(self.fr_main)
        self.fr_fin_data.pack(pady=5, padx=(0, 5), side=ctk.LEFT, fill=ctk.BOTH, expand=True, anchor=ctk.W)

        # Question Final
        self.lb_fin_question = ctk.CTkLabel(self.fr_fin_data, text="Preview")
        self.lb_fin_question.pack(anchor=ctk.W, padx=5)

        self.tb_fin_question = ctk.CTkTextbox(self.fr_fin_data, fg_color="transparent",
                                              border_color=("gray90", "gray13"), border_width=1, font=("Verdana", 13),
                                              wrap='word')
        self.tb_fin_question.pack(anchor=ctk.W, padx=5, fill=ctk.X)

        # Answer final
        self.question_type = ctk.CTkSegmentedButton(self.fr_fin_data)
        self.question_type.configure(values=["Single chose", "Multi chose"])
        self.question_type.set("Single chose")
        self.question_type.pack(anchor=ctk.W, pady=(5, 0), padx=5)

        self.fr_fin_answers = ctk.CTkFrame(self.fr_fin_data, width=500, height=100, fg_color="transparent",
                                           border_color=("gray90", "gray13"), border_width=1)
        self.fr_fin_answers.pack(anchor=ctk.W, padx=5, pady=(0, 5), expand=True, fill=ctk.BOTH)

        # Button Close
        self.btn_close = ctk.CTkButton(self, width=200, height=40, text="Close", command=self.close,
                                       fg_color="#DA3633")
        self.btn_close.pack(side=ctk.BOTTOM, pady=30, padx=10)

        # Set test question
        self.tb_raw_question.insert("0.0", text=example_question)

    def on_tb_question_change(self, event):
        flag = self.tb_raw_question.edit_modified()
        if flag:
            parsed_question = parse_question(self.tb_raw_question.get("0.0", "end"))
            self.tb_fin_question.delete("0.0", "end")
            self.tb_fin_question.insert("0.0", text=parsed_question[0])
            self.update_answers(parsed_question[1], parsed_question[2])
        self.tb_raw_question.edit_modified(False)

    def update_answers(self, answers: list, q_type=0, valid_answer=[]):
        self.clear_answers()
        if answers:
            i = 0
            for k in answers:
                _ = None
                if q_type == 0:
                    _ = ctk.CTkRadioButton(self.fr_fin_answers, value=i, text=k)
                else:
                    _ = ctk.CTkCheckBox(self.fr_fin_answers, text=k)
                _.pack(anchor=ctk.W, padx=5, pady=(20, 0))
            i += 1

    def clear_answers(self):
        for widget in self.fr_fin_answers.winfo_children():
            widget.destroy()

    def close(self):
        self.master.select_frame("MainFrame")


if __name__ == "__main__":
    pass
