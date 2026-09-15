# Log File Analyzer CLI

A command-line tool that reads log files and summarizes ERROR, WARNING, and INFO occurrences. Supports date-range filtering, exporting results to a file, and runs both locally and inside a Docker container.

## Features

- Counts occurrences of `ERROR`, `WARNING`, and `INFO` log levels
- Filters log entries by date range (`--start` / `--end`)
- Exports summary to a file (`--export`)
- Handles missing files, missing arguments, invalid dates, and blank lines gracefully
- Fully containerized with Docker

## Requirements

- Python 3.11+ (for local use)
- Docker (for containerized use)

## Usage (Local)

```bash
python analyzer.py <filename>
```

### Optional flags

| Flag | Description |
|------|-------------|
| `--start YYYY-MM-DD` | Only count entries on or after this date |
| `--end YYYY-MM-DD` | Only count entries on or before this date |
| `--export` | Write the summary to `summary.txt` instead of printing it |

### Examples

```bash
python analyzer.py sample.log
python analyzer.py sample.log --start 2026-09-01 --end 2026-09-02
python analyzer.py sample.log --export
```

## Usage (Docker)

Build the image:

```bash
docker build -t log-analyzer .
```

Run it:

```bash
docker run log-analyzer sample.log
```

With flags:

```bash
docker run log-analyzer sample.log --start 2026-09-01 --export
```

> Note: `--export` writes `summary.txt` inside the container's filesystem. To copy it to your local machine:
> ```bash
> docker cp <container_id>:/app/summary.txt .
> ```

## Sample Log Format
