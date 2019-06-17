# pollsApp

In this project we have made simple polls app. It’ll create two models: Question and Choice. A Question has a question and a publication date. List of the questions is displayed. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question. This project will help you understand the basics of Django.

### Setup and Installations:

#### To know the commands for these processes refer to the repository: [https://github.com/PranjalJain24/DjangoArchitecture]
* Setup virtual Environment for the project.
* Activate the virtual environment.
* Clone the repository using:
```
$ git clone https://github.com/PranjalJain24/pollsApp  
```
If you want to clone the repository into a directory named something other than pollsApp, you can specify the new directory name as an additional argument:
```
$ git clone https://github.com/PranjalJain24/pollsApp/edit/master/README.md mynewgit
```
That command does the same thing as the previous one, but the target directory is called mynewgit.
  
* Install Django related requirements and dependencies using:
```
pip install -r requirements.txt
```
* Make migrations for Database.
* Create admin user using createsuperuser.
* Run django server: 
```
python manage.py runserver
```
