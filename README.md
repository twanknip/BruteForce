# BruteForce Detection Tool

A build an Python-based detection engine for identifying brute-force attacks from log data.

---

## Overview

The **BruteForce Detection Tool** ingests authentication-related logs, analyzes them using detection logic, and raises alerts when brute-force patterns are identified.

---

## Features

- Modular architecture (ingestion, detection, alerting)
- Brute-force detection based on configurable thresholds
- Supports file-based log ingestion (initial version)
- Designed for extension to live log streams
- Clean separation between data ingestion and detection logic
- Git-safe: no sensitive data or logs stored in the repository

---

## Planned Features

- Live log ingestion via STDIN (--stdin)
- Real-time detection of brute-force attacks
- Integration with SIEM tools and log forwarders

## Usage

### Basic Usage

Run the application from the project root:

```bash
python main.py --file logs.txt


BruteForce/
├── ingestion/      # Log ingestion modules
├── detection/      # Brute-force detection logic
├── alerts/         # Alert handling and notification logic
├── models/         # Detection models and data structures
├── utils/          # Shared utilities and helpers
├── main.py         # Application entry point
├── README.md
└── .gitignore

