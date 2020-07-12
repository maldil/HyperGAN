from hypergan.samplers.base_sampler import BaseSampler
from hypergan.gan_component import ValidationException, GANComponent

import numpy as np
import time

class AlignedSampler(BaseSampler):
    def __init__(self, gan, samples_per_row=8):
        BaseSampler.__init__(self, gan, samples_per_row)
        self.inputs = self.gan.inputs.next()
        self.inputs2 = self.gan.inputs.next(1)

    def compatible_with(gan):
        if hasattr(gan, 'encoder'):
            return True
        return False

    def _sample(self):
        #self.inputs = self.gan.inputs.next()
        g = self.gan.generator.forward(self.inputs)
        g2 = self.gan.generator2.forward(g)
        return [
            ('input', self.inputs),
            ('input2', self.inputs2),
            ('generator', g),
            ('generator2', g2)
        ]

