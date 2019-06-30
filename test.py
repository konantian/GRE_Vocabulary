import sqlite3

path = './vocabulary.db'
connection = sqlite3.connect(path)
cursor = connection.cursor()
connection.commit()

cursor.execute("SELECT word,meaning,date_when_inserated FROM yaoniming3000")
result = cursor.fetchall()

for row in result:
	word, meaning, date_when_inserted = row
	tag = "3000"
	insert = "INSERT INTO GRE VALUES(:Word,:Meaning,:Tag,:Date_when_inserted)"
	cursor.execute(insert,{"Word":word,"Meaning":meaning,"Tag":tag,"Date_when_inserted":date_when_inserted})
connection.commit()