import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from utils.file_utils import get_path

class DialogContacts:
    def __init__(self, parent):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(get_path(__file__, "ui/contacts.glade"))
        self.builder.connect_signals(self)

        self.parent = parent

        self.window = self.builder.get_object("dialog_contacts")
        self.window.set_transient_for(self.parent)
        self.lbl_email = self.builder.get_object("lbl_email")
        self.lbl_email.set_markup('<a href="mailto:support@changenow.io">support@changenow.io</a>')
        self.lbl_telegram = self.builder.get_object("lbl_telegram")
        self.lbl_telegram.set_markup('<a href="https://t.me/changeNOW_chat">https://t.me/changeNOW_chat</a>')

        self.window.show_all()


    def run(self):
        response = self.window.run()
        self.window.hide()
        return response
    
    def destroy(self):
        self.window.destroy()
