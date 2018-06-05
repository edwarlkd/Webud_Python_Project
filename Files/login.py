from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
	return 'welcome %s' % name


@app.route('/fail')
def fail():
	return 'User ID and Password are not a match.'
		
	
	
	
@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		userID = request.form['user_id']
		userPSWD = request.form['user_pswd']
		if userPSWD == 'guest'
			return redirect(url_for('success', name = userID))
	else:
		flash('Incorrect ID or Password')
	
	
		
if __name__ == 'login':
	app.run(debug = True)

	
	
