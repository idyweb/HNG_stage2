from . import db

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    
def to_json(self):
    return {
        'id': self.id,
        'name': self.name
    }