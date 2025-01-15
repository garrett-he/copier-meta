from jinja2.ext import Extension, Environment


def license_file(value: str) -> str:
    if 'GPL' in value.upper():
        return 'COPYING'

    if 'UNLICENSE' in value.upper():
        return 'UNLICENSE'

    return 'LICENSE'


class LicenseExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)

        environment.filters['license_file'] = license_file
