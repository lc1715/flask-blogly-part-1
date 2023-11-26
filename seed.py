"""Seed file to make sample data for blogly db"""

from models import User, db     
from app import app            

#Create all tables
db.drop_all()           
db.create_all()        

#If table isn't empty, empty it
User.query.delete()     

#Add users
mickey = User(first_name='Mickey', last_name='Mouse')           
donald = User(first_name='Donald', last_name='Duck')

# Add new objects to session, so they'll persist
db.session.add(mickey)                    
db.session.add(donald)

# Commit--otherwise, this never gets saved!
db.session.commit()                

