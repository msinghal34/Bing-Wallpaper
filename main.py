import os
import getpass
import datetime

import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

from utility import save_wallpaper, set_wallpaper, download_image


def apply(button):
    logging.info("Apply button clicked")
    set_wallpaper()
    

def save(button):
    logging.info("Save button clicked")
    save_wallpaper()


def refresh(button):
    logging.info("Refresh button clicked")
    update_image()
    pass
    
handlers = {
    "onDestroy": Gtk.main_quit,
    "apply": apply,
    "save": save,
    "refresh": refresh
}

builder = Gtk.Builder()
builder.add_from_file("screen.glade")
builder.connect_signals(handlers)

if download_image() == -1:
    pass

def update_image():
    logging.info("update_image called")
    try:
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="/home/%s/.image.jpeg" % (getpass.getuser()), width=1200, height=1200, preserve_aspect_ratio=True)
        image = builder.get_object("image1")
        image.set_from_pixbuf(pixbuf)
    except:
        pass

window = builder.get_object("window1")
window.show_all()
Gtk.main()
