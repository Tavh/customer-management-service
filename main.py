from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base
from database.customer_dal import CustomerDAL
from api import customer_controller
from database.seeder import DatabaseSeeder
import os
from configparser import ConfigParser


app = Flask(__name__)

config = ConfigParser()
config.read('config.ini')

database_url = config['database']['url']
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()

if os.environ.get('FLASK_ENV') == 'development':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

seeder = DatabaseSeeder(session=session)
seeder.run()

customer_dal = CustomerDAL(session=session)

customer_controller.CustomerController(app=app, session=session)


