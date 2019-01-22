from flask import Flask, render_template, request
import phalculator
import WolframAlpha


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/kinematics')
def kinematics():
    return render_template('kinematics.html')


@app.route('/forces')
def forces():
    return render_template('forces.html')


@app.route('/wolframAsk')
def wolframAsk():
    return render_template('wolframAsk.html')


@app.route('/wolfram')
def wolfram():
    response = WolframAlpha.getResponse(request.args.get('response'))
    return (render_template('wolfram.html', html_response=response))


@app.route('/phalculatorAsk')
def phalculatorAsk():
    return (render_template('phalculatorAsk.html'))


@app.route('/dPos', methods=['GET'])
def dPos():
    return (render_template('dPos.html'))


@app.route('/dPos', methods=['GET', 'POST'])
def dPosA():
    time = int(request.form['time'])
    accel = int(request.form['accel'])
    iVel = int(request.form['iVel'])
    return (render_template('dPos.html', filled='true', answer=phalculator.dPos(time, accel, iVel)))


@app.route('/fVel', methods=['GET'])
def fVel():
    return (render_template('fVel.html'))


@app.route('/fVel', methods=['GET', 'POST'])
def fVelA():
    iVel = int(request.form['iVel'])
    accel = int(request.form['accel'])
    iPos = int(request.form['iPos'])
    fPos = int(request.form['fPos'])
    return (render_template('fVel.html', filled='true', answer=phalculator.fVel(iVel, accel, fPos, iPos)))


@app.route('/combineComp', methods=['GET'])
def combineComp():
    return (render_template('combineComp.html'))


@app.route('/combineComp', methods=['GET', 'POST'])
def combineCompA():
    vComp = int(request.form['vComp'])
    hComp = int(request.form['hComp'])
    return (render_template('combineComp.html', filled='true', answer1=phalculator.comp(2, vComp, hComp),
                            answer2=phalculator.comp2(2, vComp, hComp)))


@app.route('/splitVector', methods=['GET'])
def splitVector():
    return (render_template('splitVector.html'))


@app.route('/splitVector', methods=['GET', 'POST'])
def splitVectorA():
    mag = float(request.form['mag'])
    angle = float(request.form['angle'])
    return (render_template('splitVector.html', filled='true', answer1=phalculator.comp(1, mag, angle),
                            answer2=phalculator.comp2(1, mag, angle)))

@app.route('/friction', methods=['GET'])
def friction():
    return (render_template('friction.html'))


@app.route('/friction', methods=['GET', 'POST'])
def frictionA():
    coef = float(request.form['coef'])
    mass = float(request.form['mass'])
    angle = float(request.form['angle'])
    incline = str(request.form['inc'])
    return (render_template('friction.html', filled='true', answer=phalculator.friction(coef, mass, angle, incline)))



@app.route('/studyguides')
def studyguides():
    return (render_template('studyguides.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
