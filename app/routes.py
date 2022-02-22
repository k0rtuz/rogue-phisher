from flask import render_template, redirect, Blueprint

from .forms import GoogleLoginForm

router = Blueprint(
    'router', __name__,
    template_folder='templates',
    static_folder='static'
)


@router.route('/', methods=['GET', 'POST'])
def fake_google_login():
    form = GoogleLoginForm()
    if form.validate_on_submit():
        return redirect()
    return render_template('index.html', title='Sign In', form=form)
