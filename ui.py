from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QTabWidget, QMessageBox
from PyQt6.QtCore import Qt
import webbrowser
from search import search_movies
from watchlist import WatchlistManager
from watched import WatchedManager
from constants import BASE_URL, API_KEY


class MovieTrackerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie & TV Show Tracker")
        self.setGeometry(100, 100, 500, 600)
        self.setStyleSheet("background-color: #121212; color: white;")

        self.layout = QVBoxLayout()
        self.tabs = QTabWidget(self)

        # Watchlist & Watched Managers
        self.watchlist_manager = WatchlistManager()
        self.watched_manager = WatchedManager()

        # Search Tab
        self.search_tab = QWidget()
        self.search_layout = QVBoxLayout()

        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search for a Movie or TV Show...")
        self.search_bar.setStyleSheet(
            "padding: 10px; font-size: 16px; background-color: #333; color: white; border-radius: 10px;")

        self.search_button = QPushButton("Search", self)
        self.search_button.setStyleSheet(
            "background-color: #1DB954; color: white; font-size: 16px; padding: 10px; border-radius: 10px;")
        self.search_button.clicked.connect(self.search)

        self.result_list = QListWidget(self)
        self.result_list.setStyleSheet(
            "background-color: #222; color: white; font-size: 14px;")
        self.result_list.itemClicked.connect(self.enable_trailer_button)
        self.result_list.itemDoubleClicked.connect(self.add_to_watchlist)

        self.trailer_button = QPushButton("Show Trailer", self)
        self.trailer_button.setStyleSheet(
            "background-color: #FF4500; color: white; font-size: 16px; padding: 10px; border-radius: 10px;")
        self.trailer_button.setVisible(False)
        self.trailer_button.clicked.connect(self.show_trailer)

        self.search_layout.addWidget(self.search_bar)
        self.search_layout.addWidget(self.search_button)
        self.search_layout.addWidget(self.result_list)
        self.search_layout.addWidget(self.trailer_button)
        self.search_tab.setLayout(self.search_layout)

        # Watchlist Tab
        self.watchlist_tab = QWidget()
        self.watchlist_layout = QVBoxLayout()
        self.watchlist_list = QListWidget(self)
        self.watchlist_list.setStyleSheet(
            "background-color: #222; color: white; font-size: 14px;")

        self.load_watchlist_ui()

        self.watchlist_layout.addWidget(self.watchlist_list)
        self.watchlist_tab.setLayout(self.watchlist_layout)

        # Watched Tab
        self.watched_tab = QWidget()
        self.watched_layout = QVBoxLayout()
        self.watched_list = QListWidget(self)
        self.watched_list.setStyleSheet(
            "background-color: #222; color: white; font-size: 14px;")

        self.load_watched_ui()

        self.watched_layout.addWidget(self.watched_list)
        self.watched_tab.setLayout(self.watched_layout)

        self.tabs.addTab(self.search_tab, "Search")
        self.tabs.addTab(self.watchlist_tab, "Watchlist")
        self.tabs.addTab(self.watched_tab, "Watched")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def search(self):
        query = self.search_bar.text()
        results = search_movies(query)
        self.result_list.clear()
        for movie in results:
            self.result_list.addItem(
                f"{movie['title']} ({movie.get('release_date', 'Unknown')})")

    def enable_trailer_button(self):
        self.trailer_button.setVisible(True)

    def show_trailer(self):
        selected_item = self.result_list.currentItem()
        if selected_item:
            movie_name = selected_item.text().split(" (")[0]
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={movie_name} trailer")

    def add_to_watchlist(self, item):
        movie_name = item.text()
        self.watchlist_manager.add_movie(movie_name)
        self.load_watchlist_ui()

    def load_watchlist_ui(self):
        self.watchlist_list.clear()
        for movie in self.watchlist_manager.get_movies():
            self.watchlist_list.addItem(movie)

    def load_watched_ui(self):
        self.watched_list.clear()
        for movie in self.watched_manager.get_movies():
            self.watched_list.addItem(movie)
