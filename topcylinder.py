#!/usr/bin/env python3

from zencad import *
from globals import *

class TopCylinder(zencad.assemble.unit):
	H = 15

	def __init__(self):
		super().__init__()
		self.add(self.model())

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

		m += sqrtrans()(stolb(2.5,1.5,7,self.H).move(ROOF_R-10, 0, 0).rotZ(deg(45)))

		#m += multitrans([
		#	move(0,k,h2/2),
		#	move(0,-k,h2/2),
		#])(box(w+10,1,h2,center=True))
		#m -= multitrans([
		#	move(0,ROOF_R,self.H-h/2),
		#	move(0,-ROOF_R,self.H-h/2),
		#])(box(w,100,h,center=True))

		return m


if __name__ == "__main__":
	module = TopCylinder()
	disp(module)
	show()