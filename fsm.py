"""
	FSMsim - Finite State Machine simulation
	Copyright (c) 2016 Naveen Venkat
	Email: nav.naveenvenkat@gmail.com
"""

def fsmNone():
	return
"""
class fsm(object):

	ltable = {} #{oldState:[[input, newState, output]]}
	#Lookup Table has all the mappings
	#TODO: optimize this

	def __init__(self, st = None):
		self.state = st

	def set(self, st=None):
		self.state = st

	def add(self, oldState=None, inp=None, newState=None, output=None):
		self.ltable[oldState] = []
		self.ltable[oldState].append([inp, newState, output])

	def sim(self, inp):
		t = None
		for i in self.ltable[self.state]:
			if i[0] == inp:
				print str(self.state), "---(" + str(inp) + "/" + str(i[2]) + ")-->", str(i[1])
				self.state = i[1]
				t = i[2]
		return t

	def __repr__(self):
		return str(self.state)

f = fsm("halt")
f.add("halt", 1, "run", 1)
f.sim(1)
print f
"""