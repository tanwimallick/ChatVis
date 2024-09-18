from paraview.simple import *

# read the input data
ml100vtk = LegacyVTKReader(FileNames='/Users/tanwimallick/Documents/Paraview/generated_code/ml-100.vtk')

# create a new contour for isosurface
contour1 = Contour(registrationName='Contour1', Input=ml100vtk)
contour1.ContourBy = ['POINTS', 'var0']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'

# Create render view
renderView = CreateView('RenderView')
renderView.ViewSize = [1920, 1080]

# create new layout object
layout = CreateLayout(name='Layout')
layout.AssignView(0, renderView)

# show the contour in the render view
contour1Display = Show(contour1, renderView)
contour1Display.ColorArrayName = ['POINTS', 'var0']

# Reset and fit camera to ensure all objects are visible
renderView.ResetCamera()

# Save a screenshot of the render view
SaveScreenshot('/Users/tanwimallick/Documents/Paraview/generated_code/ml-iso-screenshot.png', renderView, ImageResolution=[1920, 1080], OverrideColorPalette='WhiteBackground')