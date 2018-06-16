#!/usr/bin/python
import sys, os, re
import pypandoc

def print_usage():
    print 'Usage: python %s <MARKDOWN_FILE>\n' % (os.path.basename(__file__))
    exit()


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
      print_usage()
    

    in_file = sys.argv[1]
    out_file = re.sub(r'\.[^\.]*$', '', in_file) + '.html'
    args = ['--smart',
            '--standalone',
            '--mathjax',
            '--highlight-style=pygments',
            '--include-in-header=%s/style.html' % sys.path[0],
            '--include-before-body=%s/before.html' % sys.path[0],
            '--include-after-body=%s/after.html' % sys.path[0],
            ]

    html = pypandoc.convert_file(in_file, 'html', extra_args=args, outputfile=out_file)
