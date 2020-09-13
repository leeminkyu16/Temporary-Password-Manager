import tkinter
import string
import secrets
import module_element_password
import module_file_read_write

class ScreenGenerate:
    def __init__(self, main_root, height, width):
        # Class Attributes
        self.root = tkinter.Tk()
        self.main_root = main_root
        self.height = height
        self.width = width
        self.root.geometry(str(height) + "x" + str(width))
        self.root.resizable(0, 0)
        self.root.title("Temporary Password Manager")

        
        # Widget Variables
        string_label_notification = tkinter.StringVar(self.root)
        string_entry_name = tkinter.StringVar(self.root)
        string_entry_description = tkinter.StringVar(self.root)
        int_lower_case_letter = tkinter.IntVar(self.root)
        int_upper_case_letter = tkinter.IntVar(self.root)
        int_digits = tkinter.IntVar(self.root)
        int_punctuation = tkinter.IntVar(self.root)
        string_password_length = tkinter.StringVar(self.root)
        string_generated_password = tkinter.StringVar(self.root)


        # Widget Funtions
        def button_back_onclick():
            self.root.destroy()

        def button_exit_onclick():
            try:
                self.main_root.destroy()
            except tkinter.TclError:
                pass
            self.root.destroy()       

        def button_submit_onclick():
            try:
                int_password_length = int(string_password_length.get())
            except ValueError:
                string_label_notification.set("Please enter a valid integer for the password length")
                return

            if (int_password_length < 0):
                string_label_notification.set("Please enter a valid integer for the password length")
                return

            string_usable_chars = ""
            if (int_lower_case_letter.get() == 1):
                string_usable_chars += string.ascii_lowercase
            if (int_upper_case_letter.get() == 1):
                string_usable_chars += string.ascii_uppercase
            if (int_digits.get() == 1):
                string_usable_chars += string.digits
            if (int_punctuation.get() == 1):
                string_usable_chars += string.punctuation

            if (string_usable_chars == ""):
                string_label_notification.set("Please enter check at least one button for generation")
                return

            string_output_password = ""

            for i in range(int_password_length):
                string_output_password += string_usable_chars[secrets.randbelow(len(string_usable_chars))]

            string_generated_password.set(string_output_password)

            element_password = module_element_password.ElementPassword(string_entry_name.get(), string_entry_description.get(), string_output_password)

            module_file_read_write.file_append("data/data.txt", element_password.encode_to_base64() + "\n")

                
        # Widgets Proper
        label_title = tkinter.Label(self.root, text="Temporary Password Manager", font=("Helvetica", 20, "bold"))

        label_notification = tkinter.Label(self.root, textvariable=string_label_notification, font=("Helvetica", 12))

        label_name = tkinter.Label(self.root, text="Name:", font=("Helvetica", 12))
        entry_name = tkinter.Entry(self.root, width=35, textvariable=string_entry_name)

        label_description = tkinter.Label(self.root, text="Description:", font=("Helvetica", 12))
        entry_description = tkinter.Entry(self.root, width=35, textvariable=string_entry_description)

        frame_check_buttons = tkinter.LabelFrame(self.root, text="Check items to be used in generation", font=("Helvetica", 12), padx=self.width/50, pady=self.width/50)

        check_button_lower_case_letter = tkinter.Checkbutton(frame_check_buttons, text="Lower case letters", variable=int_lower_case_letter, font=("Helvetica", 12))
        check_button_upper_case_letter = tkinter.Checkbutton(frame_check_buttons, text="Upper case letters", variable=int_upper_case_letter, font=("Helvetica", 12))

        check_button_digits = tkinter.Checkbutton(frame_check_buttons, text="Digits", variable=int_digits, font=("Helvetica", 12))
        check_button_punctuation = tkinter.Checkbutton(frame_check_buttons, text="Punctuation", variable=int_punctuation, font=("Helvetica", 12))

        label_password_length = tkinter.Label(self.root, text="Password Length:", font=("Helvetica", 12))
        entry_password_length = tkinter.Entry(self.root, width=35, textvariable=string_password_length)

        entry_generated_password = tkinter.Entry(self.root, width=65, textvariable=string_generated_password)

        button_back = tkinter.Button(self.root, text="Back", font=("Helvetica", 16), command=button_back_onclick)
        button_exit = tkinter.Button(self.root, text="Exit", font=("Helvetica", 16), command=button_exit_onclick)
        button_generate = tkinter.Button(self.root, text="Generate", font=("Helvetica", 16), command=button_submit_onclick)


        # Widget Placement
        label_title.grid(row=0, column=0, columnspan=3, padx=self.width/20, pady=self.height/50)

        label_notification.grid(row=1, column=0, columnspan=3, padx=self.width/20, pady=self.height/50)

        label_name.grid(row=2, column=0, padx=self.width/20, pady=self.height/50)
        entry_name.grid(row=2, column=1, columnspan=2, padx=self.width/20, pady=self.height/50)

        label_description.grid(row=3, column=0, padx=self.width/20, pady=self.height/50)
        entry_description.grid(row=3, column=1, columnspan=2, padx=self.width/20, pady=self.height/50)

        frame_check_buttons.grid(row=4, column=0, columnspan=3, padx=self.width/20, pady=self.height/50)

        check_button_lower_case_letter.grid(row=0, column=0, padx=self.width/20, pady=self.height/50)
        check_button_upper_case_letter.grid(row=0, column=1, padx=self.width/20, pady=self.height/50)
        check_button_digits.grid(row=1, column=0, padx=self.width/20, pady=self.height/50)
        check_button_punctuation.grid(row=1, column=1, padx=self.width/20, pady=self.height/50)

        label_password_length.grid(row=5, column=0, padx=self.width/20, pady=self.height/50)
        entry_password_length.grid(row=5, column=1, columnspan=2, padx=self.width/20, pady=self.height/50)

        entry_generated_password.grid(row=6, column=0, columnspan=3, padx=self.width/20, pady=self.height/50)

        button_back.grid(row=7, column=0, padx=self.width/20, pady=self.height/50)
        button_exit.grid(row=7, column=1, padx=self.width/20, pady=self.height/50)
        button_generate.grid(row=7, column=2, padx=self.width/20, pady=self.height/50)


        # Default values
        string_label_notification.set("Please enter the appropriate values into each field")

    def showScreen(self):
        self.root.mainloop()

def main():
    tk_temp = tkinter.Tk()
    title_screen = ScreenGenerate(tk_temp, 500, 525)
    tk_temp.destroy()
    title_screen.showScreen()
    

if __name__ == "__main__":
    main()
