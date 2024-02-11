#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 5467555331
    OWNER = config("OWNER")
    ffmpegcode = ["-preset superfast -c:v libx265 -s 1920x1080 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 5 -metadata title='FZXAnime [t.me/FZXAnime]' -metadata author='𝖥𝖹𝖷𝖠𝗇𝗂𝗆𝖾 [รíӀҽղԵ ժҽʍօղ]' -metadata:s:a title='𝖥𝖹𝖷 𝖠𝗇𝗂𝗆𝖾 [รíӀҽղԵ ժҽʍօղ]' -metadata:s:v title='ENCODED_BY [รíӀҽղԵ ժҽʍօղ]'"]
    THUMB = config("THUMBNAIL")
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit(1)
