from app import db


class Ticket(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	message = db.Column(db.String(150),nullable=False)
	group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
	author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	enabled = db.Column(db.Boolean, default=True)
	technician_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Group(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)

class State(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))


class State(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)


class Message(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	enabled = db.Column(db.Boolean, default=True)
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'))
	message = db.Column(db.String(150),nullable=False)
