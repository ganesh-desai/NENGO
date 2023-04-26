# Adding Groups

# If two groups are connected to the same ensemble the ensemble will recieve input from
# both sources and will represent the sum of all it's inputs.

# Ensembles have "radius" which is a particular range of values they can represent. The default
# radius is 1, i.e represents values between -1 and 1.

# If radius is changed, for example to -2 and 2, the ensemble will be efficient at representing
# values between -2 and 2. Also, the graph range setting has to be changed to match the new value.

import nengo

model = nengo.Network()
with model:
    stim_a = nengo.Node(0)
    a = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim_a, a)

    stim_b = nengo.Node(0)
    b = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim_b, b)

    c = nengo.Ensemble(n_neurons=50, dimensions=1, radius=1)
    nengo.Connection(a, c)
    nengo.Connection(b, c)