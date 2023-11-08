from flask import Blueprint, render_template, flash, request, redirect, url_for
from .models import Concert, Comment
from .forms import ConcertForm
from . import db
from flask_login import login_required, current_user

my_events_bp = Blueprint('events', __name__, url_prefix='/events')

@my_events_bp.route('/events')
@login_required
def events():
    # Query events created by the current user
    user_events = Concert.query.filter_by(userCreator=current_user).all()
    return render_template('user/events.html', user_events=user_events)

@my_events_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_event():
    form = ConcertForm()

    if form.validate_on_submit():
        event = Concert(
            EventName=form.EventName.data,
            EventDesc=form.EventDesc.data,
            # Populate other event attributes here
            UserId=current_user.id,  # Set the user ID as the creator
        )
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully', 'success')
        return redirect(url_for('my_events.my_events'))

    return render_template('create_event.html', form=form)

@my_events_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_event(id):
    event = Concert.query.get(id)

    if event is None or event.userCreator != current_user:
        flash('Event not found or unauthorized', 'danger')
        return redirect(url_for('my_events.my_events'))

    form = ConcertForm(obj=event)

    if form.validate_on_submit():
        form.populate_obj(event)
        db.session.commit()
        flash('Event updated successfully', 'success')
        return redirect(url_for('my_events.my_events'))

    return render_template('edit_event.html', form=form, event=event)

@my_events_bp.route('/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_event(id):
    event = Concert.query.get(id)

    if event is None or event.userCreator != current_user:
        flash('Event not found or unauthorized', 'danger')
        return redirect(url_for('my_events.my_events'))

    db.session.delete(event)
    db.session.commit()
    flash('Event deleted successfully', 'success')
    return redirect(url_for('my_events.my_events'))
