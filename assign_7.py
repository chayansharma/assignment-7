'''
Python Code of Sticky Notes
 
Created By : Chayan Sharma
'''
from Tkinter import *
from tkFileDialog import *
import tkMessageBox  
import time
import threading
import os

pass_flag = True
filename = ""
dir_file = ""
time_reminder = ""
msg_reminder = ""
i = 0;
prefix_file = "./app_data/"
updatefile_date=""
updatefile_month=""
updatefile_year=""
date_options = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
month_options =["01","02","03","04","05","06","07","08","09","10","11","12"]
year_options = ["10","11","12","13","14","15","16","17","18","19","20"]
pri_options =["01","02","03"]
flag = False
## Class pass_wind to make a Top level window for password
class pass_wind():
	## The constructor.
        #  @param self The object pointer.
        #  @param master The object pointer of Top level Window
	def __init__(self,master):
		self.master=master
		master.title("Enter the password and press OK ")
		self.master.minsize(width=300, height=60)
		# Entry widget to take the input password
		self.e = Entry(self.master,width = 30)
		self.e.pack()
		self.e.focus_set()
		# Button widget instance of OK
		self.b = Button(master, text="OK", width=5, command= self.callback)
		self.b.pack()
		self.b.place(x = 40 , y = 30)
		# Button widget instance of QUIR
		self.b_2 = Button(master, text="QUIT", width=5, command = self.finish)
		self.b_2.pack()
		self.b_2.place(x = 200 , y = 30)

	## Call back funtion to be called when OK button is pressed
	# @param self The object pointer.
	def callback(self):
		global  pass_flag
		# If password matches open the app
		if(self.e.get() == "password"):
			pass_flag = True
			self.master.destroy()	
		else:
			# else clear the field and ask againb
			self.e.delete(0, END)
	## finish function if pressed QUIT button
	def finish(self):
		# destroy the window
		self.master.destroy()	

## Class reminder_dialogue to open the reminder Top level window
class reminder_dialogue():
	## The constructor.
        #  @param self The object pointer.
        #  @param master The object pointer of Top level Window
	def __init__(self,master):
		self.master=master
		master.title("Reminder")
		self.master.minsize(width=600, height=100)
		self.master.maxsize(width=600, height=100)
		# Entry widget to take the input time to det the reminder
		self.e_1 = Entry(self.master,width = 10)
		self.e_1.pack()
		self.e_1.focus_set()
		self.e_1.place(x = 160 , y = 10)
		# Entry widget to take the input message
		self.e_2 = Entry(self.master,width = 40)
		self.e_2.pack()
		self.e_2.focus_set()
		self.e_2.place(x = 160 , y = 40)
		# Button widget for OK button
		self.b = Button(master, text="OK", width=5, command= self.callback)
		self.b.pack()
		self.b.place(x = 300 , y = 70)
		self.w = Label(master, text="Time in HH:MM format ")
		self.w.pack()
		self.w.place(x = 10 , y = 15)
		self.w_2 = Label(master, text="Reminder Msg ")
		self.w_2.pack()
		self.w_2.place(x = 10 , y = 40)

	## Call back funtion to be called when OK button is pressed
	# @param self The object pointer.
	def callback(self):
		global time_reminder,msg_reminder
		# Set the global variables to the time given by the user
		time_reminder = self.e_1.get()
		print time_reminder
		msg_reminder = self.e_2.get()
		print msg_reminder
		self.master.destroy()

## Class delete_dialogue to open the delete dailogue box Top level window
class delete_dialogue():
	## The constructor.
        #  @param self The object pointer.
        #  @param master The object pointer of Top level Window
	def __init__(self,master):
		global prefix_file,updatefile_date,updatefile_month,updatefile_year,dir_file
		self.master=master
		master.title("Delete")
		self.master.minsize(width=300, height=150)
		self.master.maxsize(width=300, height=150)
		self.scrollbar = Scrollbar(self.master,orient=VERTICAL)
		#list box widget to show the file names
		self.list_box = Listbox(self.master, selectmode='multiple' ,yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command=self.list_box.yview)
		# Loop to search for the messages 
		if(os.path.isdir(dir_file) == True):
			for self.file in os.listdir(dir_file):
				if self.file.endswith(".txt"):	
					if(self.file != "priority.txt"):
		       		 		self.list_box.insert(END, self.file)
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.list_box.pack()
		self.list_box.place(x = 10 , y = 0)
		# button widget for delete button
		self.b = Button(master, text="Delete", width=5, command= self.callback)
		self.b.pack()
		self.b.place(x = 200 , y = 15)
		self.b_2 = Button(master, text="Cancel", width=5, command= self.cancel_func)
		self.b_2.pack()
		self.b_2.place(x = 200 , y = 50)

	## Call back funtion to be called when Delete button is pressed
	# @param self The object pointer.
	def callback(self,event=None):
		global updatefile_date,updatefile_month,updatefile_year,dir_file
		global prefix_file,flag
        	self.idx = self.list_box.curselection()
		# Open the priority text file to update it
		self.f_r = open( dir_file+"/"+"priority"+".txt", 'r')
		# Open the temporary text file to update it
		self.f_w = open( dir_file+"/"+"temp"+".txt", 'w')
		if (self.idx != ()):
			# Remove the file slected by user
       			for self.index in self.idx:
				os.remove(dir_file+"/"+self.list_box.get(self.index))
			
			# Remove the lines in priority text file
			for self.line in self.f_r:
				for self.index in self.idx:
        				if(self.line.split()[0] == dir_file+"/"+self.list_box.get(self.index)):
						flag = True

				if(flag == False):
					self.f_w.write(self.line)
				flag = False

		self.f_r.close()
		self.f_w.close()
		# Update the priority Text file  
		os.remove(dir_file+"/"+"priority"+".txt")
		os.rename(dir_file+"/"+"temp"+".txt" ,dir_file+"/"+"priority"+".txt")
		self.master.destroy()		

	## Call back funtion to be called when Cancel button is pressed
	# @param self The object pointer.	
	def cancel_func(self):
		#Destroy the window
		self.master.destroy()

## Class main_app to open the main window
class main_app():
	## The constructor.
        #  @param self The object pointer.
        #  @param master The object pointer of Top level Window
	def __init__(self,master):
		global  pass_flag
		self.master=master
		master.title("Editor")
		self.master.minsize(width=620, height=250)
		self.master.maxsize(width=620, height=250)
		# Open the Password window
		self.pass_win = Toplevel(self.master)
		self.GUI_pass = pass_wind(self.pass_win)
		self.master.wait_window(self.pass_win)
		# Check if the password is correct or not 
		if(pass_flag == False):
			# if not correct destroy the main window
			self.master.destroy()	
		else:	
			#else continue
			# Text widget to write the message 
			self.text = Text(master, width=40, height=15)
			self.text.pack()
			self.text.place(x = 120)
			self.sb_date_Var = StringVar(master)
			self.sb_month_Var = StringVar(master)
			self.sb_year_Var = StringVar(master)
			# date Option menu widget
			self.sb_date = OptionMenu(master, self.sb_date_Var, *date_options,command = self.updatefiles)
			self.sb_date.pack()
			self.sb_date.config(width=6)
			self.sb_date.place(x = 420 , y = 10)
			# month Option menu widget
			self.sb_month = OptionMenu(master, self.sb_month_Var, *month_options,command = self.updatefiles)
			self.sb_month.pack()
			self.sb_month.config(width=6)
			self.sb_month.place(x = 480 , y = 10)
			# year Option menu widget
			self.sb_year = OptionMenu(master, self.sb_year_Var, *year_options,command = self.updatefiles)
			self.sb_year.pack()
			self.sb_year.config(width=8)
			self.sb_year.place(x = 530 , y = 10)
			# Scroll bar widget to scroll through the filenames
			self.scrollbar = Scrollbar(self.master,orient=VERTICAL)
			self.list_box = Listbox(self.master,yscrollcommand=self.scrollbar.set)
			self.scrollbar.config(command=self.list_box.yview)
			self.scrollbar.pack(side=RIGHT, fill=Y)
			self.list_box.pack()
			self.list_box.place(x = 430 , y = 60)
			# List box Widget to show the file names			
			self.list_box.bind('<<ListboxSelect>>',self.update_text)

			self.b = Button(master, text="New", width=5, command= self.new_note)
			self.b.pack()
			self.b.place(x = 20 , y = 15)
			self.b_2 = Button(master, text="Save", width=5, command= self.save_note)
			self.b_2.pack()
			self.b_2.place(x = 20 , y = 50)
			self.sb_pri_Var = StringVar(master)	
			# Priority Option menu widget
			self.sb_pri = OptionMenu(master, self.sb_pri_Var, *pri_options,command = self.set_priority_note)
			self.sb_pri.pack()
			self.sb_pri.config(width=6)
			self.sb_pri.place(x = 20 , y = 100)

			self.menubar = Menu(self.master)
			self.filemenu = Menu(self.menubar)
			self.filemenu.add_command(label="Quit", command=master.quit)
			self.menubar.add_cascade(label="File", menu=self.filemenu)
			self.option = Menu(self.menubar)
			self.menubar.add_cascade(label="Option", menu=self.option)
			self.option.add_command(label="Add reminder ...", command=self.reminder)
			self.option.add_command(label="Delete", command=self.delete_notes)
			self.master.config(menu=self.menubar)
	## Function to be called when new button is pressed
	# @param self The object pointer.
	def new_note(self):
		global date_options,month_options,year_options,dir_file
		global prefix_file,filename
		# Make a directory of name being the current data
		dir_file = prefix_file+time.strftime("%d")+"_"+time.strftime("%m")+"_"+time.strftime("%y")
		#Check if current directory exist or not
		if(os.path.isdir(dir_file) == False):
			# If not make the directory
			os.makedirs(dir_file)
			self.f = open( dir_file+"/"+"priority"+".txt", 'w')
			self.f.close()
		# Make a new text file to save the message
		self.f = open( dir_file+"/"+time.strftime("%H:%M:%S")+".txt", 'w')
		self.f.close()
		filename = dir_file+"/"+time.strftime("%H:%M:%S")+".txt"
		# Assign the priority 3 by default and update the priority text file
		self.f = open( dir_file+"/"+"priority"+".txt", 'a')
		self.f.write(filename+" "+"03"+"\n")
		self.f.close()		
		self.text.delete(0.0, END)
		self.sb_date_Var.set(date_options[int(time.strftime("%d"))-1])
		self.sb_month_Var.set(month_options[int(time.strftime("%m"))-1])
		self.sb_year_Var.set(year_options[int(time.strftime("%y"))-10])
		self.sb_pri_Var.set("03")
		self.updatefiles(10)
		
	## Function to be called when Save button is pressed
	# @param self The object pointer.
	def save_note(self):
		global filename
		self.t = self.text.get(0.0, END)
		#Update the text file
		self.f = open(filename, 'w')
		self.f.write(self.t)
		self.f.close()
		self.updatefiles(10)
	## Function to be called when priority option menu is changed
	# @param self The object pointer.		
	def set_priority_note(self,var):
		global dir_file
		self.f_r = open( dir_file+"/"+"priority"+".txt", 'r')
		self.f_w = open( dir_file+"/"+"temp"+".txt", 'w')
		for self.line in self.f_r:
        		if(self.line.split()[0] == filename):
				self.f_w.write(self.line.split()[0]+" "+self.sb_pri.cget("text")+"\n")
			else:
				self.f_w.write(self.line)
		self.f_r.close()
		self.f_w.close()
		os.remove(dir_file+"/"+"priority"+".txt")
		os.rename(dir_file+"/"+"temp"+".txt" ,dir_file+"/"+"priority"+".txt")
		self.updatefiles(10)
				
	## Function to be called when the user wants to see the previous records
	# @param self The object pointer.
	def update_text(self,event=None):	
		global filename,updatefile_date,updatefile_month,updatefile_year,prefix_file,dir_file
		self.idx = self.list_box.curselection()
		filename = dir_file+"/"+self.list_box.get(self.idx)
		self.f = open(filename, 'r')
		self.t = self.f.read()
		self.f.close()
		self.f_r = open( dir_file+"/"+"priority"+".txt", 'r')
		for self.line in self.f_r:
        		if(self.line.split()[0] == filename):
				self.sb_pri_Var.set(self.line.split()[1])
		self.f_r.close()
		self.text.delete(0.0, END)
		self.text.insert(0.0, self.t)

	## Function to be called when a new file or priority of any file is changed
	# @param self The object pointer.
	def updatefiles(self,val):
		global updatefile_date,updatefile_month,updatefile_year,prefix_file,dir_file
		updatefile_date = self.sb_date.cget("text")
		updatefile_month = self.sb_month.cget("text")
		updatefile_year = self.sb_year.cget("text")
		self.first_prior_list = []
		self.second_prior_list = []
		self.third_prior_list = []
		dir_file = prefix_file+updatefile_date+"_"+updatefile_month+"_"+updatefile_year
		self.list_box.delete(0, END)

		if(os.path.isdir(dir_file) == True):
			for self.file in os.listdir(dir_file):
				self.f_r = open( dir_file+"/"+"priority"+".txt", 'r')
				if self.file.endswith(".txt"):
					if(self.file != "priority.txt"):
						for self.line in self.f_r:
        						if(self.line.split()[0] == dir_file+"/"+self.file):
								if(self.line.split()[1] == "01"):
									self.first_prior_list.append(self.file)
								elif(self.line.split()[1] == "02"):
									self.second_prior_list.append(self.file)
								elif(self.line.split()[1] == "03"):
									self.third_prior_list.append(self.file)
				self.f_r.close()
			for self.file in self.first_prior_list:
	      	 		self.list_box.insert(END, self.file)
			for self.file in self.second_prior_list:
	      		 	self.list_box.insert(END, self.file)
			for self.file in self.third_prior_list:
		      	 	self.list_box.insert(END, self.file)
		
		self.text.delete(0.0, END)
		

	## Function to be called when delete button is pressed from menu
	# @param self The object pointer.
	def delete_notes(self):
		self.delete_win = Toplevel(self.master)
		self.GUI_delete =delete_dialogue(self.delete_win)
		self.master.wait_window(self.delete_win)
		self.updatefiles(10)
	## Function to be called when reminder button is pressed from menu
	# @param self The object pointer.
	def reminder(self):
		self.remin_win = Toplevel(self.master)
		self.GUI_remin =reminder_dialogue(self.remin_win)
		self.master.wait_window(self.remin_win)
		self.t = threading.Timer(1.0, self.check_reminder)
		self.t.start()

	## Function to check the reminder using threading
	# @param self The object pointer.
	def check_reminder(self):
		global time_reminder,msg_reminder
		if(time_reminder == time.strftime("%H:%M")):
			tkMessageBox.showinfo("Reminder", msg_reminder)
		else:
			self.master.after(2000,self.check_reminder)

root = Tk()
GUI_main = main_app(root)
root.mainloop()








