import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from utils.file_utils import get_path

class DialogHowItWorks:
    def __init__(self, parent):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(get_path(__file__, "ui/how_it_works.glade"))

        self.parent = parent

        self.window = self.builder.get_object("dialog_how_it_works")
        self.window.set_transient_for(self.parent)

        self.window.show_all()


    def run(self):
        response = self.window.run()
        self.window.hide()
        return response
    
    def destroy(self):
        self.window.destroy()
