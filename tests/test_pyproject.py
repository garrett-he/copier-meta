"""Integration tests for pyproject.toml generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_pyproject_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that pyproject.toml is generated."""
    answers = {**base_answers, 'copyright_license': 'MIT'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    assert pyproject.exists()
    content = pyproject.read_text()
    assert '[project]' in content
    assert '[tool.ruff]' in content


def test_pyproject_template_name(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test project name matches template_name."""
    answers = {**base_answers, 'copyright_license': 'MIT', 'template_name': 'copier-my-template'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'name = "copier-my-template"' in content


def test_pyproject_template_version(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test project version matches template_version."""
    answers = {**base_answers, 'copyright_license': 'MIT', 'template_version': '2.0.0'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'version = "2.0.0"' in content


def test_pyproject_template_version_default(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test project version uses default 0.1.0."""
    answers = {**base_answers, 'copyright_license': 'MIT'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'version = "0.1.0"' in content


def test_pyproject_template_description(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test project description matches template_description."""
    answers = {
        **base_answers,
        'copyright_license': 'MIT',
        'template_description': 'A template for building REST APIs.',
    }
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'description = "A template for building REST APIs."' in content


def test_pyproject_keywords(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test keywords are split and rendered correctly."""
    answers = {**base_answers, 'copyright_license': 'MIT', 'template_keywords': 'fastapi,rest,openapi'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'keywords = [ "fastapi", "rest", "openapi" ]' in content


def test_pyproject_keywords_default(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test default keywords are used."""
    answers = {**base_answers, 'copyright_license': 'MIT'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'keywords = [ "copier", "template", "code-generation" ]' in content


def test_pyproject_license(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test license matches copyright_license."""
    answers = {**base_answers, 'copyright_license': 'Apache-2.0'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'license = { text = "Apache-2.0" }' in content


def test_pyproject_maintainers(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test maintainers use copyright holder info."""
    answers = {
        **base_answers,
        'copyright_license': 'MIT',
        'copyright_holder_name': 'Alice',
        'copyright_holder_email': 'alice@example.com',
    }
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'name = "Alice"' in content
    assert 'email = "alice@example.com"' in content


def test_pyproject_authors(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test authors use copyright holder info."""
    answers = {
        **base_answers,
        'copyright_license': 'MIT',
        'copyright_holder_name': 'Bob',
        'copyright_holder_email': 'bob@example.com',
    }
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'name = "Bob"' in content
    assert 'email = "bob@example.com"' in content


def test_pyproject_urls(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test URLs use vcs_github_path."""
    answers = {**base_answers, 'copyright_license': 'MIT', 'vcs_github_path': 'my-org/my-repo', 'with_changelog': True}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'urls.Homepage = "https://github.com/my-org/my-repo"' in content
    assert 'urls.Issues = "https://github.com/my-org/my-repo/issues"' in content
    assert 'urls.Repository = "https://github.com/my-org/my-repo.git"' in content
    assert 'urls.Changelog = "https://github.com/my-org/my-repo/blob/main/CHANGELOG.md"' in content
    assert 'urls.Documentation = "https://github.com/my-org/my-repo/blob/main/README.md"' in content


def test_pyproject_changelog_url_when_enabled(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test urls.Changelog is present when with_changelog is True."""
    answers = {**base_answers, 'copyright_license': 'MIT', 'with_changelog': True}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'urls.Changelog' in content
    assert f'github.com/{answers["vcs_github_path"]}/blob/main/CHANGELOG.md' in content


def test_pyproject_changelog_url_when_disabled(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test urls.Changelog is absent when with_changelog is False."""
    answers = {**base_answers, 'copyright_license': 'MIT', 'with_changelog': False}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'urls.Changelog' not in content


def test_pyproject_tool_sections(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test tool configuration sections are present."""
    answers = {**base_answers, 'copyright_license': 'MIT'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert '[tool.ruff]' in content
    assert '[tool.pyproject-fmt]' in content
    assert '[tool.pyrefly]' in content
    assert '[tool.rumdl]' in content
    assert 'line-length = 120' in content


def test_pyproject_python_requires(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test requires-python is set."""
    answers = {**base_answers, 'copyright_license': 'MIT'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pyproject = result.project_dir / 'pyproject.toml'
    content = pyproject.read_text()
    assert 'requires-python = ">=3.12"' in content
