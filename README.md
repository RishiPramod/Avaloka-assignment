# Avaloka Internship Assignment

Python solutions for two data structures and scheduling problems.

## Files

- `lru_cache.py`: LRU cache using a dictionary and doubly linked list.
- `event_scheduler.py`: Meeting overlap detection and minimum room calculation.

## Requirements

Python 3. No external dependencies.

## Run

python lru_cache.py
python event_scheduler.py

## Expected Results

The LRU cache example prints:
10, -1, -1, 100, 40, each on a separate line.

The scheduler examples return:
- Back-to-back meetings: True, 1 room.
- Partially overlapping meetings: False, 2 rooms.
- Three simultaneous meetings: False, 3 rooms.
- Empty schedule: True, 0 rooms.

## Complexity

- LRU get and put: O(1) average time; O(C) total cache storage.
- Scheduler functions: O(n log n) time and O(n) extra space.

C is the cache capacity, and n is the number of events.