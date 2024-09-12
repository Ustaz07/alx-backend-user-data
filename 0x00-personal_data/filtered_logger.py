#!/usr/bin/env python3
"""
Module for filtering log data to obfuscate specified fields.
"""

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Returns the log message with specified fields obfuscated.

    Args:
        fields (List[str]): List of field names to obfuscate.
        redaction (str): The string to replace the field values with.
        message (str): The log message to be filtered.
        separator (str): The separator character used in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=([^;{separator}]*)"
    return re.sub(pattern, lambda x: f"{x.group(1)}={redaction}", message)
