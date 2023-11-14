import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from utils.file_utils import get_path

class DialogFAQ:
    def __init__(self, parent):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(get_path(__file__, "ui/faq.glade"))

        self.parent = parent

        self.window = self.builder.get_object("dialog_faq")
        self.window.set_transient_for(self.parent)

        self.window.show_all()


    def run(self):
        response = self.window.run()
        self.window.hide()
        return response
    
    def destroy(self):
        self.window.destroy()
