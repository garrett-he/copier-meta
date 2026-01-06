"""Integration tests for generated template project."""

from __future__ import annotations

import subprocess
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_generated_template_structure(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that generated template has expected structure."""
    answers = {**base_answers, 'copyright_license': 'MIT'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    project = result.project_dir
    assert (project / 'copier.yml').exists()
    assert (project / 'copier' / 'settings.yml').exists()
    assert (project / 'tests' / 'test_static.py').exists()
    assert (project / 'template' / '.editorconfig').exists()
    assert (project / 'template' / '.gitattributes').exists()
    assert (project / 'template' / '.gitignore').exists()
    assert (project / 'template' / 'CHANGELOG.md').exists()


def test_generated_template_tests_pass(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that the generated template's own tests pass."""
    answers = {**base_answers, 'copyright_license': 'MIT'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    project = result.project_dir
    proc = subprocess.run(
        ['uv', 'run', 'pytest', 'tests/', '--template', '.', '-q'],
        cwd=project,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, f'Generated template tests failed:\n{proc.stdout}\n{proc.stderr}'
