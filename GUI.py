__author__ = 'Kevin Haubris'

from gi.repository import Gtk as gtk


class WindowHandler:
    data = ["google", "bing", "other"]

    def run(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("Design/Layout/harvester-gui mk 2.glade")
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.cell = gtk.CellRendererText()
        name_store = gtk.ListStore(int,str)
        for count, item in enumerate(self.data):
            name_store.append((count, item))
        comboview = self.builder.get_object("combobox1")
        comboview.set_model(name_store)
        comboview.pack_start(self.cell, True)
        comboview.add_attribute(self.cell, 'text',1)
        comboview.set_active(0)
        self.window.show_all()
        gtk.main()

    def onDeleteWindow(self, *args):
        gtk.main_quit(*args)

    """def PopulateList(self, variable):
        name_store = gtk.TreeStore(int,str)
        for count, item in enumerate(self.data):
            name_store.append(count, item)
        comboview = self.builder.get_object("combobox1")
        comboview.set_model(name_store)"""


if __name__ == "__main__":
    gclass = WindowHandler()
    gclass.run()
