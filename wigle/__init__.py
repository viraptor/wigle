import requests

WIGLE_ENDPOINT = 'https://wigle.net/api/v1'

# How many entries will be sent from the server at one time. This is hardcoded
# on the website.
WIGLE_PAGESIZE = 100


class WigleAuthenticationError(Exception):
    pass


class Wigle(object):
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self._auth_cookies = None

    def _wigle_request(self, method, auth=False, **kwargs):
        url = WIGLE_ENDPOINT + '/' + method
        if auth:
            cookies = self._auth_cookies
        else:
            cookies = None
        headers = {
            'Accept': 'application/json, text/javascript',
            'User-Agent': 'python wigle client',
            'Content-Type': 'application/json',
            }
        return requests.post(url, cookies=cookies, headers=headers, **kwargs)

    def _authenticated_request(self, method, **kwargs):
        self._ensure_authenticated()
        return self._wigle_request(method, auth=True, **kwargs)

    def _unauthenticated_request(self, method, **kwargs):
        return self._wigle_request(method, auth=False, **kwargs)

    def reauthenticate(self):
        self._auth_cookies = None
        auth_data = {
            'credential_0': self.user,
            'credential_1': self.password,
            'noexpire': 'off',
            'destination': '/',
        }
        resp = self._unauthenticated_request('jsonLogin', params=auth_data, allow_redirects=False)
        if 'auth' in resp.cookies:
            self._auth_cookies = resp.cookies
        else:
            raise WigleAuthenticationError('Could not authenticate as user %s' % self.user)

    def _ensure_authenticated(self):
        if not self._auth_cookies:
            self.reauthenticate()

    def get_user_info(self):
        resp = self._authenticated_request('jsonUser')
        info = resp.json()
        return info

    def search(self, lat_range=None, long_range=None, variance=None,
               bssid=None, ssid=None,
               last_update=None,
               address=None, state=None, zipcode=None,
               on_new_page=None):
        params = {
            'latrange1': lat_range[0] if lat_range else "",
            'latrange2': lat_range[1] if lat_range else "",
            'longrange1': long_range[0] if long_range else "",
            'longrange2': long_range[1] if long_range else "",
            'variance': str(variance) or "0.01",
            'netid': bssid or "",
            'ssid': ssid or "",
            'lastupdt': last_update.strftime("%Y%m%d%H%M%S") if last_update else "",
            'addresscode': address or "",
            'statecode': state or "",
            'zipcode': zipcode or "",
            'Query': "Query",
        }

        wifis = []
        while True:
            if on_new_page:
                on_new_page(params.get('first', 1))
            resp = self._authenticated_request('jsonSearch', params=params)
            data = resp.json()
            if not data['success']:
                break

            for result in data['results']:
                wifis.append(result)

            if data['resultCount'] < WIGLE_PAGESIZE:
                break

            params['first'] = data['last'] + 1

        return wifis
