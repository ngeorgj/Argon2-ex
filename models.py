from argon2 import PasswordHasher
ph = PasswordHasher()

class User(db.Model, UserMixin):
    name = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, email, username, name, password):
        self.email = email
        self.username = username
        self.name = name
        self.password = ph.hash(password)
        
        # Add the Model to the Session and Commit()
        db.session.add(self)
        db.session.commit()
