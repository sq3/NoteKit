#!/usr/bin/env python

import codecs
import notekit_html
import markdown

##Makrdown Converting starts here

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
