import time
from logic.morse_decoder import decode_morse

LETTER_GAP = 1.0
WORD_GAP = 2.5


class MorseBuffer:
    def __init__(self):
        self.current_symbol = ""
        self.current_word = ""
        self.final_text = ""

        self.last_blink_time = None
        self.letter_committed = False

        # callback (for logging)
        self.on_word_commit = lambda word: None

    def set_word_callback(self, callback):
        self.on_word_commit = callback

    def add_symbol(self, symbol):
        self.current_symbol += symbol
        self.last_blink_time = time.time()
        self.letter_committed = False

    def update(self):
        if self.last_blink_time is None:
            return

        now = time.time()
        silence = now - self.last_blink_time

        # Commit LETTER
        if silence >= LETTER_GAP and not self.letter_committed and self.current_symbol:
            letter = decode_morse(self.current_symbol)
            self.current_word += letter
            self.current_symbol = ""
            self.letter_committed = True

        # Commit WORD
        if silence >= WORD_GAP and self.current_word:
            self.final_text += self.current_word + " "
            self.on_word_commit(self.current_word)
            self.current_word = ""
            self.last_blink_time = None
            self.letter_committed = False
