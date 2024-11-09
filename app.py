import gi
import matplotlib.pyplot as plt
import numpy as np
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

bld = Gtk.Builder()
bld.add_from_file('ui.glade')

win = bld.get_object('wnd')
pic = bld.get_object('pic')

inpa = bld.get_object('inp_a')
inpb = bld.get_object('inp_b')
inpc = bld.get_object('inp_c')

def Gtkdialog(type, title, text):
    if type == "error":
        type = Gtk.MessageType.ERROR
    if type == "info":
        type = Gtk.MessageType.INFO
    return Gtk.MessageDialog(message_type=type,
                             buttons=Gtk.ButtonsType.OK,
                             text=title,
                             secondary_text=text)

def plot_error(text):
    plt.figure(figsize=(5, 3.1), dpi=100)
    plt.text(0.5, 0.5, str(text), ha='center', va='center', fontsize=12, color='red', wrap=True)
    plt.axis("off")
    plt.savefig("plot.png", bbox_inches="tight", pad_inches=0)
    plt.close()

def plot_triangle(a, b, c):
    A = np.array([0, 0])
    B = np.array([a, 0])
    C = np.array([
        (a**2 + c**2 - b**2) / (2 * a),
        np.sqrt(c**2 - ((a**2 + c**2 - b**2) / (2 * a))**2)
    ])
    
    plt.figure(figsize=(5, 3.1), dpi=100)
    plt.plot([A[0], B[0]], [A[1], B[1]], 'b-')
    plt.plot([B[0], C[0]], [B[1], C[1]], 'b-')
    plt.plot([C[0], A[0]], [C[1], A[1]], 'b-')
    plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color="red")
    plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
    plt.text(B[0], B[1], 'B', fontsize=12, ha='left')
    plt.text(C[0], C[1], 'C', fontsize=12, ha='left')
    
    AB_mid = (A + B) / 2 + np.array([0, -0.15])
    BC_mid = (B + C) / 2 + np.array([0.15, 0])
    CA_mid = (C + A) / 2 + np.array([-0.15, 0])
    plt.text(AB_mid[0], AB_mid[1], f'{a}', fontsize=10, color='black', ha='center')
    plt.text(BC_mid[0], BC_mid[1], f'{b}', fontsize=10, color='black', ha='center')
    plt.text(CA_mid[0], CA_mid[1], f'{c}', fontsize=10, color='black', ha='center')
    
    plt.axis("equal")
    plt.axis("off")
    plt.savefig("plot.png", bbox_inches="tight", pad_inches=0)
    plt.close()

def result(obj):
    try:
        a = int(inpa.get_text())
        b = int(inpb.get_text())
        c = int(inpc.get_text())
    except:
        dialog = Gtkdialog('error', 'Значения указаны неверно', 'Одно или несколько значений заполнены наверно.\nПринимаются только целые числа')
        plot_error("Неверные значения:\nЗначения должны быть целыми и положительными")
        pic.set_from_file('plot.png')
    else:
        if a + b <= c or a + c <= b or b + c <= a:
            dialog = Gtkdialog('error', 'Треугольник не существует', 'Треугольник с указанными значениями не существует')
            plot_error("Неверные значения:\nНесуществующий треугольник")
            pic.set_from_file('plot.png')
        else:
            plot_triangle(a,b,c)
            if (a == b == c):
                dialog = Gtkdialog('info', 'Равносторонний треугольник', 'вы посмотрели на равносторонний треугольник')
                return
            if a == b or b == c or a == c:
                dialog = Gtkdialog('info', 'Равнобедренный треугольник', "вы посмотрели на равнобедренный треугольник")
                return
            if  a**2 + b**2 == c**2:
                dialog = Gtkdialog('info', 'Прямоугольный треугольник', "вы посмотрели на прямоугольный треугольник")
                return
            elif a**2 + b**2 < c**2:
                dialog = Gtkdialog('info', 'Тупоугольный треугольник', "вы посмотрели на тупоугольный треугольник")
                return
            else:
                dialog = Gtkdialog('info', 'Остроугольный треугольник', "вы посмотрели на остроугольный треугольник")
                return
    finally:
        pic.set_from_file('plot.png')
        dialog.connect('response', lambda d, self: d.destroy())
        dialog.present()

def destroy(obj):
    try:
        os.remove("plot.png")
    except:
        return
    finally:
        Gtk.main_quit()

def cls_plt(obj):
    pic.set_from_file()
    try:
        os.remove("plot.png")
    except:
        return
    finally:
        pass

def cls_all(obj):
    pic.set_from_file()
    try:
        os.remove('plot.png')
    except:
        return
    finally:
        inpa.set_text('')
        inpb.set_text('')
        inpc.set_text('')

def cls_vals(obj):
    inpa.set_text('')
    inpb.set_text('')
    inpc.set_text('')

tab = {
    "onDestroy": destroy,
    "btn_res": result,
    "clear_plot": cls_plt,
    "clear_inp": cls_vals,
    "clear_all": cls_all
}

bld.connect_signals(tab)
win.show_all()

Gtk.main()