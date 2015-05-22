#!/usr/bin/env python

import mdrender
import settings
import sys
import subprocess

def scp(source, server, path = settings.remote_note_path):
	return not subprocess.Popen(["scp", source, "%s:%s" % (server, path)]).wait()

def main(*args):
	filename = "example-note"
	server = settings.server

	if scp(filename, server):
		print("File uploaded successfully.")
		return 0
	else:
		print("File upload failed.")
		return 1


if __name__ == "__main__": sys.exit(main(*sys.argv[1:]))
