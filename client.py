# Anonymous FTP login
from ftplib import FTP
from os import environ


def main():
    with FTP() as ftp:
        addr = environ['SOURCE_ADDRESS']
        port = int(environ['SOURCE_ADDRESS_PORT'])

        ftp.connect('localhost', 2121, source_address=(addr, port))
        print(ftp.getwelcome())


if __name__ == '__main__':
    main()
