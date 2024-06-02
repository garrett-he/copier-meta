# pylint: disable=abstract-method
import re
import subprocess
import unicodedata
from datetime import date

from jinja2.ext import Extension, Environment


def slugify_filter(value: str, separator: str = '-') -> str:
    value = unicodedata.normalize('NFKD', str(value)).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-_\s]+', separator, value).strip('-_')


class DateExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)

        today = date.today()
        environment.globals['current_year'] = today.year
        environment.globals['current_month'] = today.month
        environment.globals['current_day'] = today.day


class GitExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)

        environment.globals['git_user_name'] = subprocess.getoutput('git config user.name').strip()
        environment.globals['git_user_email'] = subprocess.getoutput('git config user.email').strip()


class SlugifyExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)

        environment.filters['slugify'] = slugify_filter
