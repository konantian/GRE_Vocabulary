import sqlite3

connection = None
cursor = None
def main():
	global connection,cursor

	path = './vocabulary.db'
	connect(path)
	welcome()
	connection.commit()

def connect(path):
	global connection, cursor

	connection = sqlite3.connect(path)
	cursor = connection.cursor()
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
		insertWord(word,meaning,"other")
		word = input("Enter the word: ").strip()
		if word.lower() == "stop":
			break
		meaning = meaning_format(input("Enter the meaning: "))

def insertWord(word,meaning,tag):

	global connection,cursor

	insert_word = "INSERT INTO GRE VALUES(:Word,:Meaning,:Tag,date('now','localtime'))"

	try:
		cursor.execute(insert_word,{"Word":word,"Meaning":meaning,"Tag":tag})
		connection.commit()
	except:
		print("This word is existed in the database!")
main()