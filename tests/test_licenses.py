from .utils import LICENSE_SPEC, generate_copier_answers


def test_licenses(copie):
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
