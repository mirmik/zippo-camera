#!/usr/bin/env python3

from zencad import *

from room2 import Room
from rotplate import RotationPlate
from connection_cylinder import ConnectionCylinder
from topcylinder import TopCylinder


if __name__ == "__main__":
	room = Room()
	plate = RotationPlate()
	concyl = ConnectionCylinder()
	topcylinder = TopCylinder()

	concyl.set_color(0,1,0,0)

	room.socket.link(plate)
	plate.socket.link(concyl)
	concyl.socket.link(topcylinder)

	disp(room)
	#room.location_update()

	#disp(RoomAssemble())
	show()