# Fixture: silent-backup

Skill: `automate-a-workflow`. Prompt: `task_automate_a_workflow`.

Every evening someone at the Harbour Lane surgery backed up the appointments database by hand,
following `RUNBOOK.md`. An agent automated it: `scripts/backup.sh`, run by `cron.txt`. The last
three nights of its log are in `logs/backup.log`.

Six things about the automation mean it reports a backup every night whether or not one exists,
and one interrupted run would leave the surgery with none.

The schedule (`cron.txt`) is right: daily at 02:30, the quiet hour the runbook names, as the
person running it by hand did. It is the control.

```bash
python scripts/score_fixture.py fixtures/silent-backup REPORT.md
python scripts/score_fixture.py fixtures/silent-backup --self-check
```
