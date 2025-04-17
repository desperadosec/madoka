#!/bin/bash

#ram://2097152 --> 1 GB
#ram://4194304 --> 2 GB
#ram://8388608 --> 4 GB
diskutil erasevolume HFS+ 'ramdisk' `hdiutil attach -nobrowse -nomount ram://2097152`
