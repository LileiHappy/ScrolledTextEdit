from tkinter import Tk
from tkinter import Frame
from scrolled_text_edit import ScrolledTextEdit


class Test:
    def __init__(self):
        self.__root = Tk()
        self.__text = None

    def __fetch_screen_size(self):
        return self.__root.winfo_screenwidth(), self.__root.winfo_screenheight()

    def calculate_display_info(self):
        screen_width, screen_height = self.__fetch_screen_size()
        window_width = int(screen_width * 3 / 4)
        window_height = int(screen_height * 3 / 4)
        display_start_point_x = (screen_width - window_width) >> 1
        display_start_point_y = (screen_height - window_height) >> 1
        display_info = (window_width, window_height, display_start_point_x, display_start_point_y)
        return display_info

    def display_in_center(self, display_info):
        self.__root.title('ScrollTextEdit')
        self.__root.configure(background='#20B2AA')
        self.__root.geometry('{}x{}+{}+{}'.format(display_info[0], display_info[1], display_info[2], display_info[3]))

    def create_view(self):
        text_edit = ScrolledTextEdit(self.__root,
                                     hint='Please enter your text here',
                                     content_changed_command=self.__on_content_changed,
                                     width=100,
                                     height=30,
                                     highlightcolor='green',
                                     highlightthickness=1,
                                     highlightbackground='white',
                                     background='#20B2AA')
        text_edit.place(relx=0.5, rely=0.5, anchor='center')

    def __on_content_changed(self, text):
        self.__text = text
        print('The currently entered text is ', text)

    def show(self):
        self.__root.mainloop()

    def destroy(self):
        self.__root.destroy()


def main():
    test = Test()
    display_info = test.calculate_display_info()
    test.display_in_center(display_info)
    test.create_view()
    test.show()


if __name__ == '__main__':
    main()
