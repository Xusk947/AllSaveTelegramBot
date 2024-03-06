import time

SAVE_PATH = "C:/Users/Xusk9/Downloads"


def get_current_time_in_ns() -> str:
    return str(int(time.time() * 1e9))