import os

from .utils import generate_copier_answers


def test_template_generation(copie):
    answers = generate_copier_answers()
    result = copie.copy(extra_answers=answers)

    if result.exception:
        raise result.exception

    cwd = os.getcwd()

    os.chdir(result.project_dir)
    os.system('uv sync')

    assert os.system('uv run pytest') == 0

    os.chdir(cwd)
