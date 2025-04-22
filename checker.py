#!/usr/bin/env python3

import os
import shutil
import magika

#OUTDIR = '/tmp/ramdisk'
OUTDIR = '/home/user/projects/madoka/c'

SUCCESS_DIR = '/home/user/projects/madoka/polyglots'

m = magika.Magika()

for root, dirs, files in os.walk(OUTDIR):
    for f in files:
        filepath = os.path.join(root, f)
        res = m.identify_path(filepath)
        
        if res.output.label == 'elf':
            # If the output files are still identified as ELF,
            #   we're not interested because they are correctly classified
            os.remove(filepath)

        else:
            print("%s:%s" % (filepath,res.output.label))
            shutil.copy(filepath, os.path.join(SUCCESS_DIR,f))
            #raise Exception("WAOOO IT'S NOT AN ELF ACCORDING TO MAGIKA?!")
        #print(f)

#res = m.identify_path('./tests_data/basic/ini/doc.ini')
#print(res.output.label)
