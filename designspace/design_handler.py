import os
import plotly
import numpy as np
from stl import mesh
import plotly.graph_objects as go

def stl2mesh3d(stl_mesh):
    # stl_mesh is read by nympy-stl from a stl file; it is  an array of faces/triangles (i.e. three 3d points) 
    # this function extracts the unique vertices and the lists I, J, K to define a Plotly mesh3d
    p, q, r = stl_mesh.vectors.shape #(p, 3, 3)
    # the array stl_mesh.vectors.reshape(p*q, r) can contain multiple copies of the same vertex;
    # extract unique vertices from all mesh triangles
    vertices, ixr = np.unique(stl_mesh.vectors.reshape(p*q, r), return_inverse=True, axis=0)
    I = np.take(ixr, [3*k for k in range(p)])
    J = np.take(ixr, [3*k+1 for k in range(p)])
    K = np.take(ixr, [3*k+2 for k in range(p)])
    return vertices, I, J, K

def plot_mesh(p):
    design_mesh = mesh.Mesh.from_file(p)
    vertices, I, J, K = stl2mesh3d(design_mesh)
    x, y, z = vertices.T
    mesh3D = go.Mesh3d(x=x,
                y=y,
                z=z, 
                i=I, 
                j=J, 
                k=K, 
                flatshading=True,
                intensity=z, 
                name='BigMac',
                showscale=False)

    title = "Mesh3d from a STL file"
    fig = go.Figure(data=[mesh3D])
    #plotly.offline.plot(fig)
    div = plotly.offline.plot(fig, auto_open=False, output_type='div')
    return div
