from thinkdsp import Chirp
from thinkdsp import normalize, unbias
from thinkdsp import decorate
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import decorate, read_wave

PI2 = 2 * np.pi

class SawtoothChirp(Chirp):

    def evaluate(self, ts):
 
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys

# signal = SawtoothChirp(start=220, end=880)
# wave = signal.make_wave(duration=1, framerate=4000)
# sp = wave.make_spectrogram(256)
# sp.plot()
# decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')

# signal = SawtoothChirp(start=2500, end=3000)
# wave = signal.make_wave(duration=1, framerate=20000)
# wave.make_spectrum().plot()
# decorate(xlabel='Frequency (Hz)')

# wave=read_wave(r'D:\vs_code_prace\Test\code_72475__rockwehrmann__glissup02.wav')
# wave.make_spectrogram(512).plot(high=5000)
# decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')


class TromboneGliss(Chirp):
    
    def evaluate(self, ts):

        l1, l2 = 1.0 / self.start, 1.0 / self.end
        lengths = np.linspace(l1, l2, len(ts))
        freqs = 1 / lengths
        
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        ys = self.amp * np.cos(phases)
        return ys
low = 262
high = 349
signal = TromboneGliss(high, low)
wave1 = signal.make_wave(duration=1)
signal = TromboneGliss(low, high)
wave2 = signal.make_wave(duration=1)
wave = wave1 | wave2
sp = wave.make_spectrogram(1024)
sp.plot(high=1000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')


plt.show()
