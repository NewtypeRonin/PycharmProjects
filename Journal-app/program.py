import journal
# from journal import load, save takes only save and load from journal
# from journal import * takes all methods from journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print("--------------------------------")
    print(" This is the Journal App")
    print("--------------------------------")

def run_event_loop():

    print('What would you like to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    #journal_data = [] #defines list() of items
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            print('List selected')
            list_entries(journal_data)
        elif cmd == 'a':
            print('Add selected')
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("We don't understand '{}'. Please enter L, A or x".format(cmd))

    print('Done, goodbye!')
    journal.save(journal_name, journal_data)

def list_entries(data):
    print("Your Journal Entries: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx+1, entry))

def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)
    # data.append(text) this works directly with the data, kinda messy

print("__file__ " + __file__)
print("__name__ " + __name__)

if __name__ == '__main__':
    main()
