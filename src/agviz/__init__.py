from . import drawing

def render(out, named_tensors, filename, draw_fn = drawing.draw_all, fmt = 'pdf', **draw_kwargs):
    G = None
    if 'torch' in str(type(out)):
        from .make_graph import traverse_torch
        G = traverse_torch(out, named_tensors)
    else:
        print('Unsupported type. Supported AG libraries: [pytorch, ]')

    if G is None:
        raise Exception('Failed to produce networkx graph from autograd data. See errors above.')

    dot = draw_fn(G, **draw_kwargs)
    dot.format = fmt 
    dot.render(filename, cleanup=True)
