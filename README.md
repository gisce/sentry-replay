# sentry-irc
A plugin for [Sentry](https://www.getsentry.com/) that re-send errors to another sentry server.
## Installation
`$ pip install sentry-replay`

Add `sentry_replay` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    #...
    'sentry',
    'sentry_replay',
)
```
