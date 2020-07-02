from flask import Flask, render_template
import os

app = Flask(__name__)

videofolder = os.path.join('static','video')

app.config['UPLOAD_FOLDER'] = videofolder

pdffolder = os.path.join('static','Docs')

app.config['UPLOAD_FOL'] = pdffolder

@app.route('/')
def home():
    vid1= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE1.mp4')
    vid3= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE3.mp4')
    vid4= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE4.mp4')
    vid5= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE5.mp4')
    vid6= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE6.mp4')
    vid7= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE7.mp4')
    vid8= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE8.mp4')
    Cue1= os.path.join(app.config['UPLOAD_FOL'], 'CuestionarioE1.pdf')
    Cue2= os.path.join(app.config['UPLOAD_FOL'], 'CuestionarioE2.pdf')
    Cue3= os.path.join(app.config['UPLOAD_FOL'], 'CuestionarioE3.pdf')
    Cue4= os.path.join(app.config['UPLOAD_FOL'], 'CuestionarioE4.pdf')
    Cue5= os.path.join(app.config['UPLOAD_FOL'], 'CuestionarioE5.pdf')
    Cue6= os.path.join(app.config['UPLOAD_FOL'], 'CuestionarioE6.pdf')
    Cue7= os.path.join(app.config['UPLOAD_FOL'], 'CuestionarioE7.pdf')
    Cue8= os.path.join(app.config['UPLOAD_FOL'], 'CuestionarioE8.pdf')
    Expo= os.path.join(app.config['UPLOAD_FOL'], 'Expo3Parcial.pdf')
    Expo1= os.path.join(app.config['UPLOAD_FOL'], 'Expo3Parcial2.pdf')
    return render_template('home.html', user_video=vid1, user_video3=vid3, user_video4=vid4, user_video5=vid5, user_video6=vid6, user_video7=vid7, user_video8=vid8, Cuest1=Cue1, Cuest2=Cue2, Cuest3=Cue3, Cuest4=Cue4, Cuest5=Cue5, Cuest6=Cue6, Cuest7=Cue7, Cuest8=Cue8, Expo=Expo, Expo2=Expo1 )

@app.route('/about') 
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)