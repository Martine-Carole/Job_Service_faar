import unittest
from app import create_app, db
from app.models import JobPost, Tag


class JobPostModelTestCase(unittest.TestCase) :
    def setUp(self) :
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        with self.app.app_context() :
            db.create_all()

    def tearDown(self) :
        with self.app.app_context() :
            db.session.remove()
            db.drop_all()
        self.app_context.pop()

    def test_create_job_post(self) :
        tag = Tag(tag_name='Engineering')
        db.session.add(tag)
        db.session.commit()

        job = JobPost(
            title='Software Developer',
            description='Develop software',
            company_name='Tech Co',
            location='Remote',
            tag_id=tag.id
        )
        db.session.add(job)
        db.session.commit()
        self.assertIsNotNone(job.id)


if __name__ == '__main__' :
    unittest.main()
