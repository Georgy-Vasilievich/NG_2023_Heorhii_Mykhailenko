import argparse
import os

parser = argparse.ArgumentParser(description='Find files in a directory')
parser.add_argument('--folder', '-f', required=True, help='Folder to search in')
parser.add_argument('--file', '-n', required=True, help='Name or part of name of the file(s) to search for')
args = parser.parse_args()

for dirpath, dirnames, filenames in os.walk(args.folder):
    for filename in filenames:
        if args.file in filename:
            print(os.path.join(dirpath, filename)[len(args.folder)+1:])
