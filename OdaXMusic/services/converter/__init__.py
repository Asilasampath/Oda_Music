from os import listdir, mkdir

if "raw_files" not in listdir():
    mkdir("raw_files")

from OdaXMusic.services.converter.converter import convert
