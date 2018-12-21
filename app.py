from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')
#mapping for /hello
@app.route('/hello')
def hello():
    myName = "Shreyas"
    return ("Hello " + myName)

#mapping for myprofile
@app.route('/myprofile')
def showMyProfile():
    return render_template('MyProfile.html')

#mapping for myprofile2
@app.route('/myprofile2')
def showMyProfile2():
    return render_template('MyProfile2.html')

#mapping for myprofile
@app.route('/addprofileform')
def addprofileform():
    return render_template('MyProfileForm.html')

#mapping for myprofile2
@app.route('/addprofileform2')
def addprofform2():
    return render_template('MyProfileForm2.html')

#mapping for /addprofile
@app.route('/addprofile')
def addprofile():
    myName = request.args.get('myname') #name parameter in MyProfileForm
    state_of_residence = request.args.get('state_of_residence')
    favorite_subject = request.args.get('favorite_subject')
    return render_template('MyProfile.html', html_myname = myName, html_state_of_residence = state_of_residence, html_fav_subject = favorite_subject)

#mapping for /addprofile2
@app.route('/addprofile2')
def addprofile2():
    myName = request.args.get('myname') #name parameter in MyProfileForm
    degree = request.args.get('degree')
    return render_template('MyProfile2.html', html_myname = myName, html_degree = degree)
if __name__ == '__main__':
    app.run()
