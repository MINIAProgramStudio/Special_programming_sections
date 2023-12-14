from random import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button, CheckButtons
from operator import add
from scipy import signal
import math

fig, ax = plt.subplots(figsize=(10,13),num="Programme d'onde sinusoïdale") #створення вікна розмірами 10х15
plt.subplots_adjust(left=0.25, bottom=0.25)

x_axis = np.arange(0.0, np.pi*2, 0.001) #створення вісі абцис

class Noise: #клас збереження та генерації шуму
    def __init__(self):
        self.values = np.arange(0.0, np.pi*2, 0.001)*0
    def update(self, mean, disp):
        self.values = [(random()-0.5)*disp+mean+i-i for i in self.values]
PN = Noise()

def_opt = { #значення налаштувань за замовчуванням
    "amplitude" : 1,
    "frequency" : 1,
    "phase" : 0,
    "noise_mean": 0,
    "noise_disp": 0,
    "show_noise": False,
    "noise_undefined": True,
    "filter_len": 1,
    "filter_power": 1
}
def filter(length, power):
    length = int(length)
    return [math.sqrt(power/np.pi)*math.exp(-power*i**2) for i in range(int(length)*2+1)]



#Функція синусоїди з шумом
def harmonic_with_noise(amplitude = 1, frequency = 1, phase = 0, noise_mean = 0, noise_disp = 0, show_noise = False,update_noise = False):
    base_line = amplitude * np.sin(frequency*x_axis + phase) #створення чистої синусоїди
    if show_noise:
        if update_noise:
            PN.update(noise_mean, noise_disp) #оновлення шуму, якщо вказано за потрібне
        done_line = list(map(add, base_line, PN.values)) #додання шуму до чистої синусоїди
        return done_line
    else:
        return base_line

l, = plt.plot(x_axis, harmonic_with_noise(), lw=2, color='red', label = "Фактична") #малювання найпершої синусоїди

l2, = plt.plot(x_axis, signal.order_filter(harmonic_with_noise(),filter(def_opt['filter_len'],def_opt['filter_power']),0), lw=2,color='blue', label = 'Фільтрована')
l3, = plt.plot(x_axis, harmonic_with_noise(), lw=2, color='green', label = "Оригінал")
l2.set_visible(False)
l3.set_visible(False)
lines = [l,l2,l3]

plt.axis([0, np.pi*2, -np.pi, np.pi])


#створення повзунків
ax_color = 'lightgoldenrodyellow'
ax_freq = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=ax_color)
ax_amp = plt.axes([0.25, 0.175, 0.65, 0.03], facecolor=ax_color)
ax_phase = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=ax_color)
ax_noise_mean = plt.axes([0.25, 0.125, 0.65, 0.03], facecolor=ax_color)
ax_noise_disp = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=ax_color)
ax_filter_n = plt.axes([0.25, 0.075, 0.65, 0.03], facecolor=ax_color)
ax_filter_fr = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=ax_color)


s_freq = Slider(ax_freq, 'Частота', 0.1, 30.0, valinit=def_opt['frequency'])
s_amp = Slider(ax_amp, 'Амплітуда', 0.001, np.pi, valinit=def_opt['amplitude'])
s_phase = Slider(ax_phase, 'Фаза', 0, 2*np.pi, valinit=def_opt['phase'])
s_noise_mean = Slider(ax_noise_mean, 'Середнє значення шуму', -np.pi, np.pi, valinit=def_opt['noise_mean'])
s_noise_disp = Slider(ax_noise_disp, 'Дисперсія шуму', 0, 2*np.pi, valinit=def_opt['noise_disp'])
s_filter_n = Slider(ax_filter_n, 'Порядок фільтру', 0, 2, valinit=def_opt['noise_disp'])
s_filter_fr = Slider(ax_filter_fr, 'Частота фільтру', 0, 2, valinit=def_opt['noise_disp'])


#створення кнопки та чекбоксу
resetax = plt.axes([0.025, 0.4, 0.2, 0.04])
button = Button(resetax, 'Скинути налаштування', color=ax_color, hovercolor='0.975')
rax = plt.axes([0.025, 0.44, 0.2, 0.04], facecolor=ax_color)
radio = CheckButtons(rax, (['Показувати шум']))


def update_sin(val): #оновлення синусоїди, якщо було змінено параметри чистої синусоїди
    l.set_ydata(harmonic_with_noise(s_amp.val, s_freq.val, s_phase.val, s_noise_mean.val, s_noise_disp.val,def_opt['show_noise']))
    l2.set_ydata(
        signal.order_filter(harmonic_with_noise(s_amp.val, s_freq.val, s_phase.val, s_noise_mean.val, s_noise_disp.val,
                                                def_opt['show_noise']), filter(s_filter_n.val, s_filter_fr.val), 0))
    l3.set_ydata(harmonic_with_noise(s_amp.val, s_freq.val, s_phase.val, s_noise_mean.val, s_noise_disp.val))
    fig.canvas.draw_idle()
s_freq.on_changed(update_sin)
s_amp.on_changed(update_sin)
s_phase.on_changed(update_sin)

def update_noise(val): #оновлення синусоїди, якщо було змінено параметри шуму
    l.set_ydata(harmonic_with_noise(s_amp.val, s_freq.val, s_phase.val, s_noise_mean.val, s_noise_disp.val,
                                    def_opt['show_noise'], True))
    l2.set_ydata(
        signal.order_filter(harmonic_with_noise(s_amp.val, s_freq.val, s_phase.val, s_noise_mean.val, s_noise_disp.val,
                                                def_opt['show_noise']), filter(s_filter_n.val, s_filter_fr.val), 0))
    l3.set_ydata(harmonic_with_noise(s_amp.val, s_freq.val, s_phase.val, s_noise_mean.val, s_noise_disp.val))
    fig.canvas.draw_idle()
s_noise_mean.on_changed(update_noise)
s_noise_disp.on_changed(update_noise)

def update_filter(val):
    l2.set_ydata(
        signal.order_filter(harmonic_with_noise(s_amp.val, s_freq.val, s_phase.val, s_noise_mean.val, s_noise_disp.val,
                                                 def_opt['show_noise']),filter(s_filter_n.val,s_filter_fr.val),0))
    l3.set_ydata(harmonic_with_noise(s_amp.val, s_freq.val, s_phase.val, s_noise_mean.val, s_noise_disp.val))
    fig.canvas.draw_idle()
s_filter_n.on_changed(update_filter)
s_filter_fr.on_changed(update_filter)


#функція відновлення значень за замовчуванням
def reset(event):
    s_freq.reset()
    s_amp.reset()
    s_phase.reset()
    s_noise_mean.reset()
    s_noise_disp.reset()
button.on_clicked(reset)


#функція-обробник стану чекбоксу: увімкнення та вимкнення шуму
def callback(label):
    if def_opt['show_noise']:
        def_opt['show_noise']=False
        l.set_ydata(harmonic_with_noise(s_amp.val, s_freq.val, s_phase.val, s_noise_mean.val, s_noise_disp.val,
                                        def_opt['show_noise'], def_opt["noise_undefined"]))
        def_opt["noise_undefined"] = False
        l2.set_visible(False)
        l3.set_visible(False)
    else:
        def_opt['show_noise'] = True
        l.set_ydata(harmonic_with_noise(s_amp.val, s_freq.val, s_phase.val, s_noise_mean.val, s_noise_disp.val,
                                        def_opt['show_noise'], def_opt["noise_undefined"]))
        def_opt["noise_undefined"] = False
        l2.set_visible(True)
        l3.set_visible(True)
    fig.canvas.draw_idle()
radio.on_clicked(callback)

plt.show()