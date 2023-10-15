from flask import Blueprint, render_template, flash, request ,redirect, url_for
from .models import Booking, Concert
from .forms import BookingForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

bookbp = Blueprint('bookings', __name__, url_prefix='/bookings')

@bookbp.route('/<id>/', methods=['GET', 'POST'])
@login_required
def book(id):
    concert = db.session.scalar(db.select(Concert).where(Concert.id==id))
    print(current_user)
    print(id)
    bform = BookingForm()
    if bform.validate_on_submit():  
      booking = Booking(TicketQuantity=bform.TicketQuantity.data, UserID = current_user.id, EventID = id) 
    #   booking = Booking(TicketQuantity=bform.TicketQuantity.data, UserID = 2, EventID = 1) 
      db.session.add(booking) 
      db.session.commit() 
      print('Booking complete', 'success') 
      return redirect(url_for('concert.show', id=id))
    return render_template('concerts/book.html', concert = concert, form = bform)

