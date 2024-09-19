import time
import shutil

def format_time(seconds):
    """
    Format the given time in seconds as MM:SS.

    Args:
        seconds (float): Time in seconds.

    Returns:
        str: Formatted time in the format MM:SS.
    """
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range):
    totalElements = len(lst)
    timeStart = time.time()

    terminalWidth = shutil.get_terminal_size().columns - 30
    terminalBarWidth = terminalWidth - 10

    for i, item in enumerate(lst, start=1):
        progressedWidth = int(i / totalElements * terminalBarWidth)
        timeElapsed = time.time() - timeStart
        progressSpeed = i / timeElapsed
        timeEstimate = (totalElements - i) / progressSpeed

        progressBar = f"|{'█' * progressedWidth:<{terminalBarWidth}}|"
        prograssPercent = progressedWidth * 100 // terminalBarWidth
        progressInfo = f"{prograssPercent}%{progressBar} {i}/{totalElements}"
        timeInfo = f"[{format_time(timeElapsed)}<{format_time(timeEstimate)}, {progressSpeed:.2f}it/s]"

        print(f"\r{progressInfo} {timeInfo}", end="", flush=True)
        yield item