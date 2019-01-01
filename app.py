from flask import Flask, render_template, request
import phalculator
import WolframAlpha
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
#bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/wolframAsk')
def wolframAsk():

    return render_template('wolframAsk.html')

@app.route('/wolfram')
def wolfram():
    response = WolframAlpha.getResponse(request.args.get('response'))
    return(render_template('wolfram.html', html_response = response))

@app.route('/phalculatorAsk')
def phalculatorAsk():
    return(render_template('phalculatorAsk.html'))


@app.route('/dPos', methods=['GET'])
def dPos():
    return(render_template('dPos.html'))


@app.route('/dPos', methods=['GET', 'POST'])
def dPosA():
    time = int(request.form['time'])
    accel = int(request.form['accel'])
    iVel = int(request.form['iVel'])
    return(render_template('dPos.html', filled = 'true', answer = phalculator.dPos(time, accel, iVel)))

#mapping for myprofile
@app.route('/addprofileform')
def addprofileform():
    return render_template('MyProfileForm.html')



#mapping for /addprofile
@app.route('/addprofile')
def addprofile():
    return render_template('MyProfile.html', html_myname = request.args.get('myname'), html_state_of_residence = request.args.get('state_of_residence'), html_fav_subject = request.args.get('favorite_subject'))

if __name__ == '__main__':
    app.run()
