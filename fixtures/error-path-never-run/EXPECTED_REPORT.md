# Expected report for error-path-never-run

- bare-except: `except Exception` in fetch.py returns `{"id": 0, "name": "guest"}` for every failure. Pointing urlopen at a closed port, a 404, or a garbage URL all produce the same guest.
- untested-failure: tests/test_fetch.py only patches a successful urlopen. The guest branch has never executed.

defect_id: bare-except
defect_id: untested-failure
