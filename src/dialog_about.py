import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import webbrowser
from utils.file_utils import get_path
from version import __version__

class DialogAbout:
    def __init__(self, parent):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(get_path(__file__, "ui/about.glade"))
        self.builder.connect_signals(self)

        self.parent = parent

        self.window = self.builder.get_object("dialog_about")
        self.window.set_transient_for(self.parent)
        self.btn_donate = self.builder.get_object("btn_donate")
        self.lbl_version = self.builder.get_object("lbl_version")
        self.lbl_version.set_text(
            "version: " + __version__
        )
        self.lbl_email = self.builder.get_object("lbl_email")
        self.lbl_email.set_markup('<a href="mailto:waplay@yahoo.com">email: waplay@yahoo.com</a>')
        self.lbl_site = self.builder.get_object("lbl_site")
        self.lbl_site.set_markup('<a href="https://waplay.github.io">site: waplay.github.io</a>')

        self.window.show_all()

    def on_btn_donate_clicked(self, widget):
        webbrowser.open("https://nowpayments.io/donation/waplay")

    def run(self):
        response = self.window.run()
        self.window.hide()
        return response
    
    def destroy(self):
        self.window.destroy()
