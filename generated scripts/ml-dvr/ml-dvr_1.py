from paraview.simple import *

# read the input data from the VTK file
ml100vtk = LegacyVTKReader(FileNames=['/Users/tanwimallick/Documents/Paraview/generated_code/ml-100.vtk'])

# create a render view
renderView = CreateView('RenderView')
renderView.ViewSize = [1920, 1080]

# Create a new layout and assign the view
layout = CreateLayout(name='Layout')
layout.AssignView(0, renderView)

# create a volume render of the VTK data
volume1 = Show(ml100vtk, renderView)
volume1Display = GetDisplayProperties(ml100vtk, view=renderView)
volume1Display.SetRepresentationType('Volume')

# Apply the isometric view to properly visualize the volume
renderView.ApplyIsometricView()
renderView.ResetCamera()

# Save a screenshot of the render view
SaveScreenshot('/Users/tanwimallick/Documents/Paraview/generated_code/ml-dvr-screenshot.png', renderView, ImageResolution=[1920, 1080], OverrideColorPalette='WhiteBackground')