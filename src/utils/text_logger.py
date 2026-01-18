import os
from datetime import datetime


class TextLogger:
    def __init__(self, file_path="logs/output.txt"):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.file_path = file_path

    def log_session_start(self):
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(f"\n--- Session {datetime.now()} ---\n")

    def log_word(self, word):
        if not word:
            return
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(word + "\n")
