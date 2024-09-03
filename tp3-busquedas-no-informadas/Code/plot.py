import matplotlib.pyplot as plot

def whiskers(data, title, x_label, y_label, filename):
    plot.figure(figsize=(10,7))
    plot.boxplot(data, patch_artist=True)
    plot.title(title)
    plot.xlabel(x_label)
    plot.ylabel(y_label)
    plot.grid(True)
    plot.xticks([1,2,3,4,5,6,7], ["BFS", "DFS", "DLS", "UCS_e1", "UCS_e2", "A*_e1", "A*_e2"])
    plot.savefig(filename + ".png")
    
    return 0