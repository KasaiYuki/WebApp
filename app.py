from flask import Flask, render_template, request
import WolframAlpha


app = Flask(__name__)


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
#mapping for /hello
@app.route('/hello')
def hello():
    myName = "Shreyas"
    return ("Hello " + myName)

#mapping for myprofile
@app.route('/myprofile')
def showMyProfile():
    return render_template('MyProfile.html')


#mapping for myprofile
@app.route('/addprofileform')
def addprofileform():
    return render_template('MyProfileForm.html')



#mapping for /addprofile
@app.route('/addprofile')
def addprofile():
    myName = request.args.get('myname') #name parameter in MyProfileForm
    state_of_residence = request.args.get('state_of_residence')
    favorite_subject = request.args.get('favorite_subject')
    return render_template('MyProfile.html', html_myname = myName, html_state_of_residence = state_of_residence, html_fav_subject = favorite_subject)

if __name__ == '__main__':
    app.run()
