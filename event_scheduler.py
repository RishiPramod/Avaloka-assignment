import heapq


def can_attend_all(events):
    """Return whether one person can attend every event."""
    ordered = sorted(events, key=lambda event: event[0])

    # Validate all events before checking for overlaps.
    for start, end in ordered:
        if start >= end:
            raise ValueError("Each event must have start < end.")

    for i in range(1, len(ordered)):
        current_start = ordered[i][0]
        previous_end = ordered[i - 1][1]

        if current_start < previous_end:
            return False

    return True


def min_rooms_required(events):
    """Return the minimum number of rooms needed."""
    ordered = sorted(events, key=lambda event: event[0])

    active_end_times = []
    max_rooms = 0

    for start, end in ordered:
        if start >= end:
            raise ValueError("Each event must have start < end.")

        # Remove meetings that have finished.
        while active_end_times and active_end_times[0] <= start:
            heapq.heappop(active_end_times)

        heapq.heappush(active_end_times, end)
        max_rooms = max(max_rooms, len(active_end_times))

    return max_rooms


if __name__ == "__main__":
    schedules = [
        [(9, 10), (10, 11), (11, 12)],
        [(9, 12), (10, 11), (11, 13)],
        [(9, 11), (9, 11), (9, 11)],
        [],
    ]

    for number, events in enumerate(schedules, start=1):
        print(f"Schedule {number}: {events}")
        print(f"Can attend all: {can_attend_all(events)}")
        print(f"Minimum rooms: {min_rooms_required(events)}")
        print()