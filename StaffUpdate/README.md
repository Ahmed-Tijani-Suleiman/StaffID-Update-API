Staff Details Update Api
-----

## Introduction
This Api will update staff Id on two database tables.




## Tech Stack (Dependencies)

### 1. Backend Dependencies
Our tech stack will include the following:
 * **virtualenv** as a tool to create isolated Python environments
 * **SQLAlchemy ORM** to be our ORM library of choice
 * **MSSQL** as our database of choice
 * **Python3** and **Flask** as our server language and server framework
 *
You can download and install the dependencies mentioned above using `pip` as:
```
pip install virtualenv
pip install SQLAlchemy
pip install postgres
pip install Flask
pip install Flask-Migrate
```
 


## Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes your SQLAlchemy models.
                    "python app.py" to run after installing dependencies
  ├── config.py *** Database URLs, CSRF generation, etc
  ├
  ├── forms.py *** Your forms
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ├
  └── templates
      ├── forms
      

Overall:
* Models are located in the `MODELS` section of `app.py`.
* Controllers are also located in `app.py`.
* The web frontend is located in `templates/`, which builds static assets deployed to the web server at `static/`.
* Web forms for creating data are located in `form.py`


## Development Setup

1. **Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/Scripts/activate
```

2. **Install the dependencies:**
```
pip install -r requirements.txt
```

3. **Run the development server:**
```
export FLASK_APP=myapp
export FLASK_ENV=development # enables debug mode
python3 app.py
```
```

6. **Verify on the Browser**<br>

Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000) 

### Endpoints

#### GET '/staff/<id>'
- Fetches Department, Email, Staff_id.
 
- Sample: `GET http://127.0.0.1:5000/staff/44555`
```
  
{
  "Department": "IT",
  "Email": "aliyutijani80@yahoo.com",
  "Staff_Id": "44555"
}
   

```

#### POST '/staff''


