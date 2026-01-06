"""Test fixtures and configuration."""

from __future__ import annotations

import pytest
from chance import chance


@pytest.fixture
def base_answers() -> dict[str, str]:
    """Return random project answers generated via chance."""
    holder = chance.name()
    return {
        'copyright_holder_name': holder,
        'copyright_holder_email': chance.email(),
    }
