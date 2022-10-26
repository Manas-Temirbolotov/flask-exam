from . import db


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    department = db.Column(db.String(30))
    wage = db.Column(db.Integer)

    def __repr__(self):
        return self.name


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    birth_date = db.Column(db.DateTime)
    position = db.relationship('Position', backref=db.backref('employees', lazy=True))
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'))

    def __repr__(self):
        return self.name
