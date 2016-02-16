from flask import Flask
from flask import render_template
from flask import request
import os
import aiml 


bot = aiml.Kernel()
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/apps', methods=['GET','POST'])
def echo():
    answer = bot.respond(request.form['text'])
    return render_template("index.html", data=answer)

if __name__ == "__main__":
	print '[+] loading bot brain'
	bot.learn('brain/brain.aiml')
	print '[+] brain loaded'
	port = int(os.getenv('PORT', 33507))
	app.run(threaded=True, debug = True, host='0.0.0.0', port=port, passthrough_errors=True)
