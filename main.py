# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kg_ht import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dt = DirAccTable(35)
    dt.insert(1, "shware")
    dt.search(1)
    dt.delete(1)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
