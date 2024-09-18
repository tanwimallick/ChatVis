from paraview.simple import *

# read the input data
velocity = IOSSReader(registrationName='disk.ex2', FileName=['/Users/tpeterka/collaborations/tanwi/examples/stream-glyph/disk.ex2'])
velocity.UpdatePipeline()           # pipeline needs to be updated before bounds are computed, probably doesn't hurt to update always

# get data range
bounds = velocity.GetDataInformation().GetBounds()
length = [bounds[1] - bounds[0], bounds[3] - bounds[2], bounds[5] - bounds[4]]

# create a new stream tacer
streamTracer = StreamTracer(registrationName='StreamTracer1', Input=velocity, SeedType='Point Cloud')
streamTracer.Vectors = ['POINTS', 'V']
streamTracer.MaximumStreamlineLength = 20.15999984741211
streamTracer.SeedType.Center = [0.0, 0.0, 0.07999992370605469]
streamTracer.SeedType.Radius = 2.015999984741211

# create a new glyph
glyph = Glyph(registrationName='Glyph1', Input=streamTracer, GlyphType='Cone')
glyph.OrientationArray = ['POINTS', 'V']
glyph.ScaleArray = ['POINTS', 'V']
glyph.ScaleFactor = 0.05957118125724144
glyph.GlyphTransform = 'Transform2'

# create a new tube
tube = Tube(registrationName='Tube1', Input=streamTracer)
tube.Scalars = ['POINTS', 'AngularVelocity']
tube.Vectors = ['POINTS', 'Normals']
tube.Radius = 0.0752525282476563

# create new render view
renderView = CreateView('RenderView')
renderView.ViewSize = [1920, 1080]
renderView.CameraPosition = [(bounds[0] + bounds[1]) / 2.0 - 1.5 * max(length[1], length[2]), (bounds[2] + bounds[3]) / 2.0, (bounds[4] + bounds[5]) / 2.0]
renderView.CameraFocalPoint = [(bounds[0] + bounds[1]) / 2.0, (bounds[2] + bounds[3]) / 2.0, (bounds[4] + bounds[5]) / 2.0]
renderView.CameraViewUp = [0.0, 0.0, 1.0]

# create new layout object
layout = CreateLayout(name='Layout')
layout.AssignView(0, renderView)

# show data from both tube and glyph
tubeDisplay = Show(tube, renderView)
glyphDisplay = Show(glyph, renderView)

# color tubes and glyphs by Temp variable
ColorBy(tubeDisplay, ('POINTS', 'Temp'))
ColorBy(glyphDisplay, ('POINTS', 'Temp'))
tubeDisplay.RescaleTransferFunctionToDataRange(True)
glyphDisplay.RescaleTransferFunctionToDataRange(True)

# save screenshot (change path for your machine)
SaveScreenshot('/Users/tpeterka/collaborations/tanwi/examples/stream-glyph/stream-glyph-screenshot.png', renderView, ImageResolution=[1920, 1080])


