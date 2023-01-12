import wikipediaapi

def getWiki(userInput3):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    if not (userInput3): userInput= input("Enter the name of the Wiki page you are looking for: ")
    else: userInput = userInput3
    page_py = wiki_wiki.page(userInput)
    
    #print("Page: %s" % page_py.text)
    print("Page - Title: %s" % page_py.title)
    print("Page - Summary: %s" % page_py.summary)
    userInput2 = input("If this was the page summary you were looking for, press 'enter' or ignore, else type any letter:  ")
    if (len(userInput2)>0):
        text = page_py.text
        getWiki2(userInput, userInput2, text)
def getWiki2(userInput, userInput2, text):
    print("Page: %s" % text)
    print("FOR EXAMPLE, type 'programming language' for Python (programming language)")
    userInput2 = input("Re-enter the new page title you are looking for or enter the corresponding subtitle in parenthesis: ")
    if (len(userInput2) > 0):
        newInput= userInput+ "_" + "(" + userInput2 +")"
        print(newInput)
        getWiki(newInput)
    


getWiki("")


