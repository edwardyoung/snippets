import os
import sys

def print_usage():
    print "Usage: renamer.py <path>"
    sys.exit(1)

# Make sure the user passes and argument
if len(sys.argv) < 2:
    print_usage()

directory = sys.argv[1]
if os.path.isdir(directory):
    print "This app will rename files in " + directory + " to lower case"
    print "if the filename contains any capital letters and does not"
    print "end in .tar\n"

    # Get only files in directory that have a capital letter and
    # does not have a .tar extension
    files = [f for f in os.listdir(directory)
             if os.path.isfile(os.path.join(directory, f)) and
             any(l.isupper() for l in f) and
             not f.endswith(".tar")]

    # Rename to lower case
    [os.rename(os.path.join(directory, f), os.path.join(directory, f.lower()))
     for f in files]

    print "Only renamed these files in " + directory
    print files
    print "\nDone!"
else:
    print_usage()
