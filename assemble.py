#!/usr/bin/env python3

from zencad import *

from room2 import Room
from rotplate import RotationPlate
from connection_cylinder import ConnectionCylinder


if __name__ == "__main__":
	room = Room()
	plate = RotationPlate()
	concyl = ConnectionCylinder()

	room.socket.link(plate)
	plate.socket.link(concyl)

	disp(room)
	#room.location_update()

	#disp(RoomAssemble())
	show()