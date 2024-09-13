#!/usr/bin/env python3
"""Log formatter for redacting sensitive information in log messages."""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Obfuscates sensitive information in the message based on the provided fields.

    Args:
        fields (List[str]): List of strings representing the fields to be redacted.
        redaction (str): The string that will replace the sensitive information.
        message (str): The log message containing sensitive data.
        separator (str): The character separating the fields in the log message.

    Returns:
        str: The log message with sensitive information redacted.
    """
    for field in fields:
        message = re.sub(
            rf'{field}=[^{separator}]*',
            f'{field}={redaction}',
            message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class that obfuscates sensitive fields in log messages."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to be redacted.

        Args:
            fields (List[str]): List of fields that should be redacted in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters sensitive information from the log record.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted and redacted log record.
        """
        record.msg = filter_datum(
            self.fields,
            self.REDACTION,
            record.getMessage(),
            self.SEPARATOR
        )
        return super().format(record)
