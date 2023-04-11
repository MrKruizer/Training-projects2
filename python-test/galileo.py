from matplotlib import pyplot as plt


speed_fall = -9.81

def ball_trajectory(x, sX, sY):
	location = sY/sX*x+speed_fall*(x**2)/(2*(sX**2))
	return location;

def main():
	_leng = input('Type leng of testing pool in metrical system: ')
	_sx = input('Type Horizontal speed of ball: ')
	_sy = input('Type vertical speed of ball: ')
	if (!str.isnumeric(_leng) || !str.isnumeric(_sx) || !str.isnumeric(_sy)):
		print('Uncorrect input data')
		return
	leng = float(_leng)
	sX = float(_sx)
	sY = float(_sy)
	xs = [x/100 for x in list(range(int(leng * 100)+1))]
	ys = [ball_trajectory(x,sX,sY) for x in xs]
	plt.plot(xs,ys)
	plt.title('The trajectory of a thrown ball')
	plt.xlabel('Horizontal position of ball')
	plt.ylabel('Vertical position of ball')
	plt.axhline(y=0)
	plt.show()

main()