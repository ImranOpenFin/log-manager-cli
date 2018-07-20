## Configuration class
## Update parameters using command line args

from ConfigParser import SafeConfigParser

class Config(object):
    def __init__(self):
        parser = SafeConfigParser({'OPENFIN-API-KEY': '',
                                   'BASE-URL': '',
                                   'PRIVATE-KEY-FILE': ''})
        parser.read('config.ini')

        self._api_key = parser.get('DEFAULT', 'OPENFIN-API-KEY')
        self._base_url = parser.get('DEFAULT', 'BASE-URL')
        self._headers = {"X-Openfin-Api-Key": self.api_key}
        self._private_key = parser.get('DEFAULT', 'PRIVATE-KEY-FILE')

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, kv_pair):
        if not isinstance(kv_pair, tuple) or len(kv_pair) != 2:
            return

        key = kv_pair[0]
        value = kv_pair[1]
        if key in self._headers:
            del self._headers[key]
        self._headers[key] = value

    @property
    def private_key(self):
        return self._private_key

    @private_key.setter
    def private_key(self, value):
        self._private_key = value
