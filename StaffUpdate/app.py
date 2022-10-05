#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from cgitb import text
import email
import json
import dateutil.parser
import babel
from flask_migrate import Migrate
from flask import Flask, jsonify, render_template, request, Response, flash, redirect, url_for,abort
from flask_moment import Moment

from flask_sqlalchemy import SQLAlchemy, models_committed
from flask_wtf import Form
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
import sys

#----------------------------------------------------------------------------#
#Get App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)
migrate = Migrate(app, db)


#-----------------------------------------------------------------------------#
#Models
#------------------------------------------------------------------------------#

class IdentityUser(db.Model):
    __table__ = db.Model.metadata.tables['IdentityUser']
class StaffBasicData(db.Model):
    __table__ = db.Model.metadata.tables['StaffBasicData']






#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def index():
    return render_template('form.html')

@app.route('/staff', methods=['POST'])
def staff():
 
    email=request.form['email']
    id= request.form['id']
    StaffDetail= IdentityUser.query.filter(IdentityUser.Email == email ).one_or_none()
    StaffBasic= StaffBasicData.query.filter(StaffBasicData.Email == email ).one_or_none()


    # abort if not found
    if StaffBasic is None:
            abort(404)
    try:
            StaffDetail.StaffId = request.form['id']
            StaffBasic.Staff_Id = request.form['id']
           
            db.session.commit()

            flash('New Staff ID:' + StaffDetail.StaffId + ' Updated Succesfully.') 
   
            return redirect(url_for('index'))

    except:
        abort(400)
    
    finally:
       db.session.close()
      


@app.route('/staffs/<id>', methods=['GET'])
def staff_update(id):
   staff_data = StaffBasicData.query.get(id)
   return jsonify({
     'Email': staff_data.Email,
     'Staff_Id': staff_data.Staff_Id,
     'Department': staff_data.Department

    }
   )

@app.route('/search', methods=['POST'])
def search_detail():

  user_input = request.form['email']
  data= StaffBasicData.query.filter(StaffBasicData.Email == user_input).all()
  
  response = {
        "count": len(data),
        "data": data,
    }

  return render_template('search.html', results=response, search_term=user_input)



#----------------------------------------------------------------------------#
# ERROR HANDLERS
#----------------------------------------------------------------------------#


@app.errorhandler(400)
def bad_request(error):
        return jsonify({
            "success": False,
            'error': 400,
            "message": "Bad request"
        }), 400

@app.errorhandler(404)
def page_not_found(error):
        return jsonify({
            "success": False,
            'error': 404,
            "message": "Details not found"
        }), 404

@app.errorhandler(422)
def unprocessable_recource(error):
        return jsonify({
            "success": False,
            'error': 422,
            "message": "Unprocessable recource"
        }), 422

@app.errorhandler(500)
def internal_server_error(error):
        return jsonify({
            "success": False,
            'error': 500,
            "message": "Internal server error"
        }), 500

@app.errorhandler(405)
def invalid_method(error):
        return jsonify({
            "success": False,
            'error': 405,
            "message": "Invalid method!"
        }), 405



#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()


