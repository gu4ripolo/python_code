import time
def progress_bar(part, total, lenght=30):
    fracc = part/total
    completed = int(fracc * lenght)
    missing = lenght - completed
    bar = f"[{'#' * completed}{'-' * missing}]{fracc:.2%}"
    return bar

n = 30
for i in range(n + 1):
    time.sleep(0.1)
    print(progress_bar(i, n), end='\r')

