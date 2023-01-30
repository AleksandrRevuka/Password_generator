import tkinter as tk
import customtkinter as CTk
import password

from PIL import Image
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        CTk.set_appearance_mode("Dark")
        self.geometry("460x320")
        self.title("Password generator")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(dark_image=Image.open("img.png"), size=(460, 150))
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0, padx=(0, 20))

        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=280)
        self.entry_password.grid(row=1, column=0, padx=(0, 20))

        self.btn_generate = CTk.CTkButton(master=self.password_frame, text="Generate and copy", width=120,
                                          command=self.set_password)
        self.btn_generate.grid(row=1, column=1, padx=(0, 20))

        self.settings_frame = CTk.CTkFrame(master=self,  width=120)
        self.settings_frame.grid(row=2, column=0, padx=(20, 0), pady=(20, 20), sticky="w")

        self.password_length_slider = CTk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100,
                                                    command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        self.password_length_entry = CTk.CTkEntry(master=self.settings_frame, width=80)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="ew")

        self.cb_digits_var = tk.StringVar()

        self.cb_digits = CTk.CTkCheckBox(master=self.settings_frame, text="0-9",
                                         variable=self.cb_digits_var, onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=5)

        self.cb_lower_var = tk.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var,
                                        onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tk.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var,
                                        onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbols_var = tk.StringVar()
        self.cb_symbols = CTk.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cb_symbols_var,
                                          onvalue=punctuation, offvalue="")
        self.cb_symbols.grid(row=2, column=3)

        self.password_length_slider.set(32)
        self.password_length_entry.insert(0, "32")
        # self.cb_digits.select(1)
        # self.cb_upper.select(1)
        # self.cb_lower.select(1)

    def slider_event(self, value):
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(0, int(value))

    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get() +
                        self.cb_symbols_var.get())
        return chars

    def set_password(self):
        self.entry_password.delete(0, "end")
        password_for_copy = password.create_new(length=int(self.password_length_slider.get()),
                                                characters=self.get_characters())
        self.entry_password.insert(0, password_for_copy)
        self.entry_password.clipboard_clear()
        self.entry_password.clipboard_append(password_for_copy)


if __name__ == '__main__':
    app = App()
    app.mainloop()
