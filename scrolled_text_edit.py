from tkinter.scrolledtext import ScrolledText


class ScrolledTextEdit(ScrolledText):
    def __init__(self, container_view, hint, content_changed_command=None, **kwargs):
        super().__init__(container_view, **kwargs)
        self.__hint = hint
        self.__content_changed_command = content_changed_command
        self.__create_text_view()

    def __create_text_view(self):
        self.__show_hint()
        self.bind('<FocusIn>', self.__on_focus)
        self.bind('<FocusOut>', self.__on_focus_lost)
        self.bind("<KeyRelease>", self.__on_text_changed)

    def __show_hint(self):
        self.insert('end', self.__hint)
        self.configure(foreground='#FFE4E1')

    def __on_focus(self, event):
        if self.get(1.0, 'end').strip() != self.__hint:
            return
        self.delete(1.0, 'end')
        self.insert('end', '')
        self.configure(foreground='white')

    def __on_focus_lost(self, event):
        content = self.get(1.0, 'end').strip()
        if content != '':
            if self.__content_changed_command:
                self.__content_changed_command(content)
            return
        self.__show_hint()

    def __on_text_changed(self, event):
        content = self.get(1.0, 'end').strip()
        if content != '':
            if self.__content_changed_command:
                self.__content_changed_command(content)
