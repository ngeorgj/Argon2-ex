from flask import Flask
from models import User

app = Flask(__main__)

@app.route('/Signup', methods=['POST','GET']
def signin():
    if request.method == 'POST':
        form = request.form
        if form['password'] == form['password2']:
            new_user = User(form['email'], form['username'], form['name'], form['password']):
        else:
            flash('Passwords don't match")
            return redirect('/Signup')
            
        return redirect('/Signin)
     
     return render_template('signup-form.html')

@app.route('/Signin', methods=['POST','GET']
def signin():
    if request.method == 'POST':
        form = request.form
        user = User.query.filter_by(username=form['username']).first()

            if user and ph.verify(user.password, form['password']) == True:
                login_user(user)

            else:
                flash('Password Incorrect.')
                return redirect('/Signin')
                
    return render_template('signin-form.html')
    
if __name__ == "__main__":
    app.run(debug=True)
