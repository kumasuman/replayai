from flask import Flask, render_template,jsonify
app = Flask(__name__)
COACH=[
  {
    'id':1,
    'title':'L1 Coach',
    'location':'Banaswadi',
    'Fees':'Rs 1000'
  },
  {
    'id':2,
    'title':'L2 Coach',
    'location':'Yehlanka',
    'Fees':'Rs 2000'
  },
  {
    'id':3,
    'title':'L3 Coach',
    'location':'HRBR',
    #'Fees':'Rs 3000',
  },
  {
    'id':4,
    'title':'L4 Coach',
    'location':'OMBR',
    'Fees':'Rs 5000',
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html',coach=COACH,sports='BADMINTON')
	
@app.route("/coaches")
def list_coaches():
	return jsonify(COACH)
	

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True) 