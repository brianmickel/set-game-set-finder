import sys
from set_check import set_check

def main():
    script = sys.argv[0]
    cards_filename = sys.argv[1]

    with open(cards_filename) as f:
        cards_list = f.read().splitlines()
    # cards_list = ['ps3l','pd2e','po2e',
    #         'ro3s','rd2s','ps1l'
    #         'gd1e','po2s','gs1e'
    #         'ro1e','ps3e','rs3s']

    results = set_check(cards_list)
    sets_found = results['setList']

    if results['setExistance']:
        print("Set(s) Found")
    else:
        print("No Sets Found")

if __name__ == '__main__':
   main()

# TODO Add testing (turn the comments into tests)
# TODO clean up comments in code