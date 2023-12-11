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


def register_routes(app):
    app.add_route('/auth', AuthApi())
    app.add_route('/user', UserApi())
    app.add_route('/user_info', UserInfoApi())
    app.add_route('/user_skill', UserSkillApi())
    app.add_route('/skill', SkillApi())
    app.add_route('/work_history', WorkHistoryApi())
    app.add_route('/type', TypeApi())
    app.add_route('/hobby', HobbyApi())
    app.add_route('/hobby_skill', HobbySkillApi())
    app.add_route('/project', ProjectApi())
    app.add_route('/project_skill', ProjectSkillApi())
