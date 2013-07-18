import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.widgets import Slider, Button, RadioButtons

ax = plt.subplot(111)
plt.subplots_adjust( bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)
a0 = 3
f0 = 10
d0 = 0.5
s = a0*signal.square(2*np.pi*f0*t,duty=d0)
l, = plt.plot(t,s, lw=2, color='red')
plt.axis([0, 1, -6, 6])
plt.title("Stimulation Parameters")
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')
plt.grid()

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.2, 0.05, 0.65, 0.03], axisbg=axcolor)
axamp  = plt.axes([0.2, 0.1, 0.65, 0.03], axisbg=axcolor)
axduty = plt.axes([0.2, 0.15, 0.65, 0.03],axisbg=axcolor)

sfreq = Slider(axfreq, 'Freq', 5, 100.0, valinit=f0)
samp = Slider(axamp, 'Amp', 1, 5.0, valinit=a0)
sduty = Slider(axduty, 'Duty', 0.1, 0.9, valinit=d0)

def update(val):
    amp = samp.val
    freq = sfreq.val
    d = sduty.val
    l.set_ydata(amp*signal.square(2*np.pi*freq*t,duty=d))
    plt.draw()

sfreq.on_changed(update)
samp.on_changed(update)
sduty.on_changed(update)

# resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
# button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
# def reset(event):
#     sfreq.reset()
#     samp.reset()
#     sduty.reset()

#button.on_clicked(reset)



plt.show()
