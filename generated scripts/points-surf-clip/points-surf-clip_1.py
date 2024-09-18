from paraview.simple import *

# Read the input data file
ex2_reader = ExodusIIReader(FileName='/Users/tanwimallick/Documents/Paraview/generated_code/can_points.ex2')

# Generate a 3D Delaunay triangulation of the dataset
delaunay3D = Delaunay3D(Input=ex2_reader)
delaunay3D.Tolerance = 0.0

# Create a clip to keep -x half and remove +x half using a y-z plane at x=0
clip = Clip(registrationName='Clip', Input=delaunay3D)
clip.ClipType = 'Plane'
clip.ClipType.Origin = [0.0, 0.0, 0.0]
clip.ClipType.Normal = [1.0, 0.0, 0.0]

# Create a new render view
renderView = CreateView('RenderView')
renderView.ViewSize = [1920, 1080]

# Display the clipped data as a wireframe
clipDisplay = Show(clip, renderView)
clipDisplay.Representation = 'Wireframe'

# Set up the render view
renderView.ResetCamera()
renderView.ApplyIsometricView()
renderView.ResetCamera()

# Create a new layout
layout = CreateLayout(name='Layout')
layout.AssignView(0, renderView)

# Save a screenshot of the render view
#SaveScreenshot('/Users/tanwimallick/Documents/Paraview/generated_code/points-surf-clip-screenshot.png', renderView, TransparentBackground=1)

SaveScreenshot('/Users/tanwimallick/Documents/Paraview/generated_code/points-surf-clip-screenshot.png',renderView, ImageResolution=[1920, 1080], OverrideColorPalette='WhiteBackground')
# Render the final view
Render()