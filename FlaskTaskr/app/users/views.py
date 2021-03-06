from app import db
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from app.views import login_requred, flash_errors
from forms import RegisterForm, LoginForm
from app.models import User
from sqlalchemy.exc import IntegrityError


# this defines our users Blueprint along with custom temp & static folders.
# it also tells us the url at which users is accessible.
mod = Blueprint('users', __name__, url_prefix='/users',
                template_folder='templates',
                static_folder='static'
                )

# now @mod will be used instead of @app, like we originally used. Wow!
@mod.route('/logout/')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('You are logged out. Bye!')
    return redirect(url_for('.login'))


@mod.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method=='POST':
        u = User.query.filter_by(name=request.form['name'], password=request.form['password'].first())
        if u is None:
            error = 'Invalid password or username.'
        else:
            session['logged_in'] = True
            session['user_id'] = u.id
            flash('You are logged in. Go nuts.')
            return redirect(url_for('tasks.tasks'))  # that is, the tasks view of the tasks Blueprint.
    return render_template("users/login.html", form=LoginForm(request.form), error=error)


@mod.route('/register', methods=['get', 'post'])
def register():
    error = None
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_user = User(
            form.name.data,
            form.email.data,
            form.password.data,
        )
    try:
        db.session.add(new_user)
        db.session.commit()
        flash('Thanks for registering. Please login.')
        return redirect(url_for('.login'))  ## url for login view of the _current_ Blueprint.
    except IntegrityError:
        error = "Oh snap! That username and/or email already exists. Try again."
    else:
        flash_errors(form)
    return render_template('/users/register.html', form=form, error=error)
