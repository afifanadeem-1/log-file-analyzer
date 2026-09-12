import argparse
import sys
from datetime import datetime


parser=argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("--start", default=None)
parser.add_argument("--end", default=None)
parser.add_argument("--export", action="store_true")
args=parser.parse_args()

error_count=0
warning_count=0
info_count=0
total=0

try:
    with open (args.filename, "r")as file:
        content=file.readlines()

except FileNotFoundError:
    print("File is not found")
    sys.exit(1)

if args.start:
    try:
        start_date = datetime.strptime(args.start, "%Y-%m-%d")
    except ValueError:
        print("Invalid start date. Use YYYY-MM-DD.")
        sys.exit(1)
else:
    start_date = None

if args.end:
    try:
        end_date = datetime.strptime(args.end, "%Y-%m-%d")
    except ValueError:
        print("Invalid end date. Use YYYY-MM-DD.")
        sys.exit(1)
else:
    end_date = None
for line in content:

    if not line.strip():
        continue
    line_date_str = line.split(" ")[0]
    line_date = datetime.strptime(line_date_str, "%Y-%m-%d")
    if start_date and line_date < start_date:
        continue
    if end_date and line_date > end_date:
        continue
    total += 1

    if "ERROR" in line:
        error_count += 1
    elif "WARNING" in line:
        warning_count += 1
    elif "INFO" in line:
        info_count += 1
summary=(
    "Log Summary\n"
    f"Total Lines: {total}\n"
    f"ERROR: {error_count}\n"
    f"WARNING: {warning_count}\n"
    f"INFO: {info_count}\n"
)

if args.export:
    with open("summary.txt", "w") as file:
        file.write(summary)

    print("Summary exported to summary.txt")

else:
    print(summary)
