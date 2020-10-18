import Syllabus1
#make sure to change which python file to import. The imported file is the one with taking the input and make a ics file from it.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/upload', methods=['POST'])
  def upload_file():
     if request.method == 'POST':
         f = request.files['file']
         f.save('uploaded_file.pdf')

if __name__ == "__main__":
    app.run(debug=True)
