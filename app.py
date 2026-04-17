from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')



@app.route("/profile",methods=['GET','POST'])
def profile():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        info = request.form.get('info')
        return render_template('profile.html',name=name,age=age,info=info)
    else:
        return False


if __name__ == "__main__":
    app.run(debug=True)