from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from user import User

# defining database credentials
user = 'sriram'
password = 'root'
host = '127.0.0.1'
port = 3306
database = 'Bio-metric System'


def get_connection():
	return create_engine(
		url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
			user, password, host, port, database
		)
	)


if __name__ == '__main__':
	
	try:
		# getting engine (connection obj) for database
		engine = get_connection()
		print(f"Connection to the {host} for user {user} created successfully.")
	except Exception as ex:
		print("Connection could not be made due to the following error: \n", ex)

	with Session(engine) as session:
		stmt = select(User).where(User.date == "2023-02-03")
		# st2 = select(User)
		result = session.execute(stmt)
		# re2 = session.execute(st2)

		for user in result.scalars():
			print(f"Name : {user.name} Id : {user.id} Date : {user.date}")
