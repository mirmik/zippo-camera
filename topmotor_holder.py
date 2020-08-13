#!/usr/bin/env python3

from zencad import *
from globals import *

class TopMotorHolder(zencad.assemble.unit):
	H = 3

	def __init__(self):
		super().__init__()
		m = self.model()

		
		self.relocate(move(-15,5,12+8) * rotateX(deg(90)))
		self.add(m)
		
		
	def model(self):
		m = cylinder(r=28/2+T, h=self.H) 
		m += widewire(segment((-21+3,0,0), (21-3,0,0)), 3.5+T).extrude(self.H)
		m += box(15+2*T, 17+T, self.H).movX(-15/2-T)

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
		#m = unify(m)

		m = m.rotZ(deg(45))

		h1 = self.holder().rotZ(deg(0)).move(point3(-20.5,-12))
		h2 = self.holder().rotZ(deg(0)).move(point3(15,-12))

		m += h1
		m += h2

		m += (polygon([
			point3(18,12),
			point3(19,-12),
			point3(11,-19),
			point3(10,-12),
			point3(12,0),
			point3(12,5)
		]).extrude(T))

		return m

	def holder(self):
		H = 8
		B = 8
		W = 8

		t = 1

		stif = polygon([
			(0,0),
			(H-T, 0),
			(0, B-T),
		]).extrude(t,center=True)

		stif = stif.rotateY(deg(-90)).up(T).forw(T)

		base = box(W,B,T).movX(-W/2)
		base2 = box(W,H,T).rotX(deg(90)).movY(T).movX(-W/2)
		
		m = (base + base2 
			+ stif.movX(W/2 - t/2)
			+ stif.movX(-W/2 + t/2)
		).movY(-B)

		m -= cylinder(r=2, h=1000, center=True).rotX(deg(90)).up(H/2 + T/2)

		return m

if __name__ == "__main__":
	module = TopMotorHolder()
	disp(module)
	to_stl(module.model(), "topmotor_holder.stl", delta=0.1)
	show()