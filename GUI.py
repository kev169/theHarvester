__author__ = 'Kevin Haubris'

from gi.repository import Gtk as gtk

class WindowHandler:

    def run(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("Design/Layout/harvester-gui.glade")
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("main")
        self.window.show_all()
        gtk.main()

    def onDeleteWindow(self, *args):
        gtk.main_quit(*args)

if __name__ == "__main__":
    gclass = WindowHandler()
    gclass.run()