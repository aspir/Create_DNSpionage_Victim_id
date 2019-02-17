import socket
import argparse
import getpass
import sys


DEFAULT_ID = "Fy"
DEV = 0x3a


def get_char(xor_result):
    temp = (xor_result % DEV) + ord('A')
    if ord('Z') < temp < ord('a'):
        temp += 8
    return chr(temp)


def get_xor_result(s):
    s_xor_result = 0
    for letter in s:
        s_xor_result = s_xor_result ^ ord(letter)
    return s_xor_result


def generate_id(username, hostname):
    username_xor_result = get_xor_result(username)
    hostname_xor_result = get_xor_result(hostname)
    if hostname_xor_result == 0 or username_xor_result == 0:
        return DEFAULT_ID
    return "{0}{1}".format(get_char(username_xor_result),
                           get_char(hostname_xor_result))


def main():
    parser = argparse.ArgumentParser(description="Victim ID generator based on username and hostname")
    parser.add_argument("--username", dest='username', help="the username", default=getpass.getuser())
    parser.add_argument("--hostname", dest='hostname', help="the computer hostname", default=socket.gethostname())
    args = parser.parse_args(sys.argv[1:])
    print(generate_id(args.username, args.hostname))


if __name__ == "__main__":
    main()
