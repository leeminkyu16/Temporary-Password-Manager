import tkinter
import module_element_password
import module_file_read_write

class ScreenAdd:
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
        string_entry_password = tkinter.StringVar(self.root)
        string_entry_confirm_password = tkinter.StringVar(self.root)


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
            element_password = module_element_password.ElementPassword(string_entry_name.get(), string_entry_description.get(), string_entry_password.get())

            module_file_read_write.file_append("data/data.txt", element_password.encode_to_base64() + "\n")     


        # Widgets Proper
        label_title = tkinter.Label(self.root, text="Add Passwords", font=("Helvetica", 24))

        label_notification = tkinter.Label(self.root, textvariable=string_label_notification, font=("Helvetica", 12))

        label_name = tkinter.Label(self.root, text="Name:", font=("Helvetica", 12))
        entry_name = tkinter.Entry(self.root, width=35, textvariable=string_entry_name)

        label_description = tkinter.Label(self.root, text="Description:", font=("Helvetica", 12))
        entry_description = tkinter.Entry(self.root, width=35, textvariable=string_entry_description)

        label_password = tkinter.Label(self.root, text="Password:", font=("Helvetica", 12))
        entry_password = tkinter.Entry(self.root, width=35, show="*", textvariable=string_entry_password)

        label_confirm_password = tkinter.Label(self.root, text="Confirm Password:", font=("Helvetica", 12))
        entry_confirm_password = tkinter.Entry(self.root, width=35, show="*", textvariable=string_entry_confirm_password)

        button_back = tkinter.Button(self.root, text="Back", font=("Helvetica", 16), command=button_back_onclick)
        button_exit = tkinter.Button(self.root, text="Exit", font=("Helvetica", 16), command=button_exit_onclick)
        button_submit = tkinter.Button(self.root, text="Submit", font=("Helvetica", 16), command=button_submit_onclick)


        # Widget Placement
        label_title.grid(row=0, column=0, columnspan=3, padx=self.width/20, pady=self.height/50)

        label_notification.grid(row=1, column=0, columnspan=3, padx=self.width/20, pady=self.height/50)

        label_name.grid(row=2, column=0, padx=self.width/20, pady=self.height/50)
        entry_name.grid(row=2, column=1, columnspan=2, padx=self.width/20, pady=self.height/50)

        label_description.grid(row=3, column=0, padx=self.width/20, pady=self.height/50)
        entry_description.grid(row=3, column=1, columnspan=2, padx=self.width/20, pady=self.height/50)

        label_password.grid(row=4, column=0, padx=self.width/20, pady=self.height/50)
        entry_password.grid(row=4, column=1, columnspan=2, padx=self.width/20, pady=self.height/50)

        label_confirm_password.grid(row=5, column=0, padx=self.width/20, pady=self.height/50)
        entry_confirm_password.grid(row=5, column=1, columnspan=2, padx=self.width/20, pady=self.height/50)

        button_back.grid(row=6, column=0, padx=self.width/20, pady=self.height/50)
        button_exit.grid(row=6, column=1, padx=self.width/20, pady=self.height/50)
        button_submit.grid(row=6, column=2, padx=self.width/20, pady=self.height/50)


        # Default values
        string_label_notification.set("Please enter the appropriate values into each field")

    def showScreen(self):
        self.root.mainloop()

def main():
    tk_temp = tkinter.Tk()
    title_screen = ScreenAdd(tk_temp, 500, 500) 
    tk_temp.destroy()
    title_screen.showScreen()
    

if __name__ == "__main__":
    main()
