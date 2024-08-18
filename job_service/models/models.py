from app import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(200), nullable=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)

    def __repr__(self):
        return f'<Job {self.title}>'

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Tag {self.tag_name}>'