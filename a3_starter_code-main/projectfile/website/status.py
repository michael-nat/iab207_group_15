from flask import Blueprint, render_template, flash, request ,redirect, url_for
from .models import Booking, Concert
from datetime import datetime
#from .forms import BookingForm, UpdateBookingForm
from . import db
import sqlalchemy
from sqlalchemy.sql import text, func
import os

#TotalTickets = [3, 7, 4, 2, 5, 6, 3]

#TicketCount = 300

#TotalTickets2 = 302

current_dateTime = datetime.now()
date = db.session.scalar(db.select(Concert.EventDateTime).where(Concert.id==id))
eventDate = date




class showEventStatus(id):

    TotalTickets = sqlalchemy.select(sqlalchemy.func.sum(Booking.TicketQuantity)).where(Booking.EventID==id)
    EventTickets = sqlalchemy.select(Concert.EventTicketCount).where(Concert.id==id)

    concert = db.session.scalar(db.select(Concert.EventTicketCount).where(Concert.id==id))

    EventStatus = sqlalchemy.select(Concert.EventStatus).where(Concert.id==id)

    if (EventStatus == "Cancelled"):
        pass
    elif (eventDate > current_dateTime):
        EventStatus = "Inactive"
    elif (TotalTickets >= EventTickets):
        EventStatus = "Sold Out"
    else:
        EventStatus = "Open"

    print(EventStatus)
    




