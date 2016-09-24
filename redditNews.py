import praw
#GUI
import tkinter
#Used to open article links
import webbrowser

#Creating the windows
loginwindow = tkinter.Tk()
newswindow = tkinter.Tk()

#Changing window titles
loginwindow.wm_title("Login to Reddit")
newswindow.wm_title("Reddit News")

#Opening the login window and hiding the news window
loginwindow.deiconify()
newswindow.withdraw()

#Username and Password textvariables
Username = tkinter.StringVar()
Password = tkinter.StringVar()

def Start():
    #Creating a PRAW Reddit object
    r = praw.Reddit(user_agent='reddit_news_grabber_1.0')
    #Getting the 30 hottest news submissions
    submissions = r.get_subreddit('news').get_hot(limit=5)

    #Logging in to reddit to allow voting
    r.login(str(Username.get()), str(Password.get()))

    #Hiding the login window and showing the news window
    loginwindow.withdraw()
    newswindow.deiconify()

    #List to remember what submissions have buttons already
    already_done = []

    #Keeping track of what rows and columns the buttons are in
    rownum = 0
    colnum = 0
    switched = "No"

    #Function to open the submissions websites
    def opensite(site):
        webbrowser.open(site)

    #For loop to create buttons
    for x in submissions:
        #Checking if the buttons have already been made for the submission
        if x.id not in already_done:
            #Creating the button that has karma, title, and links to website
            tkinter.Button(newswindow, text = x, command = lambda x=x: opensite(x.url)).grid(column = colnum, row = rownum)
            #Creating the Up, Clear, and Down vote buttons
            tkinter.Button(newswindow, text = "Up Vote", command = lambda x=x: x.upvote()).grid(column = colnum + 1, row = rownum)
            tkinter.Button(newswindow, text = "Clear Vote", command = lambda x=x: x.clear_vote()).grid(column = colnum + 2, row = rownum)
            tkinter.Button(newswindow, text = "Down Vote", command = lambda x=x: x.downvote()).grid(column = colnum + 3, row = rownum)
            #Adding the submission id to the already done list
            already_done.append(x.id)
            #Increasing the row number
            rownum = rownum + 1
            #Switching off to the second half of the news window
            if rownum >= 15 and switched == "No":
                colnum = 4
                rownum = rownum - 15
                switched = "Yes"

#Login screen widgets
Username_Label = tkinter.Label(loginwindow, text = "Username")
Username_Label.grid(column = 0, row = 1)
Password_Label = tkinter.Label(loginwindow, text = "Password")
Password_Label.grid(column = 0, row = 2)

Username_Entry = tkinter.Entry(loginwindow, textvariable = Username)
Username_Entry.grid(column = 1, row = 1)
Password_Entry = tkinter.Entry(loginwindow, textvariable = Password)
Password_Entry.grid(column = 1, row = 2)

#Login Buttons
Login_Button = tkinter.Button(loginwindow, text = "Login", command = Start)
Login_Button.grid(column = 1, row = 3)

#Putting everything on the screen
tkinter.mainloop()
