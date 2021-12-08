import os
import pybullet as p
import pybullet_data
import time
import v2_1 as nn 

# 连接物理引擎
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.resetSimulation()

# 重力
p.setGravity(0, 0, -10)

# 实时仿真
useRealTimeSim = 1
p.setRealTimeSimulation(useRealTimeSim)

# 加载地面
p.loadURDF("plane.urdf")
#p.loadSDF("stadium.sdf")

# 加载小测
car = p.loadURDF("racecar/racecar.urdf")

inactive_wheels = [3, 5, 7]
wheels = [2]

# 转向轮
steering = [4, 6]

for wheel in inactive_wheels:
    p.setJointMotorControl2(car, wheel, p.VELOCITY_CONTROL, targetVelocity=0, force=0)


# 自定义参数滑块，分别为速度，转向，驱动力
vParam = p.addUserDebugParameter("force neuron", 0, 10, 10)
leftParam = p.addUserDebugParameter("left steer neuron", 0, 10, 10)
rightParam = p.addUserDebugParameter("right steer neuron", 0, 10, 10)

nn.start()

# 开始仿真
while 1:
	# 读取速度，转向角度，驱动力参数
    v = p.readUserDebugParameter(vParam) / 10.
    left = p.readUserDebugParameter(leftParam) / 10.
    right = p.readUserDebugParameter(rightParam) / 10.

    nn.active(100, v, 1)
    nn.active(200, left, 1)
    nn.active(300, right, 1)

    # 三个输出端，每个受一个神经元控制
    targetVelocity = 10 * nn.world.get_neuron_value(120)
    leftSteerAngle = 0.5 * nn.world.get_neuron_value(220)
    rightSteerAngle = 0.5 * nn.world.get_neuron_value(320)

    steeringAngle = leftSteerAngle - rightSteerAngle
    
	# 根据上面读取到的值对关机进行设置
    for wheel in wheels:
        p.setJointMotorControl2(car,
                                wheel,
                                p.VELOCITY_CONTROL,
                                targetVelocity=targetVelocity,
                                force=10)

    for steer in steering:
        p.setJointMotorControl2(car, steer, p.POSITION_CONTROL, targetPosition=steeringAngle)

    location, _ = p.getBasePositionAndOrientation(car)
    p.resetDebugVisualizerCamera(
        cameraDistance=3,
        cameraYaw=110,
        cameraPitch=-30,
        cameraTargetPosition=location
    )

    if useRealTimeSim == 0:
        p.stepSimulation()
    time.sleep(1/240.)


