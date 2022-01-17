from app.app import app

if __name__ == "__main__":
	app.run(threaded=False, port=8000, host='0.0.0.0')