# Incident 2026-10-02: duplicate charges

- 09:02 2.14 released.
- 09:19 duplicate_charge alert fired. On-call agent retried the timed-out charges.
- 09:20 to 11:40 investigated the payment client and the provider's dashboard in production.
- 10:20 alert disabled (noisy).
- 11:40 hotfix 2.14.1 deployed.
- 11:45 invoice PDFs failing.
- 12:52 2.14.2 fixed the invoices.
- 13:05 status page updated.
- 15:10 refunds issued. Resolved.
