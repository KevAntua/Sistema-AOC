from flask import Flask, render_template
import os

app = Flask(__name__)

videofolder = os.path.join('static','video')

app.config['UPLOAD_FOLDER'] = videofolder


@app.route('/')
def home():
    vid1= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE1.mp4')
    vid3= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE3.mp4')
    vid4= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE4.mp4')
    vid5= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE5.mp4')
    vid6= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE6.mp4')
    vid7= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE7.mp4')
    vid8= os.path.join(app.config['UPLOAD_FOLDER'], 'PresentacionE8.mp4')
    return render_template('home.html', user_video=vid1, user_video3=vid3, user_video4=vid4, user_video5=vid5, user_video6=vid6, user_video7=vid7, user_video8=vid8 )

@app.route('/about') 
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)