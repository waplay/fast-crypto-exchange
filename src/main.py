#!/usr/bin/env python3

# sudo apt install python3-venv
# python3 -m venv venv
# python3 -m venv --system-site-packages venv
# source venv/bin/activate (. venv/bin/activate)
# pip install -r requirements.txt
# pip freeze > requirements.txt

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.0")
from gi.repository import Gtk, WebKit2 as WebKit

import os
import sys
import webbrowser

# Need for snap
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from dialog_about import DialogAbout


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Fast Crypto Exchange")
        self.set_default_size(800, 650)

        self.webview = WebKit.WebView()
        self.webview.connect("create", self.on_webview_create)

        # Create a MenuBar
        menubar = Gtk.MenuBar()

        # Create a menu
        helpmenu = Gtk.Menu()

        # Create a menu item
        helpm = Gtk.MenuItem(label="Help Center")

        # Add menu items to the menu bar
        menubar.append(helpm)

        # Add the menu to the menu items
        helpm.set_submenu(helpmenu)

        # Create "About" menu item and add it to "Help" menu
        how_it_worksm = Gtk.MenuItem(label="How it works")
        faqm = Gtk.MenuItem(label="FAQ")
        term_of_use = Gtk.MenuItem(label="Term of use")
        privacy_policy = Gtk.MenuItem(label="Privacy policy")
        contactm = Gtk.MenuItem(label="Contact")
        aboutm = Gtk.MenuItem(label="About")
        helpmenu.append(how_it_worksm)
        helpmenu.append(faqm)
        helpmenu.append(term_of_use)
        helpmenu.append(privacy_policy)
        helpmenu.append(contactm)
        helpmenu.append(aboutm)

         # Connect "activate" event to the handler
        aboutm.connect("activate", self.on_about_menu_item_activate)

        # Create a VBox and add the menu and the rest of the GUI to it
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        vbox.pack_start(menubar, False, False, 0)
        vbox.pack_start(self.webview, True, True, 0)

        # label = Gtk.Label()
        # label.set_markup("<span font='8'>Powered by ChangeNow</span>")
        # vbox.pack_start(label, False, False, 0)

        # Add the VBox to the window
        self.add(vbox)

        html_string_dark = """
        <body style="background-color:#2b2b35;">
        <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
<iframe id='iframe-widget' src='https://changenow.io/embeds/exchange-widget/v2/widget.html?FAQ=true&amount=0.1&amountFiat=1500&backgroundColor=2B2B35&darkMode=true&from=btc&fromFiat=eur&horizontal=false&isFiat=false&lang=en-US&link_id=d52f8ce92c86d0&locales=true&logo=false&primaryColor=f45c26&to=eth&toFiat=eth&toTheMoon=true' style="height: 356px; width: 100%; border: none"></iframe>
</div>
    <script defer type='text/javascript' src='https://changenow.io/embeds/exchange-widget/v2/stepper-connector.js'></script>
</body>
        """

        html_string_light = """
        <body style="background-color:#FFFFFF;">
        <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
<iframe id='iframe-widget' src='https://changenow.io/embeds/exchange-widget/v2/widget.html?FAQ=true&amount=0.1&amountFiat=1500&backgroundColor=FFFFFF&darkMode=false&from=btc&fromFiat=eur&horizontal=false&isFiat=false&lang=en-US&link_id=d52f8ce92c86d0&locales=true&logo=false&primaryColor=f45c26&to=eth&toFiat=eth&toTheMoon=true' style="height: 356px; width: 100%; border: none"></iframe>
</div>
    <script defer type='text/javascript' src='https://changenow.io/embeds/exchange-widget/v2/stepper-connector.js'></script>
</body>
        """

        settings = Gtk.Settings.get_default()
        gtk_theme_name = settings.get_property("gtk-theme-name")
        if "dark" in gtk_theme_name.lower():
            html_string = html_string_dark
        else:
            html_string = html_string_light

        self.webview.load_html(html_string, "")

    
    def on_about_menu_item_activate(self, widget):
        dialog = DialogAbout(self)
        dialog.run()
        dialog.destroy()

    def on_webview_create(self, webview, navigation_action):
        url = navigation_action.get_request().get_uri()
        webbrowser.open(url)
        return False


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
