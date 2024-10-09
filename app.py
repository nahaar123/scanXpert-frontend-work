from flask import Flask, render_template, request, redirect, url_for # type: ignore
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'xray' not in request.files:
        return redirect(request.url)
    
    file = request.files['xray']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully'

if __name__ == "__main__":
    app.run(debug=True)
