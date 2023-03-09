from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base
from database.customer_dal import CustomerDAL
from database.purchase_dal import PurchaseDAL
from api import rest_controller
from database.seeder import DatabaseSeeder
import os
from configparser import ConfigParser
from kafka_consumer.consumer import KafkaPurchaseConsumer


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

purchase_dal=PurchaseDAL(session=session)
customer_dal=CustomerDAL(session=session)

rest_controller.RestController(app=app, session=session, customer_dal=customer_dal)

consumer = KafkaPurchaseConsumer(purchase_dal=purchase_dal, topic="purchases", bootstrap_servers="localhost:9092")
consumer.start()





