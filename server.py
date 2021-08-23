from flask import render_template
from flask import request
import logic as dbLogic
import connexion

app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure api endpoints
app.add_api('swagger.yml')

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		dbLogic.insertUser(username, password)
	return render_template('home.html', generated_key=dbLogic.generated_key)

@app.route('/docs/')
def docs():
    return render_template('docs.html')

# If in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
