from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
from thinkdsp import decorate
from thinkdsp import SquareSignal
import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal

class SawtoothSignal(Sinusoid):
    def evaluate(self, ts):
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys
# sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000)
# sawtooth.make_audio() 
# sawtooth.make_spectrum().plot()
# decorate(xlabel='Frequency (Hz)')
# sawtooth.make_spectrum().plot(color='gray')
# square = SquareSignal(amp=0.5).make_wave(duration=0.5, framerate=40000)
# square.make_spectrum().plot()
# decorate(xlabel='Frequency (Hz)')
# sawtooth.make_spectrum().plot(color='gray')
# triangle = TriangleSignal(amp=0.79).make_wave(duration=0.5, framerate=40000)
# triangle.make_spectrum().plot()
# decorate(xlabel='Frequency (Hz)')
# plt.show()

# square = SquareSignal(1100).make_wave(duration=0.5, framerate=10000)
# square.make_spectrum().plot()
# decorate(xlabel='Frequency (Hz)')
# plt.show()

# triangle = TriangleSignal().make_wave(duration=0.01)
# triangle.plot()
# decorate(xlabel='Time (s)')
# plt.show()

# spectrum = triangle.make_spectrum()
# print(spectrum.hs[0])

# spectrum.hs[0] = 100
# triangle.plot(color='gray')
# spectrum.make_wave().plot()
# decorate(xlabel='Time (s)')
# plt.show()

def filter_spectrum(spectrum):
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0
wave = TriangleSignal(freq=440).make_wave(duration=0.5)
spectrum = wave.make_spectrum()
# plt.subplot(121)
# spectrum.plot(high=10000, color='gray')
# plt.subplot(122)
# filter_spectrum(spectrum)
# spectrum.scale(440)
# spectrum.plot(high=10000)
# decorate(xlabel='Frequency (Hz)')
# plt.show()

# wave = SquareSignal(freq=440).make_wave(duration=0.5)
# spectrum = wave.make_spectrum()
# plt.subplot(121)
# spectrum.plot(high=10000, color='gray')
# plt.subplot(122)
# filter_spectrum(spectrum)
# spectrum.scale(440)
# spectrum.plot(high=10000)
# decorate(xlabel='Frequency (Hz)')
# plt.show()


# wave = SawtoothSignal(freq=440).make_wave(duration=0.5)
# spectrum = wave.make_spectrum()
# plt.subplot(121)
# spectrum.plot(high=10000, color='gray')
# plt.subplot(122)
# filter_spectrum(spectrum)
# spectrum.scale(440)
# spectrum.plot(high=10000)
# decorate(xlabel='Frequency (Hz)')
# plt.show()

filtered = spectrum.make_wave()
filtered.make_audio()
