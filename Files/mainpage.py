from flask import Flask, render_template
app = Flask(__name__)

# URL "/hello" is bound to the hello_world() function
@app.route('/hello')
def hello_world():
	return 'Hello World'
	
# ? Would this override the above? => It should
@app.route('/hello/<name>')
def hello_world(name):
	if name == 'Edward' or name == 'Andrew':
		return 'Your majesty! Hail %s' % name
	else:
		return 'Hi %s' % name

	
@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		userID = request.form['user_id']
		return 
	elif request.method == 'GET':
		userID = request.args.get('user_id')
		return redirect(url_for('hello_world', name = userID)
	else:
		return redirect(url_for('hello_world', name = ' ')
	

	
if __name__ == '__main__':
	app.run(debug = True)
	
	
	