from matplotlib import rc
from daft import daft

rc("font", family="serif", size=12)
rc("text", usetex=True)

pgm = daft.PGM([2.2, 1.6], origin=[1.4, 0.7])

# Nodes
pgm.add_node(daft.Node("counts", r"$x$", 2.5, 1, observed=True))
pgm.add_node(daft.Node("alpha", r"$\alpha$", 3, 2))
pgm.add_node(daft.Node("beta", r"$\beta$", 2, 2))

# Edges
pgm.add_edge("alpha", "counts")
pgm.add_edge("beta", "counts")

pgm.render()
pgm.figure.savefig("shifted_beta_geometric_marginalized.pdf")


