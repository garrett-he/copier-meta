"""Test fixtures and configuration."""

from __future__ import annotations

import pytest
from chance import chance


@pytest.fixture
def base_answers() -> dict[str, str]:
    """Return random template answers generated via chance."""
    holder = chance.name()
    return {
        'template_name': 'copier-test',
        'template_description': f'A test template by {holder}.',
        'vcs_github_path': f'{holder.lower().replace(" ", "-")}/copier-test',
        'copyright_holder_name': holder,
        'copyright_holder_email': chance.email(),
    }
