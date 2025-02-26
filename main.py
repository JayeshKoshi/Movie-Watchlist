from PyQt6.QtWidgets import QApplication
from ui import MovieTrackerApp

if __name__ == "__main__":
    app = QApplication([])
    window = MovieTrackerApp()
    window.show()
    app.exec()
