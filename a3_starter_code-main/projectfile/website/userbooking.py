from flask import Blueprint, render_template,request, redirect, url_for
from sqlalchemy import text
from .models import Concert, User, Booking
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

usebookbp = Blueprint('userbooking', __name__)

@usebookbp.route('/userbookings', methods=['GET', 'POST'])

@login_required
def userbookings():
    id= current_user.id
    user = db.session.scalar(db.select(User).where(User.id==id))
    # concerts = db.session.scalars(db.select(Concert).where(Concert.id in (db.select(Booking.EventID).where(Booking.UserID is id ))))  
    sql_query = text("SELECT * FROM Event WHERE Event.id in ( SELECT EventID from Bookings where UserID = 2)")
    cursor = db.session.execute(sql_query)
    concerts = db.session.scalars(cursor)
    return render_template('user/bookings.html',concerts = concerts)


