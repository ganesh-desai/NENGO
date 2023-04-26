# Multiple Dimensions

# An ensemble does not have to represent a single value. Each group can represent multiple values.

# The number of values a group is representing is called "dimensions".

# Eg: Spatial coordinates (x, y, z) = 3 dimensions

# In this model, three different values are being decoded from each of the groups of neurons. 

# Nengo decodes these values by finding different ways of weighting together the actual spiking output (top graphs) in order to produce the bottom graphs.

# Slider = input
# Value = decoded value
# Spikes = firing activity (output)

import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0, 0, 0])
    a = nengo.Ensemble(n_neurons=200, dimensions=3)
    nengo.Connection(stim, a)

    b = nengo.Ensemble(n_neurons=200, dimensions=3)
    nengo.Connection(a, b)