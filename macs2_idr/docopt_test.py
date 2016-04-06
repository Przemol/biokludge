"""Naval Fate.

Usage:
  docopt_test.py <treatment1> <treatment2> [-c <input>]
  docopt_test.py  (-h | --help)
  docopt_test.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  -c <input>, --control <input>   Control file. [default: test].


"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    print(arguments)
    
    print(arguments["<treatment1>"])
