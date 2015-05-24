#!/usr/bin/env python

import argparse
import codecs
import markdown
import mdrender
import notekit_html
import settings
import sys
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--publish', '-pub', help='Publishe your note')
parser.add_argument('--preview', '-pre', help='Shows your renderd note')
args = parser.parse_args()

def publish(args):
    def scp(source, server, path = settings.remote_note_path):
    	return not subprocess.Popen(["scp", source, "%s:%s" % (server, path)]).wait()
    	filename = "example-note"
    	server = settings.server
    
    	if scp(filename, server):
    		print("File uploaded successfully.")
    		return 0
    	else:
    		print("File upload failed.")
    		return 1

def preview(args):
    md_note = "/tmp/tmp/test-note.md"
    html_note = "/tmp/tmp/RENDERD_TEST_NOTE.html"
    
    input_file = codecs.open(
            md_note,
            mode="r",
            encoding="utf-8"
            )
    
    text = input_file.read()
    
    html = markdown.markdown(text)
    
    output_file = codecs.open(
            html_note,
            "w",
            encoding="utf-8",
            errors="xmlcharrefreplace"
            )
    
    output_file.write(notekit_html.HEADER + html + notekit_html.FOOTER)

