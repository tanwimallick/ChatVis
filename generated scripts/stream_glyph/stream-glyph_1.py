from paraview.simple import *

# Reading the disk.ex2 file
reader = ExodusIIReader(FileName='/Users/tanwimallick/Documents/Paraview/generated_code/disk.ex2')
reader.UpdatePipeline() 

# Tracing streamlines of the V data array seeded from a default point cloud
streamTracer = StreamTracer(registrationName='StreamTracer1', Input=reader, SeedType='Point Cloud')
#streamTracer.Vectors = ['POINTS', 'V']

# Rendering the streamlines with tubes for better visibility
tube = Tube(registrationName='Tube1', Input=streamTracer)
tube.Radius = 0.075

# Adding cone glyphs to the streamlines to indicate direction
glyph = Glyph(registrationName='Glyph1', Input=streamTracer, GlyphType='Cone')
glyph.OrientationArray = ['POINTS', 'V']
glyph.ScaleArray = ['POINTS', 'V']
glyph.ScaleFactor = 0.05

# Create a new view and set its properties
renderView = CreateView('RenderView')
renderView.ViewSize = [1920, 1080]

# Create a new layout object
layout = CreateLayout(name='Layout')
layout.AssignView(0, renderView)

# Coloring both the streamlines and glyphs using the Temp data array
tubeDisplay = Show(tube, renderView)
glyphDisplay = Show(glyph, renderView)
ColorBy(tubeDisplay, ('POINTS', 'Temp'))
ColorBy(glyphDisplay, ('POINTS', 'Temp'))
tubeDisplay.RescaleTransferFunctionToDataRange(True)
glyphDisplay.RescaleTransferFunctionToDataRange(True)

# Orienting the view to look from the +X direction
renderView.ResetActiveCameraToPositiveX()
renderView.ResetCamera()

# Save a screenshot of the render view
SaveScreenshot('/Users/tanwimallick/Documents/Paraview/generated_code/stream-glyph-screenshot.png', renderView, ImageResolution=[1920, 1080], OverrideColorPalette='WhiteBackground')