import subprocess
from datetime import date

from copier_template_extensions import ContextHook


class ContextUpdater(ContextHook):
    def hook(self, context):
        self.set_git_values(context)
        self.set_date_values(context)

    def set_git_values(self, context):
        context['git_user_name'] = subprocess.getoutput('git config user.name').strip()
        context['git_user_email'] = subprocess.getoutput('git config user.email').strip()

    def set_date_values(self, context):
        today = date.today()
        context['current_year'] = today.year
        context['current_month'] = today.month
        context['current_day'] = today.day
