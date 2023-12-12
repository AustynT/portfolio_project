from typing import Literal
from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.skill_model import SkillModel
from server.schemas.skill_schema import SkillSchema
