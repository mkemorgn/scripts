#!/usr/bin/env python3

"""
This script makes it easier for me to copy photos from the SD card to my network drives using ExifTool
"""

import os
import glob

file_type = input("Raw or Jpg? (R or J)").lower()


def import_jpg():
    #  The load from location and the destination can be made variables at some point if need be.
    os.system(
        "exiftool -o . '-Directory<CreateDate' -d /mnt/share/photos/JPEGS/2022/%Y-%m-%d -r /run/media/mikem/disk/DCIM/109_FUJI"
    )


def import_raw():
    os.system(
        "exiftool -o . '-Directory<CreateDate' -d /mnt/share/backup/RAWS/2022/%Y-%m-%d -r /run/media/mikem/disk/DCIM/109_FUJI"
    )

    os.system(
        "exiftool -o . '-Directory<CreateDate' -d /mnt/share/photos/RAWS/2022/%Y-%m-%d -r /run/media/mikem/disk/DCIM/109_FUJI"
    )


if file_type == "r":
    import_raw()
else:
    import_jpg()
