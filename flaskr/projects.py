from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flaskr import db
from flaskr.models import Project

projects_bp = Blueprint('projects', __name__)

@projects_bp.route("/projects", methods=["POST"])
@jwt_required()
def create_project():
    title = request.json.get("title")
    description = request.json.get("description")
    url_github = request.json.get("url_github")
    url_project = request.json.get("url_project")
    
    if not title or not description or not url_github or not url_project:
        return jsonify({"error": "All fields are required"}), 400
    
    project = Project(title=title, description=description, url_github=url_github, url_project=url_project)
    db.session.add(project)
    db.session.commit()
    
    return jsonify({"message": "Project created successfully"}), 201

@projects_bp.route("/projects", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    projects_list = [{"id": p.id, "title": p.title, "description": p.description, "url_github": p.url_github, "url_project": p.url_project} for p in projects]
    return jsonify(projects_list), 200

@projects_bp.route("/projects/<int:project_id>", methods=["GET"])
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    project_data = {"id": project.id, "title": project.title, "description": project.description, "url_github": project.url_github, "url_project": project.url_project}
    return jsonify(project_data), 200

@projects_bp.route("/projects/<int:project_id>", methods=["PUT"])
@jwt_required()
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    title = request.json.get("title")
    description = request.json.get("description")
    url_github = request.json.get("url_github")
    url_project = request.json.get("url_project")
    
    if not title or not description or not url_github or not url_project:
        return jsonify({"error": "All fields are required"}), 400
    
    project.title = title
    project.description = description
    project.url_github = url_github
    project.url_project = url_project
    db.session.commit()
    
    return jsonify({"message": "Project updated successfully"}), 200

@projects_bp.route("/projects/<int:project_id>", methods=["DELETE"])
@jwt_required()
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    
    return jsonify({"message": "Project deleted successfully"}), 200
