import tkinter
import module_generate
import module_add
import module_view
import module_edit_delete

class ScreenTable:
    def __init__(self, height, width):
        # Class Attributes
        self.root = tkinter.Tk()
        self.height = height
        self.width = width
        self.root.geometry(str(height) + "x" + str(width))
        self.root.resizable(0, 0)
        self.root.title("Temporary Password Manager")

        # Widget Functions
        def button_generate_onclick():
            generate_screen = module_generate.ScreenGenerate(self.root, 500, 525)
            generate_screen.showScreen()

        def button_add_onclick():
            add_screen = module_add.ScreenAdd(self.root, 500, 500)
            add_screen.showScreen()

        def button_view_onclick():
            view_screen = module_view.ScreenView(self.root, 525, 500)
            view_screen.showScreen()

        def button_edit_delete_onclick():
            screen_edit_delete = module_edit_delete.ScreenEditDelete(self.root, 550, 525)
            screen_edit_delete.showScreen()

        def button_exit_onclick():
            self.root.destroy()

        # Widgets Proper
        label_title = tkinter.Label(self.root, text="Temporary Password Manager", font=("Helvetica", 24))
        button_generate = tkinter.Button(self.root, text="Generate New Password", font=("Helvetica", 18), command=button_generate_onclick)
        button_add = tkinter.Button(self.root, text="Add Password", font=("Helvetica", 18), command=button_add_onclick)
        button_view = tkinter.Button(self.root, text="View Passwords", font=("Helvetica", 18), command=button_view_onclick)
        button_edit_delete = tkinter.Button(self.root, text="Edit/Delete Passwords", font=("Helvetica", 18), command=button_edit_delete_onclick)
        button_exit = tkinter.Button(self.root, text="Exit", font=("Helvetica", 18), command=button_exit_onclick)

        # Widget Placement
        label_title.grid(row=0, column=0, padx=self.width/20, pady=self.width/50)
        button_generate.grid(row=1, column=0, padx=self.width/20, pady=self.width/50)
        button_add.grid(row=2, column=0, padx=self.width/20, pady=self.width/50)
        button_view.grid(row=3, column=0, padx=self.width/20, pady=self.width/50)
        button_edit_delete.grid(row=4, column=0, padx=self.width/20, pady=self.width/50)
        button_exit.grid(row=5, column=0, padx=self.width/20, pady=self.width/50)


    def showScreen(self):
        self.root.mainloop()

def main():
    title_screen = ScreenTable(500, 500) 
    title_screen.showScreen()

if __name__ == "__main__":
    main()
