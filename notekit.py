#!/usr/bin/env python

import argparse
import codecs
import markdown
import notekit_html
import settings
import sys
import subprocess


def render(parsed_args):
    md_note = ''.join(parsed_args.note)
    html_note = settings.preview + ''.join(parsed_args.title) + ".html"
    
    input_file = codecs.open(md_note, mode="r", encoding="utf-8")
  
    note = markdown.markdown(input_file.read())
    
    output_file = codecs.open(html_note, "w", encoding="utf-8", errors="xmlcharrefreplace")
    
    output_file.write(notekit_html.HEADER + note + notekit_html.FOOTER)
   
    return html_note


def show(parsed_args):
    print("Open " + render(parsed_args) + " in your browser for a preview of your note")
    
    ##only works on Mac OS X
    subprocess.Popen(['open', render(parsed_args)])

 
def publish(parsed_args):
    
    filename = render(parsed_args) 
    server = settings.server

    def scp(source, server, path = settings.remote_note_path):
        return not subprocess.Popen(["scp", source, "%s:%s" % (server, path)]).wait()
            
    if scp(filename, server):
        print("File uploaded successfully.")
        return 0
    else:
        print("File upload failed.")
        return 1

parser = argparse.ArgumentParser()

parser.add_argument('--publish', '-p', action='store_true', help='Publish your note')
parser.add_argument('--show', '-s',  action='store_true', help='Shows you a preview of your renderd note')
parser.add_argument('note', nargs='+', help='Gives NoteKit the path of the source file ')
parser.add_argument('title', nargs='+', help='Set the title for your note')

parsed_args = parser.parse_args()
if parsed_args.publish:
    publish(parsed_args)
elif parsed_args.show:
    show(parsed_args)
