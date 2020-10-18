import tabulaPDFTables
#the import statement above decides which file gets the syllabus

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload_file():
   if request.method == 'POST':
       f = request.files['file']
       f.save('/backend/uploaded_file.pdf')
       return redirect("../",code=302)

@app.route('/uploads/<uploaded_file.pdf>')
def uploaded_file(f):
   return send_from_directory(app.config['/backend/downloaded_file.ics'], f, as_attachment=True)
   
if __name__ == '__main__':
   app.run(debug=True)

