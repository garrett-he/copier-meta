import random

from chance import chance
from pytest_copie.plugin import Copie

LICENSE_SPEC = {
    'Apache-2.0': {'filename': 'LICENSE', 'stub': 'Apache License', 'with_holder': False},
    'BSD-3-Clause': {'filename': 'LICENSE', 'stub': 'BSD 3-Clause License', 'with_holder': True},
    'GPL-3.0-or-later': {'filename': 'COPYING', 'stub': 'GNU General Public License', 'with_holder': False},
    'LGPL-3.0-or-later': {'filename': 'COPYING', 'stub': 'GNU Lesser General Public License', 'with_holder': False},
    'MIT': {'filename': 'LICENSE', 'stub': 'MIT License', 'with_holder': True},
    'MPL-2.0': {'filename': 'LICENSE', 'stub': 'Mozilla Public License', 'with_holder': False},
    'Unlicense': {'filename': 'UNLICENSE', 'stub': 'This is free and unencumbered software released into the public domain', 'with_holder': False}
}


def generate_copier_answers():
    return {
        'copyright_license': chance.pickone(list(LICENSE_SPEC.keys())),
        'copyright_holder_name': chance.name(),
        'copyright_holder_email': chance.email(),
        'copyright_year': str(random.randint(2000, 2024)),
    }


def test_meta_template_static_files(copie: Copie):
    result = copie.copy()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()

    assert result.project_dir.joinpath('.editorconfig').exists()


def test_meta_template_licenses(copie: Copie):
    for license_id, license_spec in LICENSE_SPEC.items():
        answers = generate_copier_answers()
        answers['copyright_license'] = license_id

        result = copie.copy(extra_answers=answers)

        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_dir.is_dir()

        license_text = result.project_dir.joinpath(license_spec['filename']).read_text(encoding='utf-8')
        assert license_spec['stub'] in license_text

        if license_spec['with_holder']:
            assert f'{answers["copyright_holder_name"]} <{answers["copyright_holder_email"]}>' in license_text
            assert answers['copyright_year'] in license_text

        match license_id:
            case 'GPL-3.0-or-later' | 'LGPL-3.0-or-later':
                assert result.project_dir.joinpath('COPYING').exists()
                assert not result.project_dir.joinpath('LICENSE').exists()
                assert not result.project_dir.joinpath('UNLICENSE').exists()
            case 'Unlicense':
                assert not result.project_dir.joinpath('COPYING').exists()
                assert not result.project_dir.joinpath('LICENSE').exists()
                assert result.project_dir.joinpath('UNLICENSE').exists()
            case _:
                assert not result.project_dir.joinpath('COPYING').exists()
                assert result.project_dir.joinpath('LICENSE').exists()
                assert not result.project_dir.joinpath('UNLICENSE').exists()
