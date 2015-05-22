#!/usr/bin/env python

HEADER = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">

        <link href='http://fonts.googleapis.com/css?family=Lato&subset=latin,latin-ext' rel='stylesheet' type='text/css'>

        <style>
        *, *:after, *::before {
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
        }
        
        html, body {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: left;
        }

        .content {
            position: relative;
            padding: 1em 0;
            width: 70%;
            text-align: left;
            margin-right: auto;
            margin-left: auto;
        }
        
         * {
           font-family: sans-serif;
           font-weight:300;
         }
        </style>

    </head>
    <body>
        <div class="content">
"""

FOOTER = """
        <div>
    </body>
</html>
"""
