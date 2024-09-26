import sys
from PyQt5.QtWidgets import QApplication
from gemini_handler.gemini_handler import GeminiHandler
from ui.ui import MainUI

def main():
    # Initialize Gemini Handler (API keys can be passed if needed)
    gemini_handler = GeminiHandler()

    # Initialize PyQt5 Application
    app = QApplication(sys.argv)
    main_window = MainUI(gemini_handler)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
