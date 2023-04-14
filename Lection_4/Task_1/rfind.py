import argparse
import os

def find(path, string, occurrences):
	for entry in os.scandir(path):
		entryPath = os.path.join(path, entry.name)
		if entry.is_file() and string in entry.name:
			occurrences.append(entryPath)
		elif entry.is_dir():
			find(entryPath, string, occurrences)
	return occurrences

parser = argparse.ArgumentParser(description='Find files in a directory')
parser.add_argument('--folder', '-f', required=True, help='Folder to search in')
parser.add_argument('--file', '-n', required=True, help='Name or part of name of the file(s) to search for')
args = parser.parse_args()

occurrences = find(args.folder, args.file, [])

for occurrence in occurrences:
	print(os.path.relpath(occurrence, args.folder))
