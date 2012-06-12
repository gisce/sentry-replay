"""
sentry_replay.models
~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by Eduard Carreras, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django import forms
import sentry_replay
from sentry.plugins import Plugin
from raven import Client


class ReplayOptionsForm(forms.Form):
    sentry_dsn = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'span9'})
    )


class Replay(Plugin):

    title = 'Replay'
    slug = 'replay'
    conf_title = 'Replay'
    conf_key = 'replay'
    version = sentry_replay.VERSION
    project_conf_form = ReplayOptionsForm

    author = 'Eduard Carreras'
    author_url = 'http://code.gisce.net/sentry-replay'

    def is_configured(self, project):
        return all((self.get_option(k, project)
                   for k in ('sentry_dsn',)))

    def post_process(self, group, event, is_new, is_sample, **kwargs):
        sentry_dsn = self.get_option('sentry_dsn', event.project)
        client = Client(dsn=sentry_dsn)
        data = event.as_dict()
        del data['id']
        data['message'] = event.message
        data = client.encode(data)
        client.send_encoded(message=data)
