import sqlite3

class DictionaryApp:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS words(
                id INTEGER PRIMARY KEY,
                word TEXT,
                meaning TEXT,
                sentence TEXT            
            )
            ''')
        self.conn.commit()

    def add_word(self,word,meaning,sentence):
        self.cursor.execute("INSERT INTO words (word, meaning,sentence) VALUES ( ?, ?, ?)",(word,meaning,sentence))
        self.conn.commit()

    def list_words(self):
        self.cursor.execute("SELECT * FROM words")
        words = self.cursor.fetchall()
        return words
    
    def search_word(self, word):
        self.cursor.execute("SELECT * FROM words WHERE word LIKE ? ORDER BY word ASC", ('%' + word + '%',))
        word = self.cursor.fetchall()
        return word
    
    def delete_word(self,word):
        self.cursor.execute('DELETE FROM words WHERE word = ?',(word,))
        self.conn.commit()

    def close(self):
        self.conn.close()

def main():
    dictionary  = DictionaryApp("words.db")
    while True:
        print("\n Dictionary Application")
        print("1 : Add Words")        
        print("2 : list Words")
        print("3 : Search Words")
        print("4 : Delete Words")
        print("5 : Exit")

        choice = input("Select an operations : ")
        if choice == "1" :
            word = input("Word: ")
            meaning = input("Meaning: ")
            sentence = input("Example Sentence: ")
            dictionary.add_word(word,meaning,sentence)
            print("Word added successfully...")

        elif choice == "2" :
            words = dictionary.list_words()
            if words:
                print("\nWord List : ")
                for word in words:
                    print(f"Words : {word[1]}, \nMeaning : {word[2]}, \nExample Sentence : {word[3]}")
            else :
                print("no words are added here now")

        elif choice == "3":
            word = input("Enter Word to Search: ")
            print(word)
            result = dictionary.search_word(word)
            if result:
                for word in result:
                    print(f"Words : {word[1]}, \nMeaning : {word[2]}, \nExample Sentence : {word[3]}")
            else:
                print("Word not found.")

        elif choice == "4":
            word = input("Enter Word to Delete: ")
            dictionary.delete_word(word)
            print("Word deleted.")

        elif choice == "5":
            dictionary.close()
            break

if __name__ == "__main__":
    main()
