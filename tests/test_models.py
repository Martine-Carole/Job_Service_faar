import unittest
from app import db
from app.models import JobPost

class JobPostModelTestCase(unittest.TestCase):
    def test_create_job_post(self):
        job = JobPost(title='Software Developer', description='Develop software', company='Tech Co', location='Remote')
        db.session.add(job)
        db.session.commit()
        self.assertIsNotNone(job.id)

if __name__ == '__main__':
    unittest.main()
