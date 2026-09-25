.PHONY: test release backup restore-check

test:
	python -m pytest -q

release:
	./scripts/release.sh

backup:
	python backup.py

restore-check:
	python backup.py --restore-to /tmp/restore-check && python -m pytest -q tests/test_restored.py
