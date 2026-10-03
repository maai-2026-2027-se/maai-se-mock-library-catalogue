# Library Catalogue

Search a small book collection, borrow books, and prepare lending reports.

This is a three-round team exercise. Start with [the student guide](CONTRIBUTING.md), then read your assigned card in [TASKS.md](TASKS.md). Your instructor supplies the author/reviewer schedule.

## Run it

Use Python 3.11 or later. No third-party packages are required.

```sh
python3 app.py
python3 check.py
```

The demo prints sample records and the existing `catalogue_size` result. Extend the Python functions according to the task cards. The starter has intentionally missing features and round-two bugs; baseline checks pass but final acceptance fails until the team finishes.

## Data model

Each book is a dictionary with `title` (unique nonempty string), `author` (nonempty string), `year` (positive integer), and `available` (boolean). Assume well-formed records. Functions must not mutate their inputs; borrowing returns a new list of new dictionaries.

## Test a task

```sh
python3 check.py --task L1
# After implementation and a meaningful student test:
python3 check.py --complete L1
```

Commit `completed/L1.txt` with your code and test. Normal CI checks the baseline, every completed task, and student tests. Do not edit the supplied acceptance tests, runner, task manifest, or workflow.

After all rounds, run `python3 check.py --all` on current `main`. All nine tasks must pass, all nine markers must exist, and the shared release-note line must contain L7, L8 and L9. The final team pass plus individual implementation/review evidence is required for the bonus.
