from PyQt6.QtWidgets import QMainWindow, QTextEdit


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700,500)


        #  Add chat area widget
        self.chat_area = QTextEdit(self)

        # Add input field widget


        # Add the button

class Chatbot:
    pass
