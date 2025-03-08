#Tkinter project:Mental Health Traker

from tkinter import*
from tkinter import messagebox,Text
from PIL import Image, ImageTk
import re
import mood_ques_option #user defined module
import google.generativeai as generativeai
import textwrap
window=Tk() #creating the main window
#to set the title of window
window.title('Mental Health Tracker')
#window.geometry('900x600')
window.attributes('-fullscreen',True)
screenwidth=window.winfo_screenwidth()
screenheight=window.winfo_screenheight()
img = Image.open("C:\\Users\\Hp\\OneDrive\\Desktop\python project(mood traker)\relaxing-mind-double-exposure-calm-green-nature-nature-forests_743855-9957.jpg")
img=img.resize((screenwidth,screenheight),Image.LANCZOS)# Resize the image to the window size
image1 = ImageTk.PhotoImage(img)
Label(window,image=image1).place(x=0,y=0,relwidth=1,relheight=1)

Note='''INSTRUCTION:
    This tool is designed to help you track and manage your mental health.
    Answer a series of questions to assess your mood, feelings, and overall well-being.
    Let\'s begin your journey towards a healthier mind!'. 
    Note:
    There are 5 Set of Questions,
    write the text carefully as per your behievour and feeling,
    otherwise it will gives you the wrong prediction'''

instr=Label(window,text=Note,font=('Comic Sans MS',15),bd=2,bg='skyblue')
instr.place(x=100,y=450)
wel=Label(window,text='WELCOME TO THE MENTAL HEALTH TRACKER',font=('Comic Sans MS',25,'bold','italic'),fg='white', bg='orange',bd=0,relief='flat')
wel.place(x=80,y=100)

getusername=None
getbirthdate=None
getdestination=None
#function for login page
def login_page():
    global getusername
    global getbirthdate
    global getdestination
    instr.destroy()
    wel.destroy()
    login_page_bt.destroy()
    #to make the frame inside the window
    frameloginpage = Frame(window, bg="#4979d1", relief="raised", bd=3,highlightbackground='blue')
    frameloginpage.place(x=540, y=180, width=450, height=150)

    login=Label(frameloginpage,text='Login',font=('arial',20),bg='#4979d1',fg='black')
    login.grid(row=10,column=20)

    #to get the username from user
    getusername=Entry(frameloginpage,width=30)
    getusername.grid(row=15,column=20)

    name=Label(frameloginpage,text='Your Name=',font=('Comic Sans MS',15,'bold','italic'),bg='#4979d1')
    name.grid(row=15,column=10)

    #function for login into question
    def login():
    #to check weather the entered passward from user is in correct formet for not
        if getusername.get()!="":
            new_window_page()
        else:
            messagebox.showinfo('Warning','Invalid syntex of Username or Passward')

    bt = Button(frameloginpage, text='Login', command=login,font=('Comic Sans MS',10,'bold','italic'))
    bt.grid(row=70, column=20)

login_page_bt=Button(window,text='Start',command=login_page,font=('Arial',20))
login_page_bt.place(x=900,y=700)

#to destroy the previous frame
def switch_frame(current_frame, new_frame):
    if current_frame is not None:
        current_frame.destroy()  # Destroy the previous frame
    new_frame.place(relx=0.5,rely=0.5,anchor="center",width=700,height=400)

response={}
#function to set the new page or window
choiselist={}
choise_text=None
def new_window_page():
    page=Toplevel() #toplevel use to create the child window
    page.title('Mental Health Traker')
    page.attributes('-fullscreen',True)
    pagewidth=page.winfo_screenwidth()
    pageheight=page.winfo_screenheight()
    #for image
    
    img1 = Image.open("C:\\Users\\Hp\\OneDrive\\Desktop\\python project(mood traker)\\Mind-is-like-water-1-scaled.jpg")
    img1 = img1.resize((pagewidth,pageheight),Image.LANCZOS)  # Resize the image if necessary
    image2 = ImageTk.PhotoImage(img1)
    label1 = Label(page, image=image2)
    label1.image = image2  # Keep a reference to avoid garbage collection
    label1.place(x=0,y=0,relwidth=1,relheight=1)

    #to display Emoji in page
    label1 = Label(page, text='😊 😄 😁 🤩 😎 🥳 😇', font=('Comic Sans MS', 28, 'bold', 'italic'),  fg="purple",  bg='lightyellow',  relief='solid', bd=4,  padx=20,  pady=10)  
    label1.place(x=50, y=20)  

    #function to create the next button in side the page(child window)
    currentquestion=1
    questionframe=None

    def result():
        generativeai.configure(api_key="AIzaSyDea_AdN_yfBDPBAgVGTHCwwlzohbMci0w")
        result_window=Toplevel()
        result_window.geometry('1000x600')
        result_window.configure(bg="#874e18")
        model=generativeai.GenerativeModel("gemini-1.5-pro")
        prompt=f"Identify the exact Emotional mood of person ,on the basis answers of questions in this={choiselist},this dictinary basically contain key as question and answer as value ,which denotes the users emotions,name of person is={getusername.get()},generate the mood in one sentence etc by analysing the given information,provide clear information about the mood"
                    
        response=model.generate_content(prompt)
        responsetext=response.text.strip()
        resulttext=textwrap.fill(responsetext,width=50)

        
       
        # Create a frame to hold the result content
        result_frame = Frame(result_window, relief="raised", bd=5, bg='#411887', padx=20, pady=20)
        result_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Label to display the title
        Label(result_frame, text="Your Mental Health Analysis", font=('Comic Sans MS', 18, 'bold'), bg='lightblue', fg='darkblue').pack(pady=10)

        # Label to display the AI-generated result
        result_label = Label(result_frame, text=resulttext, font=('Times New Roman', 14), bg='lightblue', fg='black', wraplength=550, justify="left")
        result_label.pack(pady=10)

        # Close button
        Button(result_frame, text="Close", command=result_window.destroy, font=('Arial', 12, 'bold'), bg='red', fg='white', padx=10, pady=5).pack(pady=10)
        
    #function to move the next page
    def move_next():
        global choise_text
        nonlocal currentquestion,questionframe
        newframe=Frame(page,bd=5,relief='raised')
        #calling of funtion to destroy the previous frame
        switch_frame(questionframe,newframe)
        questionframe=newframe

        if currentquestion<=len(mood_ques_option.testing_question()):
            questionno=Label(newframe,text=f'Question {currentquestion}',font=('Times New Roman',20),relief='raised',fg='brown').place(x=0,y=0)
            questionname=Label(newframe, text=f"Q{currentquestion}:{mood_ques_option.testing_question()[currentquestion]}",font=('Times New Roman', 30), wraplength=650, justify='left').grid(row=0, column=0, sticky='w', padx=10, pady=40)
          #  selected_option=IntVar() #it return the selected option

            Label(newframe,text="Write you text/answer here",font=('Times New Roman',15),justify="left").grid(row=5,column=0)
            choise_text=Entry(newframe,width=40,font=("Time New Roman",20))
            choise_text.grid(row=7,column=0)
            
            #radio button for options
            #for ind,op in enumerate(testing_option()[currentquestion],start=1):
                #Radiobutton(newframe,text=op,value=ind,variable=selected_option,font=('Arial',15)).grid(row=2+ind,column=0,sticky='w',padx=20)

            def save_selection():
                nonlocal currentquestion
                if choise_text.get().strip()!="":
                    choiselist.update({mood_ques_option.testing_question()[currentquestion]:choise_text.get()})
                   # response[currentquestion]=testing_option()[currentquestion][selected_option.get()-1]
                    currentquestion+=1
                    # Check if this was the last question
                    if currentquestion > len(mood_ques_option.testing_question()):
                    # If it's the last question, open the result window directly
                        result()
                    else:
                        # Otherwise, move to the next question
                        move_next()
                else:
                    messagebox.showinfo('SelectionError','Text Field is Empty')

            Button(newframe, text='Next', command=save_selection, font=('arial', 15),bg="lightcoral", fg="white").grid(row=8, column=0, pady=10)

        else:

            #set the API key
            #this function is for result predication
            
            Button(page, text='Submit', command=result,font=('arial',20),bg="lightcoral", fg="white").place(x=600,y=450)
    move_next()  
    

window.mainloop()