# 🧹 Duplicate File Cleaner & Log Automation

A Python-based automation tool that monitors a specified directory, removes empty files, and logs the cleanup activity. Designed for system hygiene, file maintenance, and automation enthusiasts.

---

## 📌 Features

- Scans a directory and its subdirectories
- Identifies and deletes **empty files**
- Logs:
  - Total files scanned
  - Empty files removed
  - Timestamp of cleanup
- Supports **command-line usage** with help and usage flags
- Scheduled to run automatically every 6 seconds (adjustable)

---

## 🛠 Requirements

- Python 3.x
- [schedule](https://pypi.org/project/schedule/)

Install dependencies:

```bash
pip install schedule
