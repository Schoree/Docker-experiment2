from pathlib import Path
from datetime import datetime

# working directory
working_dir = Path.cwd()
log_file = working_dir / "log.log"

# current date and time
def get_date_time():
    now = datetime.now()
    return now.strftime("%d.%m.%Y"), now.strftime("%H:%M:%S")

# Check existence of log.log
def write_log(log_info):
    if not log_file.exists():
        print("Warning: File not found, initialising")

        # create file and initialize
        with log_file.open("w", encoding="utf-8") as file:
            current_date, current_time = get_date_time()
            file.write(f"Datei erzeugt am {current_date} um {current_time}\n")

    current_date, current_time = get_date_time()
    log_entry = f"Aufgerufen am {current_date} um {current_time} mit Information: {log_info}"

    with log_file.open("a", encoding="utf-8") as file:
        file.write(log_entry + "\n")
    print(log_entry)