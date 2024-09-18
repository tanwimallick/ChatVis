from paraview.simple import *

# read the input data
points = IOSSReader(registrationName='can_points.ex2', FileName=['/Users/tpeterka/collaborations/tanwi/examples/points-surf-clip/can_points.ex2'])

# create a Delaunay triangulation
delaunay3D = Delaunay3D(registrationName='Delaunay3D', Input=points)

# create a new clip filter
clip = Clip(registrationName='Clip', Input=delaunay3D)
clip.ClipType = 'Plane'
clip.ClipType.Origin = [0.0, 0.0, 0.0]
clip.ClipType.Normal = [1.0, 0.0, 0.0]

# create new render view
renderView = CreateView('RenderView')
renderView.ViewSize = [1920, 1080]
renderView.CameraPosition = [16.032772458378666, 21.232772267643792, 11.132772839848393]
renderView.CameraFocalPoint = [-2.5999999046325684, 2.5999999046325635, -7.499999523162842]
renderView.CameraViewUp = [-0.40824829046386296, 0.8164965809277263, -0.40824829046386285]

# create new layout object
layout = CreateLayout(name='Layout')
layout.AssignView(0, renderView)

# show data
clipDisplay = Show(clip, renderView)
clipDisplay.Representation = 'Wireframe'

# save screenshot (change path for your machine)
SaveScreenshot('/Users/tpeterka/collaborations/tanwi/examples/points-surf-clip/points-surf-clip-screenshot.png', renderView, ImageResolution=[1920, 1080])


