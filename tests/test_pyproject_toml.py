import toml
from pytest_copie.plugin import Copie
from .utils import generate_copier_answers


def test_pyproject_toml(copie: Copie):
    answers = generate_copier_answers()
    result = copie.copy(extra_answers=answers)

    if result.exception:
        raise result.exception

    assert result.project_dir.joinpath('pyproject.toml').is_file()

    with open(result.project_dir.joinpath('pyproject.toml'), 'r', encoding='utf-8') as fp:
        pyproject = toml.loads(fp.read())

    assert pyproject['project']['name'] == answers['template_name']
    assert pyproject['project']['version'] == answers['template_version']
    assert pyproject['project']['description'] == answers['template_description']
    assert pyproject['project']['authors'][0]['name'] == answers['copyright_holder_name']
    assert pyproject['project']['authors'][0]['email'] == answers['copyright_holder_email']
    assert pyproject['project']['license']['text'] == answers['copyright_license']
    assert pyproject['project']['keywords'] == answers['template_keywords'].split(',')

    assert pyproject['project']['urls']['homepage'] == f"https://github.com/{answers['vcs_github_path']}"
    assert pyproject['project']['urls']['repository'] == f"https://github.com/{answers['vcs_github_path']}.git"
    assert pyproject['project']['urls']['changelog'] == f"https://github.com/{answers['vcs_github_path']}/blob/main/CHANGELOG.md"
