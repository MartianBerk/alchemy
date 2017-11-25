from sqlalchemy import create_engine, Column, Integer, String, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

Session = sessionmaker(autoflush=False)
Base = declarative_base()
engine = create_engine('postgresql://postgres:God0Awesome@localhost:5432/TEST')


class DataTable(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)

    def __repr__(self):
        return "<Data(name={}, city={})>".format(self.name, self.city)


class Data():
    name = None
    city = None

    def __init__(self, name=None, city=None):
        self.name = name
        self.city = city


session = Session(bind=engine)

data = Data(name='Martin', city='Birmingham')
data_table = session.query(DataTable).filter_by(id=1).one()
# data_table = DataTable(id=1, name=data.name, city=data.city)
data_table.city = "Leeds"
data_table.name = 'Martin'
# load = session.add(data_table)


for attr in inspect(data_table).attrs:
    print(attr.history)
    if attr.history.has_changes():
        print(attr.history.deleted)

exit()

connection = engine.connect()
result = connection.execute('SELECT * FROM Data')

for row in result:
    print(row)

connection.close()
