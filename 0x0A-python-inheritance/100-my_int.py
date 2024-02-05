#!/usr/bin/python3
"""Defines a rebel class MyInt that inherits from int."""


class MyInt(int):
    """Represents a rebellious integer."""

    def __eq__(self, other):
        """Override the equality operator."""
        # Invert the behavior of the equality operator
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator."""
        # Invert the behavior of the inequality operator
        return super().__eq__(other)
