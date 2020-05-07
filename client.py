# Anonymous FTP login
from ftplib import FTP
from os import environ


def main():
    with FTP() as ftp:
        host_addr = environ['HOST_ADDRESS']
        host_port = int(environ['HOST_PORT'])

        source_addr = environ['SOURCE_ADDRESS']
        source_port = int(environ['SOURCE_ADDRESS_PORT'])

        ftp.connect(host_addr, host_port, source_address=(source_addr, source_port))
        print(ftp.getwelcome())


if __name__ == '__main__':
    main()
