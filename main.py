from PySide6.QtWidgets import QApplication
from nav_sentimentanlysis_page import MyAnalysisSentiment
import sys

def main():
    app = QApplication(sys.argv)
    window = MyAnalysisSentiment()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
