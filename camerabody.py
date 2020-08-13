#!/usr/bin/env python3

from zencad import *
from globals import *

from stereopanel import plate
from topmotor_holder import TopMotorHolder

class CameraRoom(zencad.assemble.unit):


	def __init__(self):
		super().__init__()
		m = self.model()
		self.add(m)

	def model(self):
		#m = box(100,20,30,center=True)
		p = plate(T)

		X = p.bbox().xmax - p.bbox().xmin + 2*T 
		Z = p.bbox().ymax - p.bbox().ymin + 2*T
		ZU = 15
		Y = 80

		m = box(X,Y,Z+ZU, center=True)
		m -= box(X-2*T,Y-T,Z-T+ZU, center=True).move(0,T/2,T/2)

		m = m.up(ZU/2)

		p2 = p.rotX(deg(90)).rotY(deg(180)).movY(-Y/2+T/2)
		#disp(p2, color(0,1,0,0.9))
		m -= p2.bbox().shape()
		m += p2

		m -= cylinder(r=10,h=1000, center=True).rotY(deg(90)).up(2)

		mh = (
			box(31,1,T,center=True) 
			+ box(1,15,T,center=True).moveY(7.5) 
			+ cylinder(r=2.5,h=T,center=True).moveX(31/2)
			+ cylinder(r=2.5,h=T,center=True).moveX(-31/2)
			- cylinder(r=1,h=T,center=True).moveX(31/2)
			- cylinder(r=1,h=T,center=True).moveX(-31/2)
		)

		self.socket = zencad.assemble.unit(parent=self)
		self.socket.down(Z/2-T).rotateZ(deg(-90)).forw(-9).left(40)
 
		return unify(m)

if __name__ == "__main__":
	croom = CameraRoom()
	hld = TopMotorHolder()

	croom.socket.link(hld)

	to_stl(croom.model(), "camerabody.stl",  0.01)
	disp(croom)
	show()
