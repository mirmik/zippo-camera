#!/usr/bin/env python3

from zencad import *
from globals import *

class Arm(zencad.assemble.unit):
	X = 16
	Y = 8
	H = 20

	Y2 = 8 * math.sqrt(2)

	def __init__(self):
		super().__init__()
		m = self.model()
		self.add(m)

	def model(self):
		m = box(100, self.X, self.Y).back(self.X/2)
		m -= box(100, self.X-2*T, self.Y-T).back(self.X/2).up(T).forw(T)

		m=m.rotateY(deg(-45))
		#m -= box(self.W-2*T, self.W-T, self.W-T, center=True).move(0,T/2,T/2).up(self.W/2)

		m -= halfspace().rotateY(deg(90))
		m -= halfspace().mirrorXY().up(self.H)

		m2 = (
			box(self.Y2, self.X, 10)
			- box(self.Y2 - T*math.sqrt(2), self.X-2*T, 10).move(0,T)
		).move(self.H-self.Y2 ,-self.X/2,self.H)

		return m + m2


if __name__ == "__main__":
	module = Arm()
	to_stl(module.model(), "arm.stl", 0.01)
	disp(module.model())
	show()