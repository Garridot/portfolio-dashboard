import unittest
from flaskr import create_app, db
from flaskr.models import User
from flask_jwt_extended import create_access_token

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test_users.db"
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_register(self):
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User created successfully', response.get_json()['message'])

    def test_register_existing_user(self):
        user = User(username='testuser', password='testpassword')
        user.set_password('testpassword')
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Username already exists', response.get_json()['error'])

    def test_login(self):
        user = User(username='testuser', password='testpassword')
        user.set_password('testpassword')
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

        response = self.client.post('/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.get_json())

    def test_login_invalid_user(self):
        response = self.client.post('/login', json={
            'username': 'invaliduser',
            'password': 'invalidpassword'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid username or password', response.get_json()['error'])

    def test_hello_user(self):
        user = User(username='testuser', password='testpassword')
        user.set_password('testpassword')
        with self.app.app_context():
            db.session.add(user)
            db.session.commit()

        with self.app.app_context():
            access_token = create_access_token(identity='testuser')
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = self.client.get('/hello', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, testuser!', response.get_json()['message'])

if __name__ == '__main__':
    unittest.main()
