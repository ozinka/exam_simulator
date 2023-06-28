import customtkinter as ctk


class DumpFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Button Cancel
        self.btn_cancel = ctk.CTkButton(self, width=200, height=40, text="Cancel", command=self.cancel,
                                        fg_color="#DA3633")
        self.btn_cancel.pack(side=ctk.BOTTOM, pady=30, padx=10, anchor=ctk.E)

    def cancel(self):
        self.master.select_frame("MainFrame")


if __name__ == "__main__":
    pass
