from paraview.simple import *

# read the input data
ml100vtk = LegacyVTKReader(FileNames=['/Users/tanwimallick/Documents/Paraview/generated_code/ml-100.vtk'])

# create a new slice in a plane parallel to the y-z plane at x=0
slice1 = Slice(registrationName='Slice1', Input=ml100vtk)
slice1.SliceType = 'Plane'
slice1.SliceType.Origin = [0.0, 0.0, 0.0]
slice1.SliceType.Normal = [1.0, 0.0, 0.0]
slice1.SliceOffsetValues = [0.0]
slice1.PointMergeMethod = 'Uniform Binning'

# create a new contour on the slice at the 0.5 value
contour1 = Contour(registrationName='Contour1', Input=slice1)
contour1.ContourBy = ['POINTS', 'var0']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'

# create a render view
renderView = CreateView('RenderView')
renderView.ViewSize = [1920, 1080]

# show the contour data in red color
contour1Display = Show(contour1, renderView)
contour1Display.ColorArrayName = ['POINTS', '']
contour1Display.DiffuseColor = [1.0, 0.0, 0.0]

# set render view direction to +x
renderView.ResetActiveCameraToPositiveX()
renderView.ResetCamera()

# create new layout object and assign the render view
layout = CreateLayout(name='Layout')
layout.AssignView(0, renderView)

# save a screenshot of the render view with the specified resolution
SaveScreenshot('/Users/tanwimallick/Documents/Paraview/generated_code/ml-slice-iso-screenshot.png', renderView, ImageResolution=[1920, 1080], OverrideColorPalette='WhiteBackground')