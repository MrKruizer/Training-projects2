from matplotlib import pyplot as plt

speed_fall = -9.81

def ball_trajectory(x, sX, sY):
	location = sY/sX*x+speed_fall*(x**2)/(2*(sX**2))
	return location;

def main():
	leng = float(input('Type leng of testing pool in metrical system: '))
	sX = float(input('Type Horizontal speed of ball: '))
	sY = float(input('Type vertical speed of ball: '))
	xs = [x/100 for x in list(range(int(leng * 100)+1))]
	ys = [ball_trajectory(x,sX,sY) for x in xs]
	plt.plot(xs,ys)
	plt.title('The trajectory of a thrown ball')
	plt.xlabel('Horizontal position of ball')
	plt.ylabel('Vertical position of ball')
	plt.axhline(y=0)
	plt.show()

main()