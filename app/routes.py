from flask_restful import Resource, Api, reqparse
from app.models import JobPost, Tag
from app import db

class JobPostResource(Resource):
    def get(self, job_id):
        job = JobPost.query.get_or_404(job_id)
        return {
            'id': job.id,
            'image_url': job.image_url,
            'title': job.title,
            'description': job.description,
            'company_name': job.company_name,
            'location': job.location,
            'posted_date': job.posted_date,
            'tag_id': job.tag_id
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('image_url', required=False)
        parser.add_argument('title', required=True, help="Title cannot be blank!")
        parser.add_argument('description', required=True, help="Description cannot be blank!")
        parser.add_argument('company_name', required=True, help="Company name cannot be blank!")
        parser.add_argument('location', required=True, help="Location cannot be blank!")
        parser.add_argument('tag_id', required=True, type=int, help="Tag ID cannot be blank!")
        args = parser.parse_args()

        job = JobPost(
            image_url=args['image_url'],
            title=args['title'],
            description=args['description'],
            company_name=args['company_name'],
            location=args['location'],
            tag_id=args['tag_id']
        )
        db.session.add(job)
        db.session.commit()
        return {
            'id': job.id,
            'image_url': job.image_url,
            'title': job.title,
            'description': job.description,
            'company_name': job.company_name,
            'location': job.location,
            'posted_date': job.posted_date,
            'tag_id': job.tag_id
        }, 201

    def put(self, job_id):
        parser = reqparse.RequestParser()
        parser.add_argument('image_url', required=False)
        parser.add_argument('title', required=True, help="Title cannot be blank!")
        parser.add_argument('description', required=True, help="Description cannot be blank!")
        parser.add_argument('company_name', required=True, help="Company name cannot be blank!")
        parser.add_argument('location', required=True, help="Location cannot be blank!")
        parser.add_argument('tag_id', required=True, type=int, help="Tag ID cannot be blank!")
        args = parser.parse_args()

        job = JobPost.query.get_or_404(job_id)
        job.image_url = args['image_url']
        job.title = args['title']
        job.description = args['description']
        job.company_name = args['company_name']
        job.location = args['location']
        job.tag_id = args['tag_id']
        db.session.commit()
        return {
            'id': job.id,
            'image_url': job.image_url,
            'title': job.title,
            'description': job.description,
            'company_name': job.company_name,
            'location': job.location,
            'posted_date': job.posted_date,
            'tag_id': job.tag_id
        }

    def delete(self, job_id):
        job = JobPost.query.get_or_404(job_id)
        db.session.delete(job)
        db.session.commit()
        return {'message': 'Job post deleted successfully'}

def initialize_routes(api):
    api.add_resource(JobPostResource, '/jobs/<int:job_id>', '/jobs')
