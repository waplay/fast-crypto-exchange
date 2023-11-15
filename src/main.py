#!/usr/bin/env python3

# Copyright 2023 Sergey Tsymbal aka waplay

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.0")
from gi.repository import Gtk, WebKit2 as WebKit

import os
import sys
import webbrowser

# Need for snap
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from utils.api_utils import app_launch_stats
from dialog_about import DialogAbout
from dialog_how_it_works import DialogHowItWorks
from dialog_faq import DialogFAQ
from dialog_contacts import DialogContacts


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Fast Crypto Exchange")
        self.set_default_size(950, 650)

        self.webview = WebKit.WebView()
        self.webview.connect("create", self.on_webview_create)

        # Create menu
        menubar = Gtk.MenuBar()
        helpmenu = Gtk.Menu()
        helpm = Gtk.MenuItem(label="Help Center")
        menubar.append(helpm)
        helpm.set_submenu(helpmenu)

        # Create menu items and add it to the menu
        separator = Gtk.SeparatorMenuItem()
        separator2 = Gtk.SeparatorMenuItem()
        how_it_worksm = Gtk.MenuItem(label="How it works")
        faqm = Gtk.MenuItem(label="FAQ")
        term_of_use = Gtk.MenuItem(label="Term of use")
        privacy_policy = Gtk.MenuItem(label="Privacy policy")
        contactsm = Gtk.MenuItem(label="Contacts")
        aboutm = Gtk.MenuItem(label="About")
        statusm = Gtk.MenuItem(label="Check status")
        helpmenu.append(how_it_worksm)
        helpmenu.append(faqm)
        helpmenu.append(statusm)
        helpmenu.append(separator)
        helpmenu.append(term_of_use)
        helpmenu.append(privacy_policy)
        helpmenu.append(contactsm)
        helpmenu.append(separator2)
        helpmenu.append(aboutm)

        # Connect "activate" event to the handlers
        aboutm.connect("activate", self.on_about_menu_item_activate)
        how_it_worksm.connect("activate", self.on_how_it_works_menu_item_activate)
        faqm.connect("activate", self.on_faq_menu_item_activate)
        term_of_use.connect("activate", self.on_term_of_use_menu_item_activate)
        privacy_policy.connect("activate", self.on_privacy_policy_menu_item_activate)
        contactsm.connect("activate", self.on_contacts_menu_item_activate)
        statusm.connect("activate", self.on_status_menu_item_activate)

        # Create a VBox and add the menu and the rest of the GUI to it
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        vbox.pack_start(menubar, False, False, 0)
        vbox.pack_start(self.webview, True, True, 0)

        # Add the VBox to the window
        self.add(vbox)

        html_string_dark = """
    <body style="background-color:#2b2b35; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; margin: 0;">

		<iframe id='iframe-widget' src='https://changenow.io/embeds/exchange-widget/v2/widget.html?FAQ=true&amount=0.1&amountFiat&backgroundColor=2B2B35&darkMode=true&from=btc&horizontal=false&isFiat=false&lang=en-US&link_id=d52f8ce92c86d0&locales=true&logo=true&primaryColor=f45c26&to=eth&toTheMoon=false' style="height: 356px; width: 100%; border: none"></iframe>
        <script defer type='text/javascript' src='https://changenow.io/embeds/exchange-widget/v2/stepper-connector.js'></script>
    	
		<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; margin-top: 10px;">
        	<div style="text-align: center; margin-right: 20px;">
            	<p style="font-weight: bold; color: white; font-size: 14px;">Anonymous</p>
            	<p style="color: white; font-size: 12px;">No accounts, no verification, no KYC.<br>No one can block your funds.</p>
        	</div>
        	<div style="text-align: center; margin-left: 20px;">
            	<p style="font-weight: bold; color: white; font-size: 14px;">Secured</p>
            	<p style="color: white; font-size: 12px;">You fully control your funds.<br>Each exchange takes only ~2- 25 minutes.</p>
        	</div>
    	</div>
        <div style="width: 100%; text-align: center; margin-top: 40px;">
            <p style="color: gray; font-size: 10px;">Powered by <a href="https://documenter.getpostman.com/view/8180765/SVfTPnM8?version=latest#intro" style="color: gray; text-decoration: underline dashed gray;" onclick="window.open(this.href); return false;">ChangeNOW API</a></p>
        </div>
	</body>
        """

        html_string_light = """
    <body style="background-color:#FFFFFF; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; margin: 0;">

		<iframe id='iframe-widget' src='https://changenow.io/embeds/exchange-widget/v2/widget.html?FAQ=true&amount=0.1&amountFiat&backgroundColor=FFFFFF&darkMode=false&from=btc&horizontal=false&isFiat=false&lang=en-US&link_id=d52f8ce92c86d0&locales=true&logo=true&primaryColor=f45c26&to=eth&toTheMoon=false' style="height: 356px; width: 100%; border: none"></iframe>
        <script defer type='text/javascript' src='https://changenow.io/embeds/exchange-widget/v2/stepper-connector.js'></script>
    	
		<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; margin-top: 50px;">
        	<div style="text-align: center; margin-right: 20px;">
            	<p style="font-weight: bold; font-size: 14px;">Anonymous</p>
            	<p style="font-size: 12px;">No accounts, no verification, no KYC.<br>No one can block your funds.</p>
        	</div>
        	<div style="text-align: center; margin-left: 20px;">
            	<p style="font-weight: bold; font-size: 14px;">Secured</p>
            	<p style="font-size: 12px;">You fully control your funds.<br>Each exchange takes only ~2- 25 minutes.</p>
        	</div>
    	</div>
        <div style="width: 100%; text-align: center; margin-top: 40px;">
            <p style="color: gray; font-size: 10px;">Powered by <a href="https://documenter.getpostman.com/view/8180765/SVfTPnM8?version=latest#intro" style="color: gray; text-decoration: underline dashed gray;" onclick="window.open(this.href); return false;">ChangeNOW API</a></p>
        </div>
	</body>
        """

        settings = Gtk.Settings.get_default()
        gtk_theme_name = settings.get_property("gtk-theme-name")
        if "dark" in gtk_theme_name.lower():
            html_string = html_string_dark
        else:
            html_string = html_string_light

        self.webview.load_html(html_string, "")

        # Сollecting app launch statistics
        app_launch_stats()

    
    def on_about_menu_item_activate(self, widget):
        dialog = DialogAbout(self)
        dialog.run()
        dialog.destroy()

    def on_how_it_works_menu_item_activate(self, widget):
        dialog = DialogHowItWorks(self)
        dialog.run()
        dialog.destroy()

    def on_faq_menu_item_activate(self, widget):
        dialog = DialogFAQ(self)
        dialog.run()
        dialog.destroy()

    def on_term_of_use_menu_item_activate(self, widget):
        url = "https://changenow.io/terms-of-use"
        webbrowser.open(url)

    def on_privacy_policy_menu_item_activate(self, widget):
        url = "https://changenow.io/privacy-policy"
        webbrowser.open(url)

    def on_contacts_menu_item_activate(self, widget):
        dialog = DialogContacts(self)
        dialog.run()
        dialog.destroy()

    def on_status_menu_item_activate(self, widget):
        url = "https://changenow.io/status-page"
        webbrowser.open(url)

    def on_webview_create(self, webview, navigation_action):
        url = navigation_action.get_request().get_uri()
        webbrowser.open(url)
        return None

    
def main():
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
