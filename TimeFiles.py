#add a timestamp to a filenames
import datatime as dt
def timestamp():
    return f"{dt.datatime.now():%Y%m%d%H%M%S}"

with open(f"myfile_{timestamp()}.txt") as f:
    f.write("Hello!")
