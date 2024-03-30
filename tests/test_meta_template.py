from pytest_copie.plugin import Copie


def test_meta_template_static_files(copie: Copie):
    result = copie.copy()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()

    assert result.project_dir.joinpath('.editorconfig').exists()
