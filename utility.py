import os
import getpass
import datetime

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

from html.parser import HTMLParser

link = ""
class MyHTMLParser(HTMLParser):
    def handle_startendtag(self, tag, attrs):
        if tag == "link" and attrs[1][1][:4] == "/th?":
            global link
            link = "https://www.bing.com" + attrs[1][1]

def download_image():
    """
    Downloads the current image from Bing
    """
    logging.info("download_image called")
    os.system("wget -nv https://www.bing.com -O .bing_html")
    logging.info("Received Bing page")
    with open(".bing_html") as html:
        first_line = html.readline()
        parser = MyHTMLParser()
        parser.feed(first_line)
        logging.info("Downloading %s", link)
        if link == "":
            logging.error("Link is null")
            return -1
        else:
            os.system("wget -nv -O ~/.image.jpeg %s" % link)
    logging.info("Downloaded image")

def set_wallpaper(image=".image.jpeg"):
    """
    Sets the current wallpaper to image
    """
    logging.info("set_wallpaper called")
    os.system("gsettings set org.gnome.desktop.background picture-uri \"file:///home/%s/%s\"" %
              (getpass.getuser(), image))
    logging.info("Wallpaper should have changed")

def save_wallpaper():
    """
    Saves the shown wallpaper to pictures folder
    """
    # logging.info("save_wallpaper called")
    os.system("cp ~/.image.jpeg ~/Pictures/%s.jpeg"%(datetime.date.today()))
    # logging.info("Wallpaper should have saved")
