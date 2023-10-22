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
    userquery = db.select(Booking.EventID).where(Booking.UserID==id)
    userresult = db.session.execute(userquery).scalars()
    userbookings = userresult.all()
    
    # print(userbookings)
    
    concerts = db.session.scalars(db.select(Concert).where(Concert.id.in_(userbookings)))
    
    return render_template('user/bookings.html',concerts = concerts)



