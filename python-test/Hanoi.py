import re


layer = ' {t1}   {t2}   {t3}'
regex = '\d to \d'
sections = []

class section:
	def __init__(self, w, t, n):
		self.__weight = w
		self.__tower = t
		self.__number = n
		self.__number_in_tower = n
	
	@property
	def weight(self):
		return self.__weight
	@property
	def tower(self):
		return self.__tower
	@property
	def number(self):
		return self.__number
	@property
	def number_in_tower(self):
		return self.__number_in_tower
	@property
	def draw(self):
		return f"{self.number}/{self.weight}"

	def rearrange(self, t):
		if (t <= 0 or t >3):
			raise Exception('Incorrect tower number')
		if t == self.__tower:
			raise Exception('Original number tower equal new')
		out_tower_sections = [s for s in sections if s.__tower == self.__tower]
		if len(out_tower_sections) == 0:
			raise Exception('Not found sections in origin tower')
		if any(s.weight < self.__weight for s in out_tower_sections):
			raise Exception('Origin tower have section with less weight')
		on_tower_sections = [s for s in sections if s.__tower == t]
		if len(on_tower_sections) == 0:
			self.__tower = t
			self.__number_in_tower = 1
			draw()
			return
		if not any(s.__weight <= self.__weight for s in on_tower_sections):
			self.__tower = t
			self.__number_in_tower = len(on_tower_sections)+1
			draw()
			return
		raise Exception('Target tower have section with less weight')


def play():
	while True:
		i = input();
		if len(i) == 0:
			continue
		i = i.strip().lower()
		if i == 'quit':
			break
		elif i == 'auto':
			generate_tower()
			draw()
			auto(1,3)
		else:
			if re.fullmatch(regex, i):
				vals = i.split(' ')
				if str.isnumeric(vals[0]) and str.isnumeric(vals[2]):
					if ( vals[0] > 5 ):
						print('Number of section out of range')
					elif (vals[2] > 3 or vals[2] < 1):
						print('Number of tower out of range')
					else:
						try:
							sections[val[0]-1].rearrange(vals[2])
						except Exception as e:
							print(e)
			else:
				print('Incorrect instruction. Sample: 5 to 3')



def auto(n, t):
	if n <=0 or n > len(sections):
		return 
	try:
		if sections[n-1].tower == 1 and t == 3:
			auto(n + 1, 2)
			sections[n-1].rearrange(t)
			auto(n+1, 3)
		elif sections[n-1].tower == 1 and t == 2:
			auto(n + 1, 3)
			sections[n-1].rearrange(t)
			auto(n+1, 2)
		elif sections[n-1].tower == 2 and t == 1:
			auto(n + 1, 3)
			sections[n-1].rearrange(t)
			auto(n+1, 1)
		elif sections[n-1].tower == 2 and t == 3:
			auto(n + 1, 1)
			sections[n-1].rearrange(t)
			auto(n+1, 3)
		elif sections[n-1].tower == 3 and t == 1:
			auto(n + 1, 2)
			sections[n-1].rearrange(t)
			auto(n+1, 1)
		elif sections[n-1].tower == 3 and t == 2:
			auto(n + 1, 1)
			sections[n-1].rearrange(t)
			auto(n+1, 2)
	except Exception as e:
		print(e)


def draw():
	for i in range(len(sections)):
		lt = layer
		l = [ s for s in sections if s.number_in_tower == 5-i]
		if any(s.tower == 1 for s in l):
			lt = lt.replace('{t1}', next(s for s in l if s.tower == 1).draw)
		else:
			lt = lt.replace('{t1}', '|')
		if any(s.tower == 2 for s in l ):
			lt = lt.replace('{t2}', next(s for s in l if s.tower == 2).draw)
		else:
			lt = lt.replace('{t2}', '|')
		if any(s.tower == 3 for s in l ):
			lt = lt.replace('{t3}',  next(s for s in l if s.tower == 3).draw)
		else:
			lt = lt.replace('{t3}', '|')
		print(lt)

def generate_tower():
	sections.clear()
	for i in range(5):
		sections.append(section(5-i,1,i+1))

def main():
	generate_tower()
	draw()
	play()
	print('End')
main()