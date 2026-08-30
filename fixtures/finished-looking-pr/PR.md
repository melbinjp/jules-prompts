# Fix password reset emails

This change restores password reset delivery. The email template now includes
the reset token, tests cover the template, and the mailer is used.

Closes the issue.
