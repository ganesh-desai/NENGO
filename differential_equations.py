# Differential Equations

# Recurrent connections can also be used to represent differential equations.

# In this model the differential equation of a low-pass filter is implemented.

# In the low pass filter system, the output y is a smoothed version of the input x, given by
# dy/dt = x/tau - y/tau

# Tau is the time constant for the smoothing (larger = smoother)

# The model requires one input connection to compute x/tau and a recurrent connection that computes -y/tau.

# Time constant is very important as the functions are implemented by neurons.

# The resulting rule is that both connections need to get scaled by the synapse value and the recurrent connection must add the stored value back in.

# Input = (x/tau) * synapse
# Recurrent = (-y/tau) * synapse + y

# Since both functions are linear, transform can be used.

import nengo

model = nengo.Network()
with model:
    stim_x = nengo.Node(0)
    x = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim_x, x)

    y = nengo.Ensemble(n_neurons=50, dimensions=1)
    tau = 0.5
    synapse = 0.1

    def input_function(x):
        return x / tau * synapse

    def recurrent_function(y):
        return (-y / tau) * synapse + y

    nengo.Connection(x, y, synapse=synapse, function=input_function)
    nengo.Connection(y, y, synapse=synapse, function=recurrent_function)
