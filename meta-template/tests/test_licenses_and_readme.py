from .utils import LICENSE_SPEC, generate_copier_answers


def test_licenses_and_readme(copie):
    for license_id, license_spec in LICENSE_SPEC.items():
        answers = generate_copier_answers()
        answers['copyright_license'] = license_id

        result = copie.copy(extra_answers=answers)

        if result.exception:
            raise result.exception

        license_file = license_spec['filename']
        license_text = result.project_dir.joinpath(license_file).read_text(encoding='utf-8')
        assert license_spec['stub'] in license_text

        if license_spec['with_holder']:
            assert f'{answers["copyright_holder_name"]} <{answers["copyright_holder_email"]}>' in license_text
            assert answers['copyright_year'] in license_text

        assert result.project_dir.joinpath(license_file).exists()

        assert license_file in result.project_dir.joinpath('.editorconfig').read_text(encoding='utf-8')

        readme = result.project_dir.joinpath('README.md').read_text()

        assert answers['project_name'] in readme
        assert answers['project_description'] in readme

        assert license_spec['stub'] in readme

        if license_id == 'Unlicense':
            assert 'This is free and unencumbered software released into the public domain' in readme
        else:
            assert f'Copyright (C) {answers["copyright_year"]} {answers["copyright_holder_name"]} <{answers["copyright_holder_email"]}>' in readme
            assert f'see [{license_file}](./{license_file}).' in readme
