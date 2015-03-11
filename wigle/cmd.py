from . import Wigle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--user', dest='user', type=str, required=True, help='Wigle username')
parser.add_argument('--pass', dest='password', type=str, required=True, help='Wigle password')


def user_info():
    parser.description = 'Get Wigle account information'
    args = parser.parse_args()

    info = Wigle(args.user, args.password).get_user_info()
    if not info.get('success'):
        print('Unauthorized to get user info')
    else:
        print('User: %s' % info.get('userid', '<unknown>'))
        print('Donate data: %s' % info.get('donate', '<unknown>'))
        print('Joined on: %s' % info.get('joindate', '<unknown>'))
        print('Last logged in on: %s' % info.get('lastlogin', '<unknown>'))


def search():
    parser.description = 'Get Wigle account information'
    parser.add_argument('--ssid', dest='ssid', type=str,
                        help='SSID of the network')
    parser.add_argument('--bssid', dest='bssid', type=str,
                        help='BSSID of the network')
    parser.add_argument('--max', dest='max', type=int, default=20,
                        help='maximum number of networks to download')
    args = parser.parse_args()

    def notify_new_page(first):
        print("Downloading new page (records from %i)" % first)

    results = Wigle(args.user, args.password).search(
        ssid=args.ssid,
        bssid=args.bssid,
        on_new_page=notify_new_page,
        max_results=args.max)

    for result in results:
        print("%(ssid)s, %(netid)s, %(trilat)s, %(trilong)s" % result)
