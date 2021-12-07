import pybullet as p
import time
import pybullet_data

# client connect to physics simulation, and sends command to physics server.
client = p.connect(p.GUI) # GUI/DIRECT are physics sumulation servers.
dataPath = pybullet_data.getDataPath()
print(dataPath)
p.setAdditionalSearchPath(dataPath) # set 3d model file searching path

p.setGravity(0,0,-10) # by default there is no gravity

planeId = p.loadURDF("plane.urdf") # Universal Robot Description File

startPos = [ 0, 0, 1 ]
startOrientation = p.getQuaternionFromEuler([ 0, 0, 0 ])
boxId = p.loadURDF("r2d2.urdf", startPos, startOrientation)

p.resetBasePositionAndOrientation(boxId, startPos, startOrientation) # set pos and ori

for i in range(0, 10000):
    p.stepSimulation()
    time.sleep(1./240.) # 240fps

cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos, cubeOrn)
p.disconnect()
