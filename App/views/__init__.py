# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin
from .workouts import workout_views
from .routine import routine_views
from .all_workouts import all_workouts_views
from .login import login_views


views = [user_views,
    index_views, 
    auth_views,
    workout_views,
    routine_views,
    all_workouts_views,
    login_views,
    setup_admin] 
# blueprints must be added to this list