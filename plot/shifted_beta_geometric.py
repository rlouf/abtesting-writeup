from matplotlib import rc
from daft import daft

rc("font", family="serif", size=12)
rc("text", usetex=True)

pgm = daft.PGM([2.2, 2.6], origin=[1.4, 0.7])

# Nodes
pgm.add_node(daft.Node("counts", r"$x$", 2.5, 1, observed=True))
pgm.add_node(daft.Node("jump_proba", r"$\theta_i$", 2.5, 2))
pgm.add_node(daft.Node("alpha", r"$\alpha$", 3, 3))
pgm.add_node(daft.Node("beta", r"$\beta$", 2, 3))

# Edges
pgm.add_edge("jump_proba", "counts")
pgm.add_edge("alpha", "jump_proba")
pgm.add_edge("beta", "jump_proba")

# Plaque
pgm.add_plate(daft.Plate([1.5, 1.5, 2, 1], label=r"user $i$",
    shift=0.1))

pgm.render()
pgm.figure.savefig("shifted_beta_geometric.pdf")


