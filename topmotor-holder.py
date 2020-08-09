#!/usr/bin/env python3

from zencad import *
from globals import *

class TopMotorHolder(zencad.assemble.unit):
	H = 5

	def __init__(self):
		super().__init__()
		m = self.model()
		self.add(m)
		
		
	def model(self):
		m = cylinder(r=28/2+T, h=self.H) 
		m += widewire(segment((-21+3,0,0), (21-3,0,0)), 3.5+T).extrude(self.H)
		m += box(15+2*T, 17+T, self.H).movX(-15/2-T)

		#XR = (21-3) * math.sin(deg(45))
		#p2 = rotateZ(deg(45))(point3(15/2+T - 4,17+T))
		#p3 = rotateZ(deg(45))(point3(15/2+T+8,17+T))
#
		#plg = polygon([
		#	point3(-XR, -XR-3.5-T),
		#	point3(20, -XR-3.5-T),
		#	point3(20, p3.y),				
		#	p3,
		#	p2,
		#])#.rotZ(deg(45))
#
		#eplg = plg.extrude(T)

		m -= box(15, 17, self.H).movX(-15/2).up(T)
		m -= box(6,1000,1000).move(-3,0,T)
		m -= cylinder(r=28/2, h=self.H-T).up(T) 
		m -= (box(21*2-3*2, 7, self.H, center=True).up(T+self.H/2) 
				+ cylinder(r=3.5, h=self.H-T).movX(21-3).up(T)
				+ cylinder(r=3.5, h=self.H-T).movX(-21+3).up(T)
			)
		m -= cylinder(r=2,h=T).move(21-3,0,0)
		m -= cylinder(r=2,h=T).move(-21+3,0,0)
		m -= cylinder(r=5,h=T).movY(-8)
		m = unify(m)

		#eplg = eplg.rotateZ(deg(-45))

		#eplg -= cylinder(r=2,h=T).move(21-3,0,0)
		#eplg -= cylinder(r=2,h=T).move(-21+3,0,0)
		#eplg -= cylinder(r=5,h=T).movY(-8)

		#m += hl(eplg)
		#m = m.rotZ(deg(45)) + eplg#.rotZ(deg(45))


		#hl(plg)

		return m


if __name__ == "__main__":
	module = TopMotorHolder()
	disp(module)
	to_stl(module.model(), "topmotor-holder.stl", delta=0.1)
	show()