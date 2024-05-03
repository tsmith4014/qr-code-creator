#run.py is the file that will be used to run the application. It will import the create_app function from the app package and then run the application.
# run.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
