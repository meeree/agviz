# Example: render the hidden states of a RNN for 5 timesteps, visualizing parameters and states. Also, play with "full" rendering, where we show all the intermediate functions.
import torch
from agviz import render

def eval_to_list(cell, inp):
    states = []
    h = None
    for x in inp.swapaxes(0,1):
        states.append(cell(x, h))
        h = states[-1]
    return states

if __name__ == '__main__':
    inputs = torch.randn((10, 5, 3)) # (batches, time, input dim).
    cell = torch.nn.RNNCell(3, 100) # 3 = inp dim, 100 = hidden dim.
    hjs = eval_to_list(cell, inputs)
    render(hjs[-1].sum(), {
            **{f'hidden[{j+1}]': (hj, 'state') for j, hj in enumerate(hjs)},                # State of GRU 
            **{name: (param, 'param') for name, param in cell.named_parameters()}  # GRU params
            },
            'example_ag_viz',
            fmt = 'png',
            penwidth = '10',
            color_edges = False,
            simplify = []# Don't simplify anything.
    )
