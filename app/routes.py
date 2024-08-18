from flask_restful import Resource, Api
from app.models import JobPost
from app import db

class JobPostResource(Resource):
    def get(self, job_id):
        job = JobPost.query.get_or_404(job_id)
        return {'id': job.id, 'title': job.title, 'description': job.description, 'company': job.company, 'location': job.location, 'posted_date': job.posted_date}

    def post(self):
        # Logic for creating a new job post
        pass

    def put(self, job_id):
        # Logic for updating a job post
        pass

    def delete(self, job_id):
        # Logic for deleting a job post
        pass

def initialize_routes(api):
    api.add_resource(JobPostResource, '/jobs/<int:job_id>', '/jobs')
