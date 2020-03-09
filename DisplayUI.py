
from tkinter import *
from tkinter.font import Font
import goal
#Author: Maura McCabe

import os


class SurveyUI(Frame):


    def __init__(self, master, survey_data):

        self.master = master
        Frame.__init__(self, master)

        #Make question members to hold the answers to each question to be filled in below

        self.survey_data = survey_data

        if(survey_data == []):
            window.destroy()
        else:
            print(self.survey_data)


            if(self.survey_data[0] == []):
                self.question1 = survey_data[0]
            else:
                self.question1 = survey_data[0][0]

            if(self.survey_data[1] == []):
                self.question2 = survey_data[1]
            else:
                self.question2 = survey_data[1][0]

            if(self.survey_data[2] == []):
                self.question3 = survey_data[2]
            else:
                self.question3 = survey_data[2][0]

            if(self.survey_data[3] == []):
                self.question4 = survey_data[3]
            else:
                self.question4 = survey_data[3][0]

            if(self.survey_data[4] == []):
                self.question5 = survey_data[4]
            else:
                self.question5 = survey_data[4][0]

        

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


        #Second question label and placement
        self.third_label = Label(self.frame, text="2. How do you feel while completing your goal?", font=self.my_font_question, bg="pink")
        self.third_label.place(y= 180, anchor = W)

        self.question_label2 = Label(self.frame, text = self.question2, font=self.my_font_answer, bg="pink", wraplength = 450, justify = LEFT, relief = RIDGE)
        self.question_label2.place(y=220, anchor = W)


        #Third question label and placement
        self.fourth_label = Label(self.frame, text="3. What is hindering you in achieving this goal?", font=self.my_font_question, bg="pink")
        self.fourth_label.place(y= 260, anchor = W)

        self.question_label3 = Label(self.frame, text = self.question3, font=self.my_font_answer, bg="pink", wraplength = 450, justify = LEFT, relief = RIDGE)
        self.question_label3.place(y=300, anchor = W)


        #Fourth question label and placement
        self.fifth_label = Label(self.frame, text="4. Can you reformat your goal to make it more achievable?", font=self.my_font_question, bg="pink")
        self.fifth_label.place(y= 340, anchor = W)

        self.question_label4 = Label(self.frame, text = self.question4, font=self.my_font_answer, borderwidth=1, bg="pink", wraplength=450, justify = LEFT, relief = RIDGE)
        self.question_label4.place(y=380, anchor = W)


        #Fifth question label and placement
        self.sixth_label = Label(self.frame, text="5. What will help you remember to continue to pursue this goal?", font=self.my_font_question, bg="pink")
        self.sixth_label.place(y= 420, anchor = W)

        self.question_label5 = Label(self.frame, text = self.question5, font=self.my_font_answer, bg="pink", wraplength=450, justify = LEFT, relief = RIDGE)
        self.question_label5.place(y=460, anchor = W)




if __name__ == '__main__':
    root = Tk()
    f = SurveyUI(root)
    f.pack()
    root.mainloop()