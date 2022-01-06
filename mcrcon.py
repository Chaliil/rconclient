from rcon import Client, exceptions
import argparse
import getpass

parser = argparse.ArgumentParser(description='Use rcon in your command line')

parser.add_argument('server', help='specify server to connect to',nargs='+', type=str)
parser.add_argument('-p', '--port', help='specify port to connect to (default is 25575)', default='25575', type=int, required=False)

args = parser.parse_args()


while True:
    try:
        password = getpass.getpass(prompt='Please enter the password for rcon: ')
        with Client(args.server, args.p, passwd=password) as client:
            while True:
                command = input('> ' )

                if command == 'exit':
                    break
                
                response = client.run(command)
                print(response)

        break
    except KeyboardInterrupt as e:
        print()
        break
    except exceptions.WrongPassword:
        print('wrong password, please try again')

print('rcon session closed')