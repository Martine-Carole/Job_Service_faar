from . import db

class JobPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Integer)
    skills = db.Column(db.String(200))
    employer_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'location': self.location,
            'job_type': self.job_type,
            'salary': self.salary,
            'skills': self.skills,
            'employer_id': self.employer_id
        }
