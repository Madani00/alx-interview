#!/usr/bin/python3
""" module """
import sys
import signal


def print_statistics(status_counts, total_size):
    """Print the collected statistics."""
    print("File size: {:d}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{:d}: {}".format(code, status_counts[code]))


def handle_sigint(signum, frame):
    """Handle the SIGINT signal (Ctrl + C) and print statistics."""
    print_statistics(status_counts, total_size)
    sys.exit(0)


# Register the SIGINT signal handler
signal.signal(signal.SIGINT, handle_sigint)

if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}
    try:
        for line in sys.stdin:
            data = line.strip().split()
            try:
                total_size += int(data[-1])
                status_code = int(data[-2])
                if status_code in status_counts:
                    status_counts[status_code] += 1
                    line_count += 1
            except Exception:
                pass
            if line_count % 10 == 0:
                print_statistics(status_counts, total_size)

    except KeyboardInterrupt:
        print("\nKeyboard interrupt received while reading from stdin.")
        print_statistics(status_counts, total_size)
        sys.exit(0)

    print_statistics(status_counts, total_size)
