
from tkinter import *
from tkinter.font import Font
import goal
import os


class SurveyUI(Frame):


    def __init__(self, master, survey_data):

        self.master = master
        Frame.__init__(self, master)

        #self.goal_n = goal_n

        #self.note = new_note

        self.survey_data = survey_data
       
        print(self.survey_data)
        self.question1 = survey_data[0]
        self.question2 = survey_data[1]
        self.question3 = survey_data[2]
        self.question4 = survey_data[3]
        self.question5 = survey_data[4]

        

        self.goal_list = goal.GoalList("savefile.csv")
        if os.path.exists("files/savefile.csv"):
            self.goal_list.load()

        self.frame = Frame(self, width=500, height= 500)

        self.frame1 = Frame(self.frame)

        #First label "Survey" at the top of the window
        self.frame.pack()
        self.frame.configure(bg="pink")

        self.my_font_title = Font(size = 20)
        self.my_font_question = Font(size = 15)
        self.my_font_description = Font(size = 14)
        self.my_font_answer = Font(size=13)
        self.first_label = Label(self.frame,
            text="Survey",
            font=self.my_font_title, bg="pink")
        self.first_label.place(x=250,anchor = N)

        #description of what the survey UI is for
        self.description_label = Label(self.frame, text="Complete this survey to better understand why your goal progression may be delayed.", font= self.my_font_description, bg="pink")
        self.description_label.place(y=50)

        #First question label and placement
        self.second_label = Label(self.frame, text="1. How are you feeling?", font=self.my_font_question, bg="pink")
        self.second_label.place(y= 100, anchor = W)

        self.question_label = Label(self.frame, text = self.question1, font=self.my_font_answer, bg="pink", wraplength = 450, justify=LEFT, relief = RIDGE)
        self.question_label.place(y=140, anchor = W)


        #submit button for textbox
        # self.buttonCommit = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
        # self.buttonCommit.place(y=150, x=400)
        

        #Second question label and placement
        self.third_label = Label(self.frame, text="2. How do you feel while completing your goal?", font=self.my_font_question, bg="pink")
        self.third_label.place(y= 180, anchor = W)

        self.question_label2 = Label(self.frame, text = self.question2, font=self.my_font_answer, bg="pink", wraplength = 450, justify = LEFT, relief = RIDGE)
        self.question_label2.place(y=220, anchor = W)
        #Submit button for textbox2
        # self.buttonCommit2 = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
        # self.buttonCommit2.place(y=230, x=400)

        #Third question label and placement
        self.fourth_label = Label(self.frame, text="3. What is hindering you in achieving this goal?", font=self.my_font_question, bg="pink")
        self.fourth_label.place(y= 260, anchor = W)

        self.question_label3 = Label(self.frame, text = self.question3, font=self.my_font_answer, bg="pink", wraplength = 450, justify = LEFT, relief = RIDGE)
        self.question_label3.place(y=300, anchor = W)
        #Submit button for textbox3
        # self.buttonCommit3 = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
        # self.buttonCommit3.place(y=310, x=400)

        #Fourth question label and placement
        self.fifth_label = Label(self.frame, text="4. Can you reformat your goal to make it more achievable?", font=self.my_font_question, bg="pink")
        self.fifth_label.place(y= 340, anchor = W)

        self.question_label4 = Label(self.frame, text = self.question4, font=self.my_font_answer, borderwidth=1, bg="pink", wraplength=450, justify = LEFT, relief = RIDGE)
        self.question_label4.place(y=380, anchor = W)

        #Submit button for textbox4
        # self.buttonCommit4 = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
        # self.buttonCommit4.place(y=390, x=400)

        #Fifth question label and placement
        self.sixth_label = Label(self.frame, text="5. What will help you remember to continue to pursue this goal?", font=self.my_font_question, bg="pink")
        self.sixth_label.place(y= 420, anchor = W)

        self.question_label5 = Label(self.frame, text = self.question5, font=self.my_font_answer, bg="pink", wraplength=450, justify = LEFT, relief = RIDGE)
        self.question_label5.place(y=460, anchor = W)

        # #Submit button for textbox5
        # self.buttonCommit5 = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
        # self.buttonCommit5.place(y=470, x=400)

        
        #self.goal_list.goals[self.goal_n].update(0, self.note, self.inputArray)

        #self.goal_list.goals[self.goal_n].update(0, self.note, self.inputArray)

        # def retrieve_text():
        #     self.inputArray = []
            
        #     inputValue = self.textBox.get()
        #     inputValue2 = self.textBox2.get()
        #     inputValue3 = self.textBox3.get()
        #     inputValue4 = self.textBox4.get()
        #     inputValue5 = self.textBox5.get()


            
        #     self.inputArray.append(inputValue)
        #     self.inputArray.append(inputValue2)
        #     self.inputArray.append(inputValue3)
        #     self.inputArray.append(inputValue4)
        #     self.inputArray.append(inputValue5)


        #     survey = self.goal_list.goals[self.goal_n].update(0, self.note, self.inputArray)
        #     return self.inputArray

        #     # self.goal_list.save()
        #     #print(self.inputArray)
        #     #return self.inputArray
    

        #     #print(self.inputArray)

            
        #     #self.goal_list.goals[self.goal_n].set_survey(self.inputArray)
            
            
        #     #print(self.goal_list.goals[self.goal_n].rec)




if __name__ == '__main__':
    root = Tk()
    f = SurveyUI(root)
    f.pack()
    root.mainloop()