from graphviz import Digraph

def draw_all(G, glob_attrs = {}):
    dot = Digraph(node_attr={'fontsize': glob_attrs.get('fontsize', '20')})
    dot.attr(rankdir=glob_attrs.get('rankdir', 'LR'))
    dot.edge_attr.update(pen_width=glob_attrs.get('pen_width', '4'))
    dot.attr(ranksep=glob_attrs.get('ranksep', '0.1'), nodesep=glob_attrs.get('nodesep', '0.2'))

    # nodes
    for n, d in G.nodes(data=True):
        group = d['group']
        shape = {'state': 'ellipse', 'param': 'square', 'none': 'ellipse', 'func': 'ellipse'}[group]
        color = {'state': '#8df2b2ff:transparent', 'param': '#8de9f2ff:transparent', 'none': 'black', 'func': 'black'}[group]
        attrs = {'label': d['label'], 'shape': shape, 'fillcolor': color, 'style': 'filled'}
        if group == 'none' or group == 'func':
            attrs['label'] = ''
            attrs['width'] = '0.1'
            attrs['height'] = '0.1'
        dot.node(str(n), **attrs)

    color_cycle = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'] # Matplotlib default cycler.
    for eidx, (u, v) in enumerate(G.edges()):
        dot.edge(str(u), str(v), color = color_cycle[eidx % len(color_cycle)])

    return dot
