import shutil
import platform

def get_platform():
	print("The platform is", platform.platform()) 
	total, used, free = shutil.disk_usage(__file__)
	print ('total, used, free: ', total, used, free)
	return
if __name__ == '__main__':
	get_platform()
