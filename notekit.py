#!/usr/bin/env python

import argparse
import codecs
import markdown
import mdrender
import notekit_html
import settings
import sys
import subprocess


def publish(*args, **kwargs):
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

    md_note = "/tmp/tmp/test-note.md"
def show(*args, **kwargs):
    html_note = "/tmp/tmp/RENDERD_TEST_NOTE.html"
    
    input_file = codecs.open(md_note, mode="r", encoding="utf-8")
    
    note = markdown.markdown(input_file.read())
    
    output_file = codecs.open(html_note, "w", encoding="utf-8", errors="xmlcharrefreplace")
    
    output_file.write(notekit_html.HEADER + html + notekit_html.FOOTER)


parser = argparse.ArgumentParser()

parser.add_argument('--publish', '-p', action='store_true', help='Publishe your note')
parser.add_argument('--show', '-s',  action='store_true', help='Shows you a preview of your renderd note')
parser.add_argument('note', nargs='+')

parsed_args = parser.parse_args()
if parsed_args.action is None:
    parser.parse_args(['-h'])
parsed_args.action(parsed_args)
if parsed_args.publish:
    publish(parsed_args)
elif parsed_args.show:
    show(parsed_args)
    note = ''.join(parsed_args.note)
