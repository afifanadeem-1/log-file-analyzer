import sys

if len(sys.argv) < 2:
    print("Usage: python analyzer.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

error_count=0
warning_count=0
info_count=0

try:
    with open (filename, "r")as file:
        content=file.readlines()

except FileNotFoundError:
    print("File is not found")
    sys.exit(1)

for line in content:
    if "ERROR" in line:
        error_count+=1
    elif "WARNING" in line:
        warning_count+=1
    elif "INFO" in line:
        info_count+=1

print("Log Summary")
print(f"Total Lines: {len(content)}")
print(f"ERROR: {error_count}")
print(f"WARNING: {warning_count}")
print(f"INFO: {info_count}")
