# Wigle

Python interface to wigle APIs. This project is unofficial and may stop working
due to API changes at any point without warning.

Currently supported operations: authentication, search and user information

#Search

Search supports all the options available via web interface. For example to
search for APs advertising network "foobar", use:

    wigle = Wigle('username', 'password')
    wigle.search(ssid="foobar")

Paging happens behind the scenes and will pull all results in multiple requests
when necessary.

See docstrings for more details.
