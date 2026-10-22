# Avaloka Internship Assignment

Python implementations of an **LRU Cache** and an **Event Scheduler**, with runnable examples.

## Project Files

| File | Description |
|---|---|
| `lru_cache.py` | Fixed-capacity cache with least recently used eviction |
| `event_scheduler.py` | Meeting overlap detection and minimum room calculation |

## Getting Started

**Requirements:** Python 3. No external packages are needed.

Clone the repository:

```bash
git clone https://github.com/RishiPramod/Avaloka-assignment.git
cd Avaloka-assignment
```

Run the examples:

```bash
python lru_cache.py
python event_scheduler.py
```

## Problem 1: LRU Cache

The cache uses a dictionary for key lookup and a doubly linked list to maintain usage order.

- `get(key)` returns the stored value and marks the entry as recently used. Returns `-1` if the key is missing.
- `put(key, value)` inserts or updates an entry. When inserting into a full cache, it evicts the least recently used entry.

A zero-capacity cache stores nothing. Negative capacity raises `ValueError`.

### Example Output

```text
10
-1
-1
100
40
```

The example demonstrates retrieving values, updating an existing entry, and evicting entries based on their usage order.

## Problem 2: Event Scheduler

The scheduler provides two functions:

- `can_attend_all(events)` checks whether one person can attend every meeting without overlaps.
- `min_rooms_required(events)` calculates the minimum number of rooms needed.

Events are sorted by start time. Room calculation uses a min-heap of active meeting end times.

Meetings that end exactly when another begins do not overlap. Each event must satisfy `start < end`; otherwise, the functions raise `ValueError`. The original input is not modified.

### Example Output

```text
Schedule 1: [(9, 10), (10, 11), (11, 12)]
Can attend all: True
Minimum rooms: 1

Schedule 2: [(9, 12), (10, 11), (11, 13)]
Can attend all: False
Minimum rooms: 2

Schedule 3: [(9, 11), (9, 11), (9, 11)]
Can attend all: False
Minimum rooms: 3

Schedule 4: []
Can attend all: True
Minimum rooms: 0
```

## Complexity

| Operation | Time | Space |
|---|---|---|
| LRU `get` | O(1) average | O(1) extra per call |
| LRU `put` | O(1) average/amortized | O(1) extra per call |
| `can_attend_all` | O(n log n) | O(n) extra |
| `min_rooms_required` | O(n log n) | O(n) extra |

The cache uses **O(C) total storage**, where `C` is its capacity. For the scheduler, `n` is the number of events.

## Design Notes

- **LRU trade-off:** Fast lookup and recency updates require additional list pointers and consistency between the dictionary and list.
- **Room assignment extension:** Track `(end_time, room_id)` and reuse available room IDs to assign specific rooms.
- **Thread safety:** The current cache is single-threaded. Protecting complete `get` and `put` operations with a shared lock would make concurrent access safe.