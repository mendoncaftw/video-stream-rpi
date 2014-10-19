from flask import Flask, render_template

app=Flask(__name__)

@app.route("/jwplayer")
def jwplayer():
	return render_template('jwplayer.html')

@app.route("/strobemediaplayer")
def strobemediaplayer():
	return render_template('strobemediaplayer.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
