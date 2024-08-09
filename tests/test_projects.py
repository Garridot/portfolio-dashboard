import unittest
from flaskr import create_app, db
from flaskr.models import Project, User
from flask_jwt_extended import create_access_token

class ProjectsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('flaskr.config.TestConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Crear un usuario de prueba y obtener un token de acceso
        user = User(username='testuser', password='Testpassword1!')
        db.session.add(user)
        db.session.commit()
        self.access_token = create_access_token(identity='testuser')

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_project(self):
        response = self.client.post('/api/projects', json={
            'title': 'New Project',
            'description': 'Project description',
            'skills': 'skills1, skills2',
            'url_github': 'https://github.com/testuser/newproject',
            'url_project': 'https://newproject.com'
        }, headers={'Authorization': f'Bearer {self.access_token}'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Project created successfully', response.get_json()['message'])

    def test_get_projects(self):
        with self.app.app_context():
            project = Project(title='New Project', description='Project description', url_github='https://github.com/testuser/newproject', url_project='https://newproject.com')
            db.session.add(project)
            db.session.commit()

        response = self.client.get('/api/projects', headers={'Authorization': f'Bearer {self.access_token}'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.get_json()) > 0)

    def test_get_project(self):
        with self.app.app_context():
            project = Project(title='New Project', description='Project description', skills = 'skills1, skills2', url_github='https://github.com/testuser/newproject', url_project='https://newproject.com')
            db.session.add(project)
            db.session.commit()
            project_id = project.id

        response = self.client.get(f'/api/projects/{project_id}', headers={'Authorization': f'Bearer {self.access_token}'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('New Project', response.get_json()['title'])

    def test_update_project(self):
        with self.app.app_context():
            project = Project(title='New Project', description='Project description', skills = 'skills1, skills2', url_github='https://github.com/testuser/newproject', url_project='https://newproject.com')
            db.session.add(project)
            db.session.commit()
            project_id = project.id

        response = self.client.put(f'/api/projects/{project_id}', json={
            'title': 'Updated Project',
            'description': 'Updated description',
            'skills': 'skills3, skills4',
            'url_github': 'https://github.com/testuser/updatedproject',
            'url_project': 'https://updatedproject.com'
        }, headers={'Authorization': f'Bearer {self.access_token}'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Project updated successfully', response.get_json()['message'])

    def test_delete_project(self):
        with self.app.app_context():
            project = Project(title='New Project', description='Project description', skills = 'skills1, skills2', url_github='https://github.com/testuser/newproject', url_project='https://newproject.com')
            db.session.add(project)
            db.session.commit()
            project_id = project.id

        response = self.client.delete(f'/api/projects/{project_id}', headers={'Authorization': f'Bearer {self.access_token}'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Project deleted successfully', response.get_json()['message'])

if __name__ == '__main__':
    unittest.main()


