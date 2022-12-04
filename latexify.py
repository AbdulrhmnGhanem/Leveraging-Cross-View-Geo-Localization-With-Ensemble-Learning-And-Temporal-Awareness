#! /usr/bin/env python

import re
import subprocess

def cite(groups):
    ref = groups.group(1)
    
    is_range_of_refs = '-' in ref
    is_comma_separated_refs = ',' in ref
    if is_range_of_refs:
        ref = ref.split('-')
        ref = range(int(ref[0]), int(ref[1])+1)
        ref = ','.join(f'bib{i}' for i in ref)
    elif is_comma_separated_refs:
        ref = ref.split(', ')
        ref = ','.join(f'bib{i}' for i in ref)
    else:
        ref = f'bib{ref}'

    return '~\\cite{' + ref + '}'

def table(txt, cols_num, rows_num):
    rows = txt.split('\n')
    rows = [rows[i:i+cols_num] for i in range(0, len(rows), cols_num)]
    assert len(rows) == rows_num, f'len(rows) = {len(rows)} != {rows_num}'
    table = [' & '.join((n, b, latexify(f' {r}'))) for n, b, r in rows]

    table_body = ''
    for line in table:
        table_body +=  '& ' + line + '& \\\\\n'
    table_body += '\\bottomrule'

    return table_body

def latexify(txt):
    txt = re.sub(r' \[([0-9-, ]+)\]', cite, txt)
    return txt.replace('%', '\%')



def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    p.wait()
    data = p.stdout.read()
    return data.decode('utf-8')

def setClipboardData(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    p.wait()

def references():
    with open('references.txt') as fp:
        refs = fp.readlines()
        assert len(refs) == 55
    s = ''
    for i, ref in enumerate(refs):
        s += '\\bibitem{bib' + str(i+1) + '}\n' + "ref" + "\n\\newblock{info} \n\n"
    print(s)

if __name__ == '__main__':
    latexified = latexify(getClipboardData())
    # setClipboardData(byte(latexified))
    print(latexified)
