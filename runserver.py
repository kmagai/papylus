import os
from papylus import app

def runserver():
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
	runserver()
