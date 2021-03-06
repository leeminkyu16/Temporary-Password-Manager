import tkinter
import module_element_password
import module_file_read_write

class ScreenEditDelete:
    def __init__(self, main_root, height, width):
        # Class Attributes
        self.root = tkinter.Tk()
        self.main_root = main_root
        self.height = height
        self.width = width
        self.root.geometry(str(height) + "x" + str(width))
        self.root.resizable(0, 0)
        self.root.title("Temporary Password Manager")
        self.num_of_rows = 5
        self.num_of_columns = 3
        self.data_current_index = 0

        list_string_element_password = module_file_read_write.file_read_line_by_line("data/data.txt")
        self.list_element_password = []
        for string_element in list_string_element_password:
            element_password = module_element_password.ElementPassword()
            element_password.set_value(string_element)
            self.list_element_password.append(element_password)


        # Widgets Variables
        string_label_notification = tkinter.StringVar(self.root)
        table_string_entry_label = [[0 for x in range(self.num_of_columns)] for y in range(self.num_of_rows)]
        table_entry_label = [[0 for x in range(self.num_of_columns)] for y in range(self.num_of_rows)]
        table_button_delete = [0 for x in range(self.num_of_rows)]


        # General Functions
        def update_displayed_data():
            for i in range(self.num_of_rows):
                if (i + self.data_current_index < len(self.list_element_password)):
                    table_string_entry_label[i][0].set(self.list_element_password[i + self.data_current_index].name)
                    table_string_entry_label[i][1].set(self.list_element_password[i + self.data_current_index].description)
                    table_string_entry_label[i][2].set(self.list_element_password[i + self.data_current_index].password)

        def update_list_password_elements():
            for i in range(self.num_of_rows):
                self.list_element_password[i + self.data_current_index].name = table_string_entry_label[i][0].get()
                self.list_element_password[i + self.data_current_index].description = table_string_entry_label[i][1].get()
                self.list_element_password[i + self.data_current_index].password = table_string_entry_label[i][2].get()

        def delete_element_in_list(i):
            del self.list_element_password[i + self.data_current_index]
            update_displayed_data()


        # Widget Functions
        def button_go_to_top_onclick():
            update_list_password_elements()
            self.data_current_index = 0
            update_displayed_data()

        def button_go_to_bottom_onclick():
            if (len(self.list_element_password) - self.num_of_rows > 0):
                update_list_password_elements()
                self.data_current_index = len(self.list_element_password) - self.num_of_rows
                update_displayed_data()

        def button_go_up_onclick():
            if (self.data_current_index > 0):
                update_list_password_elements()
                self.data_current_index += -1
                update_displayed_data()
            else:
                string_label_notification.set("There are no more password up")

        def button_go_down_onclick():
            if (self.data_current_index < len(self.list_element_password) - self.num_of_rows):
                update_list_password_elements()
                self.data_current_index += 1
                update_displayed_data()
            else:
                string_label_notification.set("There are no more password down")

        def button_back_onclick():
            self.root.destroy()

        def button_save_onclick():
            update_list_password_elements()
            string_output = ""
            for i in range(len(self.list_element_password)):
                string_output += self.list_element_password[i].encode_to_base64() + "\n"
            module_file_read_write.file_write("data/data.txt", string_output)
            string_label_notification.set("Successfully saved the changes")

        def button_exit_onclick():
            try:
                self.main_root.destroy()
            except tkinter.TclError:
                pass
            self.root.destroy()


        # Widgets Proper
        label_title = tkinter.Label(self.root, text="Edit/Delete Passwords", font=("Helvetica", 24))

        label_notification = tkinter.Label(self.root, textvariable=string_label_notification, font=("Helvetica", 12))

        frame_data = tkinter.Frame(self.root, padx=self.width/20, pady=self.width/100)

        label_table_header_name = tkinter.Label(frame_data, text="Name", font=("Helvetica", 14, "underline"))
        label_table_header_description = tkinter.Label(frame_data, text="Description", font=("Helvetica", 14, "underline"))
        label_table_header_password = tkinter.Label(frame_data, text="Password", font=("Helvetica", 14, "underline"))

        for i in range(self.num_of_rows):
            for j in range(self.num_of_columns):
                table_string_entry_label[i][j] = tkinter.StringVar(frame_data)
                table_string_entry_label[i][j].set("")
                if (j == 0):
                    table_entry_label[i][j] = tkinter.Entry(frame_data, width=10, textvariable=(table_string_entry_label[i][j]), font=("Helvetica", 14))
                elif (j == 1):
                    table_entry_label[i][j] = tkinter.Entry(frame_data, width=10, textvariable=(table_string_entry_label[i][j]), font=("Helvetica", 14))
                else:
                    table_entry_label[i][j] = tkinter.Entry(frame_data, width=10, textvariable=(table_string_entry_label[i][j]), font=("Helvetica", 14))

            table_button_delete[i] = tkinter.Button(frame_data, text="Delete", font=("Helvetica", 14), command=lambda i=i: delete_element_in_list(i))                

        frame_button_movement = tkinter.Frame(self.root, padx=self.width/20, pady=self.width/100)

        button_go_to_top = tkinter.Button(frame_button_movement, text="To Top", font=("Helvetica", 14), command=button_go_to_top_onclick)
        button_go_to_bottom = tkinter.Button(frame_button_movement, text="To Bottom", font=("Helvetica", 14), command=button_go_to_bottom_onclick)
        button_go_up = tkinter.Button(frame_button_movement, text="Up", font=("Helvetica", 14), command=button_go_up_onclick)
        button_go_down = tkinter.Button(frame_button_movement, text="Down", font=("Helvetica", 14), command=button_go_down_onclick)

        frame_button_exit = tkinter.Frame(self.root, padx=self.width/20, pady=self.width/100)

        button_back = tkinter.Button(frame_button_exit, text="Back", font=("Helvetica", 14), command=button_back_onclick)
        button_save = tkinter.Button(frame_button_exit, text="Save", font=("Helvetica", 14), command=button_save_onclick)
        button_exit = tkinter.Button(frame_button_exit, text="Exit", font=("Helvetica", 14), command=button_exit_onclick)


        # Widget Placement
        label_title.grid(row=0, column=0, padx=self.width/10, pady=self.width/100)

        label_notification.grid(row=1, column=0, padx=self.width/10, pady=self.width/100)

        frame_data.grid(row=2, column=0, pady=self.width/100)

        label_table_header_name.grid(row=0, column=0, padx=self.width/20, pady=self.width/100)
        label_table_header_description.grid(row=0, column=1, padx=self.width/20, pady=self.width/100)
        label_table_header_password.grid(row=0, column=2, padx=self.width/20, pady=self.width/100)

        for i in range(self.num_of_rows):
            for j in range(self.num_of_columns):
                table_entry_label[i][j].grid(row=i+1, column=j, padx=self.width/100, pady=self.width/100)
            table_button_delete[i].grid(row=i, column=self.num_of_columns, padx=self.width/100, pady=self.width/100)

        frame_button_movement.grid(row=3, column=0, columnspan=4, pady=self.width/100)

        button_go_to_top.grid(row=0, column=0, padx=self.width/100, pady=self.width/100)
        button_go_to_bottom.grid(row=0, column=1, padx=self.width/100, pady=self.width/100)
        button_go_up.grid(row=0, column=2, padx=self.width/100, pady=self.width/100)
        button_go_down.grid(row=0, column=3, padx=self.width/100, pady=self.width/100)

        frame_button_exit.grid(row=4, column=0, columnspan=4, padx=self.width/100, pady=self.width/100)

        button_back.grid(row=0, column=0, padx=self.width/100, pady=self.width/100)
        button_save.grid(row=0, column=1, padx=self.width/100, pady=self.width/100)
        button_exit.grid(row=0, column=2, padx=self.width/100, pady=self.width/100)

        # Default values
        string_label_notification.set("Please remember to click \"save\" before exiting")
        update_displayed_data()


    def showScreen(self):
        self.root.mainloop()

def main():
    tk_temp = tkinter.Tk()
    screen_view = ScreenEditDelete(tk_temp, 550, 525) 
    tk_temp.destroy()
    screen_view.showScreen()
    

if __name__ == "__main__":
    main()
