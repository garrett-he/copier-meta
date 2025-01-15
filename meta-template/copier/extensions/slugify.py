import re
import unicodedata

from jinja2.ext import Extension, Environment


def slugify_filter(value: str, separator: str = '-') -> str:
    value = unicodedata.normalize('NFKD', str(value)).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-_\s]+', separator, value).strip('-_')


class SlugifyExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)

        environment.filters['slugify'] = slugify_filter
