import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('server', required=True)
    parser.add_argument('port', metavar='N', type=int, help='revisions', required=False)
    res = parser.parse_args()

print(res)