import argparse
import json

from detection.brute_force_rule import BruteForceRule
from detection.engine import DetectionEngine
from ingestion.log_reader import LogReader
from ingestion.live_log_reader import LiveLogReader


def parse_args():
    parser = argparse.ArgumentParser(
        description="Brute force detection tool"
    )

    parser.add_argument(
        "--logfile",
        required=True,
        help="Path to log file"
    )

    parser.add_argument(
        "--live",
        action="store_true",
        help="Enable live log monitoring"
    )

    parser.add_argument(
        "--max-failures",
        type=int,
        default=3,
        help="Maximum failed attempts before alert"
    )

    parser.add_argument(
        "--window",
        type=int,
        default=60,
        help="Time window in seconds"
    )

    return parser.parse_args()


def print_alerts(alerts):
    output = []

    for alert in alerts:
        output.append({
            "rule": alert.rule_name,
            "severity": alert.severity,
            "timestamp": alert.timestamp.isoformat(),
            "event_count": len(alert.evidence),
            "events": [
                {
                    "timestamp": e.timestamp.isoformat(),
                    "ip_address": e.ip_address,
                    "username": e.username,
                    "success": e.success
                }
                for e in alert.evidence
            ]
        })

    if output:
        print(json.dumps(output, indent=2))


def main():
    args = parse_args()

    rule = BruteForceRule(
        max_failures=args.max_failures,
        window_seconds=args.window
    )

    engine = DetectionEngine([rule])

    if args.live:
        print("Starting live log monitoring...")
        reader = LiveLogReader(args.logfile)

        for event in reader.follow():
            engine.add_event(event)
            alerts = engine.run()
            print_alerts(alerts)

    else:
        reader = LogReader()
        events = reader.read_file(args.logfile)

        print(f"Events read: {len(events)}")

        for event in events:
            engine.add_event(event)

        alerts = engine.run()
        print_alerts(alerts)


if __name__ == "__main__":
    main()
