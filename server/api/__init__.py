from .auth_api import AuthApi
from .user_api import UserApi
from .user_info_api import UserInfoApi
from .user_skill_api import UserSkillApi
from .skill_api import SkillApi
from .work_history import WorkHistoryApi
from .type_api import TypeApi
from .hobby_api import HobbyApi
from .hobby_skill_api import HobbySkillApi
from .project_api import ProjectApi
from .project_skill_api import ProjectSkillApi
from .token_type_api import TokenTypeApi


def register_routes(app) -> None:
    auth_api = AuthApi()
    app.register_blueprint(auth_api.bp_auth)
    user_api = UserApi()
    app.register_blueprint(user_api.bp_user)
    user_info_api = UserInfoApi()
    app.register_blueprint(user_info_api.bp_user_info)
    user_skill_api = UserSkillApi()
    app.register_blueprint(user_skill_api.bp_user_skill)
    skill_api = SkillApi()
    app.register_blueprint(skill_api.bp_skill)
    work_history_api = WorkHistoryApi()
    app.register_blueprint(work_history_api.bp_work_history)
    type_api = TypeApi()
    app.register_blueprint(type_api.bp_type)
    hobby_api = HobbyApi()
    app.register_blueprint(hobby_api.bp_hobby)
    hobby_skill_api = HobbySkillApi()
    app.register_blueprint(hobby_skill_api.bp_hobby_skill)
    project_api = ProjectApi()
    app.register_blueprint(project_api.bp_project)
    project_skill_api = ProjectSkillApi()
    app.register_blueprint(project_skill_api.bp_project_skill)
    token_type = TokenTypeApi()
    app.register_blueprint(token_type.bp_token_type)
