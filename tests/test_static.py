"""Integration tests for static file generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie

STATIC_FILES = [
    '.editorconfig',
    '.gitattributes',
    '.gitignore',
    '.pre-commit-config.yaml',
    'CHANGELOG.md',
    'justfile',
]


def test_static_files_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that all static files are generated."""
    answers = {**base_answers, 'copyright_license': 'MIT'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    for filename in STATIC_FILES:
        filepath = result.project_dir / filename
        assert filepath.exists(), f'Static file {filename} not found'
