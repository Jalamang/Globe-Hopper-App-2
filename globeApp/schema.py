import dbconn

myCursor = dbconn.con.cursor()

myCursor.execute("USE globehopperapp")

myCursor.execute("DROP TABLE IF EXISTS Country");
myCursor.execute("CREATE TABLE Country(CountryId INT AUTO_INCREMENT  PRIMARY KEY, Name VARCHAR(100) NOT NULL, Population DOUBLE NOT NULL, Continent VARCHAR(250) NOT NULL)");
myCursor.execute("DROP TABLE IF EXISTS City");
myCursor.execute("CREATE TABLE City(CityId INT AUTO_INCREMENT  PRIMARY KEY,Name VARCHAR(100) NOT NULL,CountryId INT NOT NULL,Capital INT NOT NULL,FirstLandmark VARCHAR(250) NOT NULL,SecondLandmark VARCHAR(250) NOT NULL,ThirdLandmark VARCHAR(250) NOT NULL)");
dbconn.con.commit()


