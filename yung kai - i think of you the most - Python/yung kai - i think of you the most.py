import time
import sys

print(" n \ n")

lyrics = [
    ("I'll always come back to you <3", 1.5, 0.15),
    ("You and the sky I'm thinkin of", 1.0, 0.04),
    ("Count how many days til it's enough", 1.0, 0.05),
    ("To make you fall in love, I'll be your one", 0.9, 0.07),
    ("Can it be this way? Oh my, oh my, oh, my", 0.8, 0.08),
    ("If I, if I, if I were to let you go, I'd be a fool", 0.8, 0.07),
    ("I'll just wait for you", 1.2, 0.10),
]
def type_out(text, char_delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def play_lyrics(lyrics):
    for line, line_delay, char_delay in lyrics:
        type_out(line, char_delay)
        time.sleep(line_delay)

if __name__ == "__main__":
    play_lyrics(lyrics)