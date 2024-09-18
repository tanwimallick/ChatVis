from paraview.simple import *

# read the input data
ml100vtk = LegacyVTKReader(registrationName='ml-100.vtk', FileNames=['/Users/tpeterka/collaborations/tanwi/examples/ml-dvr/ml-100.vtk'])

# get range of 'var0'
source = GetActiveSource()
pd = source.PointData
min, max = pd.GetArray(0).GetRange()

# get color transfer function/color map for 'var0'
var0LUT = GetColorTransferFunction('var0')
var0LUT.RGBPoints = [min, 0.0, 0.0, 0.75, (min + max) / 2.0, 0.75, 0.75, 0.75, max, 0.75, 0.0, 0.0]

# get opacity transfer function/opacity map for 'var0'
var0PWF = GetOpacityTransferFunction('var0')
var0PWF.Points = [min, 0.0, 0.5, 0.0, (min + max) / 2.0, 0.5, 0.5, 0.0, max, 1.0, 0.5, 0.0]

# create new render view
renderView = CreateView('RenderView')
renderView.ViewSize = [1920, 1080]
renderView.CameraPosition = [3.8637033051562737, 3.8637033051562724, 3.8637033051562737]
renderView.CameraViewUp = [-0.40824829046386296, 0.8164965809277263, -0.40824829046386285]

# create new layout object
layout = CreateLayout(name='Layout')
layout.AssignView(0, renderView)

# show data
ml100vtkDisplay = Show(ml100vtk, renderView)
ml100vtkDisplay.Representation = 'Volume'
ml100vtkDisplay.ColorArrayName = ['POINTS', 'var0']
ml100vtkDisplay.LookupTable = var0LUT
ml100vtkDisplay.ScalarOpacityFunction = var0PWF

# save screenshot (change path for your machine)
SaveScreenshot('/Users/tpeterka/collaborations/tanwi/examples/ml-dvr/ml-dvr-screenshot.png', renderView, ImageResolution=[1920, 1080])


