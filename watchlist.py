from utils import load_json, save_json
from constants import WATCHLIST_FILE


class WatchlistManager:
    def __init__(self):
        self.watchlist = load_json(WATCHLIST_FILE)

    def add_movie(self, movie):
        if movie not in self.watchlist:
            self.watchlist.append(movie)
            save_json(WATCHLIST_FILE, self.watchlist)

    def remove_movie(self, movie):
        if movie in self.watchlist:
            self.watchlist.remove(movie)
            save_json(WATCHLIST_FILE, self.watchlist)

    def get_movies(self):
        return self.watchlist
