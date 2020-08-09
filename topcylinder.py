#!/usr/bin/env python3

from zencad import *
from globals import *

class TopCylinder(zencad.assemble.unit):
	H = 15

	def __init__(self):
		super().__init__()
		m = self.model()
		m = m.rotateX(deg(180)).movZ(self.H)
		self.relocate(up(T))
		self.add(m)

	def model(self):
		m = cylinder(r=ROOF_R, h=self.H)
		m -= cylinder(r=ROOF_R-2*T, h=self.H-T).up(T)

		#ixk = math.sqrt(iR**2 - yk**2)

		h = self.H - 2*T
		w2 = 12
		w = w2 + T*2 + 4*2
		
		k = math.sqrt((ROOF_R)**2 - (w/2)**2)

		m = m ^ box(m.bbox().xmax-m.bbox().xmin, k*2, self.H, center=True).up(self.H/2)
		m -= box(w2, 1000, h, center=True).up(self.H-h/2)

		m -= cylinder(r=ROOF_R-T, h=T).up(self.H-T)

		m -= multitrans(
		[
			move(w2-1-T/2, 0, T+T),
			move(-w2+1+T/2, 0, T+T),
			move(w2-1-T/2, 0, 5+T+T),
			move(-w2+1+T/2, 0, 5+T+T),
		])(cylinder(r=1.9/2,h=1000, center=True).rotX(deg(90)))

		m += sqrmirror()(stolb(2.5,1.5,7,self.H).move(ROOF_R-10, 0, 0).rotZ(deg(45)))

		return m


if __name__ == "__main__":
	module = TopCylinder()
	to_stl(module.model(), "topcylinder.stl", 0.01)
	disp(module.model())
	show()