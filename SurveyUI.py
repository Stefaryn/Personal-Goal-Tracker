
from tkinter import *
from tkinter.font import Font
import goal
import os
import csv

class SurveyUI(Frame):


    def __init__(self, master, goal_n, new_note):

        self.master = master
        Frame.__init__(self, master)

        self.goal_n = goal_n

        self.note = new_note


        self.goal_list = goal.GoalList("savefile.csv")
        if os.path.exists("files/savefile.csv"):
            self.goal_list.load()



        self.goal_name = str(self.goal_list.goals[self.goal_n].name)
        print("IN SURVEY: goal_name",self.goal_name)
        self.goal_size = len(self.goal_list.goals[self.goal_n].rec)
        print("IN SURVEY: goal_size",self.goal_size)

        self.frame = Frame(self, width=500, height= 500)

        self.frame1 = Frame(self.frame)

        #First label "Survey" at the top of the window
        self.frame.pack()
        self.frame.configure(bg="pink")

        self.my_font_title = Font(size = 20)
        self.my_font_question = Font(size = 15)
        self.my_font_description = Font(size = 12)
        self.first_label = Label(self.frame,
            text="Survey",
            font=self.my_font_title, bg="pink")
        self.first_label.place(x=250,anchor = N)

        #description of what the survey UI is for
        self.description_label = Label(self.frame, text="Complete this survey to better understand why your goal progression may be delayed.", font= self.my_font_description, bg="pink")
        self.description_label.place(y=50)

        #First question label and placement
        self.second_label = Label(self.frame, text="How are you feeling?", font=self.my_font_question, bg="pink")
        self.second_label.place(y= 100, anchor = W)

        #string variable1 associated with answer to the first question
        self.variable1 = StringVar()

        #Text Box for the first question
        self.textBox = Entry(self.frame, width= 50, textvariable = self.variable1, bg="pink")
        self.textBox.place(y=120)

        #submit button for textbox
        # self.buttonCommit = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
        # self.buttonCommit.place(y=150, x=400)
        

        #Second question label and placement
        self.third_label = Label(self.frame, text="How do you feel while completing your goal?", font=self.my_font_question, bg="pink")
        self.third_label.place(y= 180, anchor = W)

        #string variable2 associated with answer to the Second question
        self.variable2 = StringVar()

        #Text Box for the second question
        self.textBox2 = Entry(self.frame, width= 50, textvariable = self.variable2, bg="pink")
        self.textBox2.place(y=200)

        #Submit button for textbox2
        # self.buttonCommit2 = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
        # self.buttonCommit2.place(y=230, x=400)

        #Third question label and placement
        self.fourth_label = Label(self.frame, text="What is hindering you in achieving this goal?", font=self.my_font_question, bg="pink")
        self.fourth_label.place(y= 260, anchor = W)

        #string variable3 associated with answer to the third question
        self.variable3 = StringVar()

        #Text Box for the third question
        self.textBox3 = Entry(self.frame, width= 50, textvariable = self.variable3, bg="pink")
        self.textBox3.place(y=280)

        #Submit button for textbox3
        # self.buttonCommit3 = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
        # self.buttonCommit3.place(y=310, x=400)

        #Fourth question label and placement
        self.fifth_label = Label(self.frame, text="Can you reformat your goal to make it more achievable?", font=self.my_font_question, bg="pink")
        self.fifth_label.place(y= 340, anchor = W)

        #string variable4 associated with answer to the fourth question
        self.variable4 = StringVar()

        #Text Box for the fourth question
        self.textBox4 = Entry(self.frame, width= 50, textvariable = self.variable4, bg="pink")
        self.textBox4.place(y=360)

        #Submit button for textbox4
        # self.buttonCommit4 = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
        # self.buttonCommit4.place(y=390, x=400)

        #Fifth question label and placement
        self.sixth_label = Label(self.frame, text="What will help you remember to continue to pursue this goal?", font=self.my_font_question, bg="pink")
        self.sixth_label.place(y= 420, anchor = W)

        #string variable5 associated with answer to the fifth question
        self.variable5 = StringVar()

        #Text Box for the fifth question
        self.textBox5 = Entry(self.frame, width= 50, textvariable = self.variable5, bg="pink")
        self.textBox5.place(y=440)

        #Submit button for textbox5
        self.buttonCommit5 = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
        self.buttonCommit5.place(y=470, x=400)

        
        #self.goal_list.goals[self.goal_n].update(0, self.note, self.inputArray)

        #self.goal_list.goals[self.goal_n].update(0, self.note, self.inputArray)

        def retrieve_text():
            self.inputArray = []
            
            inputValue = self.textBox.get()
            inputValue2 = self.textBox2.get()
            inputValue3 = self.textBox3.get()
            inputValue4 = self.textBox4.get()
            inputValue5 = self.textBox5.get()


            
            self.inputArray.append(inputValue)
            self.inputArray.append(inputValue2)
            self.inputArray.append(inputValue3)
            self.inputArray.append(inputValue4)
            self.inputArray.append(inputValue5)

            print("inputArray", self.inputArray)
            save_survey()


            #survey = self.goal_list.goals[self.goal_n].update(0, self.note, self.inputArray)
            master.destroy()
            return self.inputArray



        def save_survey():

            filename = self.goal_name.replace(" ","_")
            filename = "surveys/" + filename + "_survey"+ str(self.goal_size)+ ".csv"

            with open(filename,'w') as csvfile:
                filewriter = csv.writer(csvfile, lineterminator='\n')

                for note in self.inputArray:
                    #You could add the questions too
                    filewriter.writerow([note])
            csvfile.close()



            # self.goal_list.save()
            #print(self.inputArray)
            #return self.inputArray
    

            #print(self.inputArray)

            
            #self.goal_list.goals[self.goal_n].set_survey(self.inputArray)
            
            
            #print(self.goal_list.goals[self.goal_n].rec)




if __name__ == '__main__':
    root = Tk()
    f = SurveyUI(root)
    f.pack()
    root.mainloop()


