from paraview.simple import *

# read the input data
ml100vtk = LegacyVTKReader(registrationName='ml-100.vtk', FileNames=['/Users/tpeterka/collaborations/tanwi/examples/ml-iso/ml-100.vtk'])

# create a new contour
contour1 = Contour(registrationName='Contour1', Input=ml100vtk)
contour1.ContourBy = ['POINTS', 'var0']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'

# create new render view
renderView = CreateView('RenderView')
renderView.ViewSize = [1920, 1080]

# create new layout object
layout = CreateLayout(name='Layout')
layout.AssignView(0, renderView)

# show data
contour1Display = Show(contour1, renderView)

# save screenshot (change path for your machine)
SaveScreenshot('/Users/tpeterka/collaborations/tanwi/examples/ml-iso/ml-iso-screenshot.png', renderView, ImageResolution=[1920, 1080])


