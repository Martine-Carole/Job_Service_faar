from flask import request, jsonify
from flask_restful import Resource, Api
from .models import db, JobPost
from . import create_app

app = create_app()
api = Api(app)

class JobList(Resource):
    def get(self):
        jobs = JobPost.query.all()
        return jsonify([job.to_dict() for job in jobs])


    def post(self):
        data = request.json
        new_job = JobPost(**data)
        db.session.add(new_job)
        db.session.commit()
        return jsonify(new_job.to_dict()), 201

class JobDetail(Resource):
    def get(self, job_id):
        job = JobPost.query.get_or_404(job_id)
        return jsonify(job.to_dict())

    def put(self, job_id):
        job = JobPost.query.get_or_404(job_id)
        for key, value in request.json.items():
            setattr(job, key, value)
        db.session.commit()
        return jsonify(job.to_dict())

    def delete(self, job_id):
        job = JobPost.query.get_or_404(job_id)
        db.session.delete(job)
        db.session.commit()
        return '', 204

api.add_resource(JobList, '/jobs')
api.add_resource(JobDetail, '/jobs/<int:job_id>')
