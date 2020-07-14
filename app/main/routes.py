from flask import render_template
# from flask_login import login_required, current_user
# from flask_sqlalchemy import get_debug_queries
from . import main
# from .forms import EditProfileForm, EditProfileAdminForm, PostForm, CommentForm
from .. import db
from ..models import User, Course
# from ..decorators import admin_required, permission_required
from sqlalchemy.orm import scoped_session, sessionmaker, Query
from flask import current_app
import pandas as pd

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/users')
def users():
    db_session = scoped_session(sessionmaker(bind=current_app.config['ENGINE']))
    # users = db_session.query(User)
    users = pd.read_sql(db_session.query(User).statement,db_session.bind)
    # print(users)
    # df=pd.DataFrame(users)
    return render_template('admin/users.html', users=[users.to_html(classes="table table-striped", header="true")])

@main.route('/courses')
def courses():
    db_session = scoped_session(sessionmaker(bind=current_app.config['ENGINE']))
    # courses = db_session.query(Course)
    courses = pd.read_sql(db_session.query(Course).statement,db_session.bind)
    # print(users)
    # df=pd.DataFrame(users)
    return render_template('admin/courses.html', courses=[courses.to_html(classes="table table-striped", header="true")])


# @main.route('/user/<username>')
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     page = request.args.get('page', 1, type=int)
#     pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
#         page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
#         error_out=False)
#     posts = pagination.items
#     return render_template('user.html', user=user, posts=posts,
#                            pagination=pagination)

