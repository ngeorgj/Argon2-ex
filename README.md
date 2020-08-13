# Argon2-ex
# This is an Argon2 Tutorial

<h3> Dependencies </h3>
<li> <a href="https://www.python.org/">Python</a> 3.8 or higher  </li>
<li> <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> - pip install flask </li>
<li> <a href="https://flask-login.readthedocs.io/en/latest/">Flask-Login</a> - pip install flask-login </li>
<li> <a href="https://pypi.org/project/argon2-cffi/">Argon2</a> - pip install argon2-cffi </li>

<h3> Models.py </h3>
<p>Here you will declare your database models. 

To hash the password you need to import the PasswordHasher from Argon2 in your `models.py`, so:<br>
`from argon2 import PasswordHasher`

And you need to call it to your program, the default is to use "ph" to name it, so: <br>
`ph = PasswordHasher()`

I'm using the constructor to hash my password as follows:
```python
class User(db.Model, UserMixin):
    name = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, email, username, name, password):
        self.email = email
        self.username = username
        self.name = name
        self.password = ph.hash(password) # < === This is the PasswordHasher, hashing the password when the class is constructed.
        
        # Add the Model to the Session and Commit()
        db.session.add(self)
        db.session.commit()
```
Now, when your model is created inside your db, it's already encrypted, protecting the user.

Your HTML is by your choice, the way you use to collect the information from html, if from `JSON` or `request.form` it's up to you.

An Example signup form is above in the documentation, and cited below:
```html
<form action="/Signup" method="post">
    <input type="text" name='username' placeholder="username">
    <input type="email" name='email' placeholder="email">
    <input type="password" name='password' placeholder="password">
    <input type="password" name='password2' placeholder="confirm password">
    <input type="submit" value="Signup">
</form>
```

The route that this form is posting is this:
```python
@app.route('/Signup', methods=['POST','GET']
def signin():
    if request.method == 'POST':
        form = request.form
        
        # Checks if the passwords match.
        if form['password'] == form['password2']:
            # If they match, a new user is registered in the system with his password safe.
            new_user = User(form['email'], form['username'], form['name'], form['password']):
           
        else:
            # If it does not match, the user is redirected.
            flash('Passwords don't match")
            return redirect('/Signup')
            
        return redirect('/Signin)
     
     return render_template('signup-form.html')
```

Basically assigning the `request.form` to a variable named `form` and using it to pass information.

As the signup form, the signin form is up to your choice, i'll make it very basic:
```html
<form action="/Signin" method="post">
    <input type="text" name='username' placeholder="username or email">
    <input type="password" name='password' placeholder="password">
    <input type="submit" value="Login">
</form>
```

The route is this:
```python
@app.route('/Signin', methods=['POST','GET']
def signin():
    if request.method == 'POST':
        form = request.form
        
        # Gets the user from database.
        user = User.query.filter_by(username=form['username']).first()
            
            # Checks if the passwords match (db password & input password), if they are ok, login user.
            if user and ph.verify(user.password, form['password']) == True:
                login_user(user)

            else:
                flash('Password Incorrect.')
                return redirect('/Signin')
                
    return render_template('signin-form.html')
```
</p>

And that's it.

Hope it helps who needs it!

by: @ngeorg
@ 13/08/2020

