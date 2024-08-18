from flask_restful import Resource, reqparse
from models import Job, Tag
from main import api, db
from flask import jsonify

job_post_args = reqparse.RequestParser()
job_post_args.add_argument("title", type=str, help="Title of the job is required", required=True)
job_post_args.add_argument("description", type=str, help="Description of the job is required", required=True)
job_post_args.add_argument("company_name", type=str, help="Company name is required", required=True)
job_post_args.add_argument("location", type=str, help="Location is required", required=True)
job_post_args.add_argument("posted_date", type=str, help="Posted date is required", required=True)
job_post_args.add_argument("tag_id", type=int, help="Tag ID is required", required=True)
job_post_args.add_argument("image_url", type=str, help="Image URL is optional", required=False)

class JobResource(Resource):
    def get(self, job_id):
        job = Job.query.get_or_404(job_id)
        return jsonify({
            "id": job.id,
            "image_url": job.image_url,
            "title": job.title,
            "description": job.description,
            "company_name": job.company_name,
            "location": job.location,
            "posted_date": job.posted_date,
            "tag_id": job.tag_id
        })

    def post(self):
        args = job_post_args.parse_args()
        job = Job(
            title=args['title'],
            description=args['description'],
            company_name=args['company_name'],
            location=args['location'],
            posted_date=args['posted_date'],
            tag_id=args['tag_id'],
            image_url=args['image_url']
        )
        db.session.add(job)
        db.session.commit()
        return {"message": "Job created", "job_id": job.id}, 201

    def put(self, job_id):
        args = job_post_args.parse_args()
        job = Job.query.get(job_id)
        if not job:
            return {"message": "Job not found"}, 404
        job.title = args['title']
        job.description = args['description']
        job.company_name = args['company_name']
        job.location = args['location']
        job.posted_date = args['posted_date']
        job.tag_id = args['tag_id']
        job.image_url = args['image_url']
        db.session.commit()
        return {"message": "Job updated"}

    def delete(self, job_id):
        job = Job.query.get(job_id)
        if not job:
            return {"message": "Job not found"}, 404
        db.session.delete(job)
        db.session.commit()
        return {"message": "Job deleted"}

api.add_resource(JobResource, '/job', '/job/<int:job_id>')

# TagResource can be similarly defined for managing tags