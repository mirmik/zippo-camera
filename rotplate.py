#!/usr/bin/env python3

from zencad import *
from globals import *

class RotationPlate(zencad.assemble.unit):
	def __init__(self):
		super().__init__()
		self.add(self.model())

	def model(
			self,
			border_h=4
		):
		t = T
		r = ROOF_R
		spike_r1 = SPIKE_R1
		spike_r2 = SPIKE_R2
		border_t = BORDER_T
		spike_n = SPIKE_N
		light_r = LIGHT_R

		stub_size = (5,2,2)
		stub_r = 23
	
		
		base = cylinder(r=r, h=t)
		border = cylinder(r=r+border_t, h=border_h+t) - cylinder(r=r, h=border_h+t) 
		spikes = rotate_array(spike_n)(sphere(r=spike_r1).up(t).left(spike_r2)) - halfspace()
		stub = box(stub_size, center=True).up(t+stub_size[2]/2).left(stub_r)
	
		motor_hole = cylinder(r=6, h=t)
		light_hole = LIGHT_HOLES
	
		conic = cone(r1=r, r2=r+10, h=10).up(t+spike_r1)

		self.socket = zencad.assemble.unit(parent=self, location=moveZ(spike_r1+T))

		return unify(
			base
			+ border
			+ spikes
			+ stub
	
			- motor_hole
			- light_hole
			- cables_hole().rotZ(deg(180))
			- NUT_HOLE1
			- conic
		)

if __name__ == "__main__":
	rotplate = RotationPlate()
	disp(rotplate)
	show()