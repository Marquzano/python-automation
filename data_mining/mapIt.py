#! /home/marquzano/workspace/data_mining/bin/python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()
try:
    webbrowser.open('https://www.google.com/maps/place/' + address)
except Exception as exc:
    print('Your request to map has failed due to the following error:\n' + exc)