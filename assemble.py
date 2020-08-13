#!/usr/bin/env python3

from zencad import *

from room2 import Room
from rotplate import RotationPlate
from connection_cylinder import ConnectionCylinder
from topcylinder import TopCylinder
from arm import Arm
from camerabody import CameraRoom


if __name__ == "__main__":
	room = Room()
	plate = RotationPlate()
	concyl = ConnectionCylinder()
	topcylinder = TopCylinder()
	arm0 = Arm()
	arm1 = Arm()
	camera = CameraRoom()

	concyl.set_color(0,1,0,0)

	topcylinder.rotateZ(deg(90))

	room.socket.link(plate)
	plate.socket.link(concyl)
	concyl.socket.link(topcylinder)

	topcylinder.socket0.link(arm0)
	topcylinder.socket1.link(arm1)


	camera.up(90)
	disp(camera)
	disp(room)
	#room.location_update()

	#disp(RoomAssemble())
	show()