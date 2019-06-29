import sqlite3

connection = None
cursor = None
def main():
	global connection,cursor

	path = './vocabulary.db'
	connect(path)
	#initScript = open('init.sql','r').read()
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

def meaning_format(meaning):

	meaning = meaning.strip()
	meaning = meaning.replace(" ",",").replace("n","n.").replace("v","v.") \
	.replace("adj","adj.").replace(",v"," v").replace(",adj"," adj") \
	.replace(",n"," n").replace("adv","adv.").replace("prep","prep.")

	return meaning

def welcome():

	global connection,cursor

	word = input("Enter the word: ").strip()
	meaning = meaning_format(input("Enter the meaning: "))
	
	while word.lower() != 'stop':
		insertWord(word,meaning)
		word = input("Enter the word: ").strip()
		if word.lower() == "stop":
			break
		meaning = meaning_format(input("Enter the meaning: "))

def insertWord(word,meaning):

	global connection,cursor

	insert_word = "INSERT INTO yaoniming3000 VALUES(:word,:meaning,date('now','localtime'))"

	cursor.execute(insert_word,{"word":word,"meaning":meaning})

	connection.commit()

main()