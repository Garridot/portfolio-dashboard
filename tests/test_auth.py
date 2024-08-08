# import unittest
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import create_access_token, JWTManager
# from flaskr import create_app, db
# from flaskr.models import User

# class AuthTestCase(unittest.TestCase):

#     def setUp(self):
#         self.app = create_app('flaskr.config.TestConfig')
#         self.client = self.app.test_client()
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
#         self.app_context.pop()

#     def test_register(self):
#         response = self.client.post('/register', json={
#             'username': 'testuser',
#             'password': 'Testpassword1!'
#         })
#         self.assertEqual(response.status_code, 201)

#     def test_login(self):
#         user = User(username='testuser', password='Testpassword1!')
#         db.session.add(user)
#         db.session.commit()

#         response = self.client.post('/login', json={
#             'username': 'testuser',
#             'password': 'Testpassword1!'
#         })
#         self.assertEqual(response.status_code, 200)
#         data = response.get_json()
#         self.assertIn('access_token', data)

#     def test_login_invalid(self):
#         response = self.client.post('/login', json={
#             'username': 'wronguser',
#             'password': 'wrongpassword'
#         })
#         self.assertEqual(response.status_code, 401)

#     def test_protected_route(self):
#         access_token = create_access_token(identity='testuser')
#         headers = {'Authorization': f'Bearer {access_token}'}
#         response = self.client.get('/hello', headers=headers)
#         self.assertEqual(response.status_code, 200)

# if __name__ == '__main__':
#     unittest.main()
