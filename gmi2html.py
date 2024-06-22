#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
filename = args.filename
pre = False
style = 'style.css'
with open(filename, 'r') as f:
    lines = f.readlines()
with open(filename.rsplit('.', 1)[0] + '.html', 'w') as f:
    f.write('<!DOCTYPE html>\n<html>\n<head>')
    if style:
        f.write(f'<link href="{style}" rel="stylesheet">')
    f.write('</head>\n<body>')
    for line in lines:
        if pre:
            match line:
                case '```\n':
                    f.write('</pre>')
                    pre = False
                case other:
                    f.write(line)
        else:
            match line[:2]:
                case '=>':
                    ln = line.split(' ', 2)
                    f.write(f'<a href="{ln[1].strip()}">{ln[2].strip()}</a>')
                case '# ':
                    ln = line.split(' ', 1)
                    f.write(f'<h1>{ln[1]}</h1>')
                case '##':
                    ln = line.split(' ', 1)
                    if line[2] == '#':
                        h = 3
                    else:
                        h = 2
                    f.write(f'<h{h}>{ln[1]}</h{h}>')
                case '> ':
                    ln = line.split(' ', 1)
                    f.write(f'<blockquote>{ln[1]}</blockquote>')
                case '``':
                    if line[2] == '`':
                        pre = True
                        f.write('<pre>')
                    else:
                        f.write(f'<p>{line}</p>')
                case '* ':
                    ln = line.split(' ', 1)
                    f.write(f'<li>•\n{ln[1]}</li>')
                case other:
                    if not line == '\n':
                        f.write(f'<p>{line}</p>')
            f.write('\n')
    f.write('</body>\n</html>')
