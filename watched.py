from utils import load_json, save_json
from constants import WATCHED_FILE


class WatchedManager:
    def __init__(self):
        self.watched = load_json(WATCHED_FILE)

    def add_movie(self, movie):
        if movie not in self.watched:
            self.watched.append(movie)
            save_json(WATCHED_FILE, self.watched)

    def get_movies(self):
        return self.watched
