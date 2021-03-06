#the import statement above decides which file gets the syllabus
import os
import sys
import tabula
from os import listdir
from docx import Document
#sys.path.append(os.path.abspath("backend"))
import SyllabusStripper
from flask import Flask, render_template, request, redirect, send_from_directory, send_file
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload_file():
   if request.method == 'POST':
       f = request.files['file']
       filename = f.filename
       if filename[filename.index("."):] == ".pdf":
           f.save('uploaded_file.pdf')
       if filename[filename.index("."):] == ".doc":
           f.save('uploaded_file.doc')
       if filename[filename.index("."):] == ".docx":
           f.save('uploaded_file.docx')
       #os.system("python ./backend/SyllabusStripper.py")
       SyllabusStripper.main()
       #exec(open("backend/SyllabusStripper.py").read())
   
   return send_file('download.ics')

@app.route('/upload/uploaded_file')
def uploaded_file(f):
   return send_from_directory(app.config['download.ics'], f, as_attachment=True)
   
if __name__ == '__main__':
   app.run(debug=True)

