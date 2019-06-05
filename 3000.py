import sqlite3

connection = None
cursor = None
def main():
	global connection,cursor

	path = './vocabulary.db'
	connect(path)
	initScript = open('init.sql','r').read()
	#cursor.executescript(initScript)
	#connection.commit()
	welcome()
	connection.commit()

def connect(path):
	global connection, cursor

	connection = sqlite3.connect(path)
	cursor = connection.cursor()
	cursor.execute('PRAGMA foreign_keys=ON; ')

	connection.commit()

def welcome():

	global connection,cursor

	word = input("Enter the word: ")
	meaning = input("Enter the meaning: ").replace(" ",",")
	while word.lower() != 'stop':
		insertWord(word,meaning)
		word = input("Enter the word: ")
		if word.lower() == "stop":
			break
		meaning = input("Enter the meaning: ").replace(" ",",")

def insertWord(word,meaning):

	global connection,cursor

	insert_word = "INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),:word,:meaning,date('now','localtime'))"

	cursor.execute(insert_word,{"word":word,"meaning":meaning})

	connection.commit()

main()