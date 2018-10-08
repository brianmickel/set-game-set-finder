import sys
from set_check import set_check

def main():
    script = sys.argv[0]
    filename = sys.argv[1]

    with open(filename) as f:
        cards_list = f.read().splitlines()

    results = set_check(cards_list)
    sets_found = results['setList']

    if results['setExistance']:
        print("Set(s) Found")
    else:
        print("No Sets Found")

if __name__ == '__main__':
   main()
