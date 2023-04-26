# Two Neurons

# Both neurons respond differently to inputs. Each sensitive to either positive or negative
# inputs respectively. This is an inherent property of real neurons called "on" and "off" neurons.

# Bottom graph combines the output of both neurons and shows the "decoded" value.

# Two neurons represent the input more accurately.

import nengo

model = nengo.Network()
with model:
    stim = nengo.Node(0)
    ens = nengo.Ensemble(n_neurons=2, dimensions=1, seed=5)
    nengo.Connection(stim, ens)