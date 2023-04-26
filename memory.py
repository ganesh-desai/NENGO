# Memory

# To store information, we make a connection from an ensemble back to itself. That is, we create a second ensemble that is representing
# the same value that the original is currently representing and connect it to itself.

# If that input is zero, then the stored value should stay the same as it currently is.
# If the input is positive, the stored value should increase.
# If the input is negative, it should decrease.

# The input Connection "transform=0.1" is to control how strongly the input affects the stored value. Larger = quicker change in stored value.

# Recurrent Connection from b back to itself has synapse=0.1 as the longer time constant makes the memory more stable, and is commonly
# found in the real brain for recurrent connections.

# Mathematical Note: In the case where the input transform is exactly equal to the recurrent synapse (as it is here), it turns out that the resulting system
# should compute the mathematical integral of the input.

import nengo

model = nengo.Network()
with model:
    stim_a = nengo.Node(0)
    a = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim_a, a)

    b = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(b, b, synapse=0.1)
    nengo.Connection(a, b, transform=0.1)