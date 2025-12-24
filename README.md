# BruteForce Detection Tool

A build an Python-based detection engine for identifying brute-force attacks from log data.  

---

## Overview

The **BruteForce Detection Tool** ingests authentication-related logs, analyzes them using detection logic, and raises alerts when brute-force patterns are identified.

The project is intentionally structured to resemble real-world SOC / SIEM tooling and can be extended to support live log sources such as syslog, sockets, or Windows event logs.

---

## Features

- Modular architecture (ingestion, detection, alerting)
- Brute-force detection based on configurable thresholds
- Supports file-based log ingestion (initial version)
- Designed for extension to live log streams
- Clean separation between data ingestion and detection logic
- Git-safe: no sensitive data or logs stored in the repository

---

## Usage

### Basic Usage

Run the application from the project root:

```bash
python main.py --file logs.txt

## Project Structure

```text
BruteForce/
├── ingestion/      # Log ingestion modules
├── detection/      # Brute-force detection logic
├── alerts/         # Alert handling and notification logic
├── models/         # Detection models and data structures
├── utils/          # Shared utilities and helpers
├── main.py         # Application entry point
├── README.md
└── .gitignore

## Planned Features
- Live log ingestion via STDIN (`--stdin`)
- Real-time detection of brute-force attacks
- Integration with SIEM tools and log forwarders
