class Publication:
    
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # setter functions
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author

    # getter functions
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author

    # display
    def display_info(self):
        print(f"Publication name : {self.__title}")
        print(f"Author : {self.__author}")

class Book(Publication):

    def __init__(self, title, author, number_pages=0):
        super().__init__(title, author) # inherent from publication the title and the author
        self.__number_pages = number_pages
        
    # setter function (book pages)
    def set_number_of_pages(self, number_pages):
        if number_pages > 0:            
            self.__number_pages = number_pages

        else:
            print("Number of pages must be positive!")
        
    # getter function (book pages)    
    def get_number_of_pages(self):
        return self.__number_pages

class Magazine(Publication):

    def __init__(self, title, author, issue_number):
        super().__init__(title, author) # inherent from publication the title and the author
        self.__issue_number = issue_number
        
    # setter function (issue number)
    def set_issue_number(issue_number):
        self.__issue_number = issue_number
        
    # getter function (issue number)    
    def get_issue_number(self):
        return self.__issue_number
    
# Sample objects
pub1 = Publication("The Central Scholar Newspaper", "Ma'am Ruth De Leon")
book1 = Book("Don Quixote", "Miguel Cervantes", 500)
mag1 = Magazine("National Geographic", "Various Authors", 223)

print("Publication Information ::: ")
pub1.display_info()

print("\nBook Information ::: ")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information ::: ")
mag1.display_info()
print(mag1.get_issue_number())

