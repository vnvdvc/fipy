__docformat__ = 'restructuredtext'

from matplotlibViewer import MatplotlibViewer

def make(vars, title = None, limits = None):
    """
    Generic function for creating a `MatplotlibViewer`. The `make` function
    will search the module tree and return an instance of the first
    `MatplotlibViewer` it finds of the correct dimension.
    
    :Parameters:

      - `vars`: a `CellVariable` or tuple of `CellVariable` objects to plot
      - `limits`: a dictionary with possible keys `'xmin'`, `'xmax'`,
        `'ymin'`, `'ymax'`, `'zmin'`, `'zmax'`, `'datamin'`, `'datamax'`.
        A 1D Viewer will only use `'xmin'` and `'xmax'`, a 2D viewer
        will also use `'ymin'` and `'ymax'`, and so on.
        All viewers will use `'datamin'` and `'datamax'`.
        Any limit set to a (default) value of `None` will autoscale.
      - `title`: displayed at the top of the Viewer window

    """
    if type(vars) not in [type([]), type(())]:
        vars = [vars]
        
    from fipy.viewers import MeshDimensionError
    
    try:
        from matplotlib1DViewer import Matplotlib1DViewer
        return Matplotlib1DViewer(vars = vars, title = title, limits = limits)
    except MeshDimensionError:
        try:
            from matplotlib2DViewer import Matplotlib2DViewer
            return Matplotlib2DViewer(vars = vars, title = title, limits = limits)
        except MeshDimensionError:
            from matplotlibVectorViewer import MatplotlibVectorViewer
            return MatplotlibVectorViewer(vars = vars, title = title)
