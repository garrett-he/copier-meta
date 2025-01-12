import random

from chance import chance

LICENSE_SPEC = {
    'Apache-2.0': {'stub': 'Apache License', 'with_holder': False, 'filename': 'LICENSE'},
    'BSD-3-Clause': {'stub': 'BSD 3-Clause License', 'with_holder': True, 'filename': 'LICENSE'},
    'GPL-3.0-or-later': {'stub': 'GNU General Public License', 'with_holder': False, 'filename': 'COPYING'},
    'LGPL-3.0-or-later': {'stub': 'GNU Lesser General Public License', 'with_holder': False, 'filename': 'COPYING'},
    'MIT': {'stub': 'MIT License', 'with_holder': True, 'filename': 'LICENSE'},
    'MPL-2.0': {'stub': 'Mozilla Public License', 'with_holder': False, 'filename': 'LICENSE'},
    'Unlicense': {'stub': 'This is free and unencumbered software released into the public domain', 'with_holder': False, 'filename': 'UNLICENSE'}
}


def generate_copier_answers() -> dict:
    return {
        'copyright_license': chance.pickone(list(LICENSE_SPEC.keys())),
        'copyright_holder_name': chance.name(),
        'copyright_holder_email': chance.email(),
        'copyright_year': str(random.randint(2000, 2024))
    }
