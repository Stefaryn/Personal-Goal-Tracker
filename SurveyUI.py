
from tkinter import *
from tkinter.font import Font

class SurveyUI:


	def __init__(self):

		self.root = Tk()

		self.frame = Frame(self.root, width=500, height= 500)

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
		self.buttonCommit = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
		self.buttonCommit.place(y=150, x=400)
		

		#Second question label and placement
		self.third_label = Label(self.frame, text="How do you feel while completing your goal?", font=self.my_font_question, bg="pink")
		self.third_label.place(y= 180, anchor = W)

		#string variable2 associated with answer to the Second question
		self.variable2 = StringVar()

		#Text Box for the second question
		self.textBox2 = Entry(self.frame, width= 50, textvariable = self.variable2, bg="pink")
		self.textBox2.place(y=200)

		#Submit button for textbox2
		self.buttonCommit2 = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
		self.buttonCommit2.place(y=230, x=400)

		#Third question label and placement
		self.fourth_label = Label(self.frame, text="What is hindering you in achieving this goal?", font=self.my_font_question, bg="pink")
		self.fourth_label.place(y= 260, anchor = W)

		#string variable3 associated with answer to the third question
		self.variable3 = StringVar()

		#Text Box for the third question
		self.textBox3 = Entry(self.frame, width= 50, textvariable = self.variable3, bg="pink")
		self.textBox3.place(y=280)

		#Submit button for textbox3
		self.buttonCommit3 = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
		self.buttonCommit3.place(y=310, x=400)

		#Fourth question label and placement
		self.fifth_label = Label(self.frame, text="Can you reformat your goal to make it more achievable?", font=self.my_font_question, bg="pink")
		self.fifth_label.place(y= 340, anchor = W)

		#string variable4 associated with answer to the fourth question
		self.variable4 = StringVar()

		#Text Box for the fourth question
		self.textBox4 = Entry(self.frame, width= 50, textvariable = self.variable4, bg="pink")
		self.textBox4.place(y=360)

		#Submit button for textbox4
		self.buttonCommit4 = Button(self.frame, text="Submit", height = 1, command=lambda: retrieve_text(), bg="pink")
		self.buttonCommit4.place(y=390, x=400)

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

		

		def retrieve_text():
			
			inputValue = self.textBox.get()
			inputValue2 = self.textBox2.get()
			inputValue3 = self.textBox3.get()
			inputValue4 = self.textBox4.get()
			inputValue5 = self.textBox5.get()

			# print(inputValue)
			# print(inputValue2)
			# print(inputValue3)
			# print(inputValue4)
			# print(inputValue5)


		self.root.mainloop()



if __name__ == '__main__':
	SurveyUI()