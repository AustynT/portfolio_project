from server import db


class ProjectModel(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.type_id'))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    project_image = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    # Relationship for project skills
    project_skills = db.relationship('ProjectSkill', backref='project')
