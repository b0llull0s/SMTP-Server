# SMTP-Server
- Just a simple SMTP server implementation using the `aiosmtpd` library for `Python 3.6` or higher.
## Configuration
- The server listens on 0.0.0.0 by default, meaning it accepts connections from all network interfaces.
- The default port is 25, which is the standard port for SMTP.
## Example Output
- When an email is received, the server will print:
```
---------- MESSAGE FOLLOWS ----------
From: sender@example.com
To: recipient@example.com
Subject: Test Email

This is a test email message.
------------ END MESSAGE ------------
```
