
class Hobby(db.Model):
    __tablename__ = 'hobbies'
    hobby_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.type_id'))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    # Relationship for hobby skills
    hobby_skills = db.relationship('HobbySkill', backref='hobby')
