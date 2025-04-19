#!/usr/bin/env python3

import os
import magika

OUTDIR = '/tmp/ramdisk'

m = magika.Magika()

for root, dirs, files in os.walk(OUTDIR):
    for f in files:
        filepath = os.path.join(root, f)
        res = m.identify_path(filepath)
        
        if res.output.label == 'elf':
            os.remove(filepath)

        else:
            print(res.output.label)
            raise Exception("WAOOO IT'S NOT AN ELF ACCORDING TO MAGIKA?!")
        #print(f)

#res = m.identify_path('./tests_data/basic/ini/doc.ini')
#print(res.output.label)
