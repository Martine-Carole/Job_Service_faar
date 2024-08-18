from app import db

class JobPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    posted_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50), nullable=False)
    jobs = db.relationship('JobPost', backref='tag', lazy=True)
