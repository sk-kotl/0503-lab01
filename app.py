import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

bld = Gtk.Builder()
bld.add_from_file('ui.glade')

win = bld.get_object('wnd')
pic = bld.get_object('pic')

a = bld.get_object('inp_a').get_text()
b = bld.get_object('inp_b').get_text()
c = bld.get_object('inp_c').get_text()

def result(obj):
    if (a == b or b == c or a == c):
        dialog = Gtk.MessageDialog(message_type=Gtk.MessageType.INFO,
                                   buttons=Gtk.ButtonsType.OK,
                                   text="Равнобедренный",
                                   secondary_text="вы посмотрели на равнобедренный треугольник.")
        pic.set_from_file('rb.png')
    # ...

tab = {
    "onDestroy": Gtk.main_quit,
    "btn_res": result
}

bld.connect_signals(tab)
win.show_all()

Gtk.main()