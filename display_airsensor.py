#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in9
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    epd = epd2in9.EPD()
    logging.info("init and Clear")
    epd.init(epd.lut_full_update)
    epd.Clear(0xFF)
    
    logging.info("3.read bmp file")
    Himage = Image.open('airsensorimage.bmp')
    epd.display(epd.getbuffer(Himage))

    logging.info("Goto Sleep...")
    epd.sleep()
    epd.Dev_exit()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in9.epdconfig.module_exit()
    exit()
