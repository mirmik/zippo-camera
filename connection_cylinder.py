#!/usr/bin/env python3

from zencad import *
from globals import *

class ConnectionCylinder(zencad.assemble.unit):
	def __init__(self):
		super().__init__()
		self.add(self.model())

	def model(self):
		m = cylinder(ROOF_R-T, T*2)
		m -= motor_screw(3,5,3).down(T)
		m -= cylinder(h=100, r=1.1,center=True)

		#m += sqrmirror()(
		#	(cylinder(r=4,h=3) - cylinder(r=3,h=3))
		#		.move(ROOF_R-10, 0, T*2).rotZ(deg(45)) 
		#	)
		m -= sqrmirror()(
			(cylinder(r=2,h=T*2))
				.move(ROOF_R-10, 0, 0).rotZ(deg(45)) 
			)

		m -= sqrmirror()(
			(cylinder(r=4,h=T))
				.move(ROOF_R-10, 0, T).rotZ(deg(45)) 
			)

		m -= cables_hole().extrude(T*2).mirrorXZ()
		
		m = fillet(m, refs=[point3(0,5,0), point3(0,5,5)], r=1)

		m += box(5,T,2, center=True).move(28,0,-T+2/2)

		return m

if __name__ == "__main__":
	concyl = ConnectionCylinder()
	disp(concyl)
	to_stl(concyl.model(), "/home/mirmik/models/concyl.stl", delta=0.1)
	show()