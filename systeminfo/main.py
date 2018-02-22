import shutil
import platform

def get_platform():	
	x="The platform is: "
	y= platform.platform()
	return x, y
if __name__ == '__main__':
	get_platform()
