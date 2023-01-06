from tkinter import *
import tkinter.messagebox
import backend

class MovieBooker:
	def __init__(self, root):
		self.root = root
		self.root.title("Movie Ticket Booking System")
		self.root.geometry("1350x750+0+0")
		self.root.config(bg = "black")

		#member variables
		Movie_Name = StringVar()
		Movie_ID = StringVar()
		Cast = StringVar()
		Budget = StringVar()
		Duration = StringVar()
		Rating = StringVar()
		Release_Date = StringVar()
		Director = StringVar()

		#member functions of the class
		def insert_data():
			if(len(Movie_ID.get()) != 0):
				backend.create_record()
				backend.insert_record(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get())
				MovieList.delete(0,END)
				MovieList.insert(END,(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get()))			

		def display_data():
			MovieList.delete(0,END)
			for row in backend.view_record():
				MovieList.insert(END, row, str(""))
		
		def clear_fields():
			self.txtMovie_ID.delete(0,END)
			self.txtMovie_Name.delete(0,END)
			self.txtRelease_Date.delete(0,END)
			self.txtDirector.delete(0,END)
			self.txtCast.delete(0,END)
			self.txtBudget.delete(0,END)
			self.txtRating.delete(0,END)
			self.txtDuration.delete(0,END)

		def search_data():
			MovieList.delete(0,END)
			for row in backend.search_record(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Duration.get(),Rating.get()):
				MovieList.insert(END, row, str(""))

		def delete_data():
			if(len(Movie_ID.get()) != 0 or len(Movie_Name.get()) != 0 or len(Release_Date.get()) != 0 or len(Rating.get()) != 0):
				backend.delete_record(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Rating.get())
				clear_fields()
				display_data()

		def update_data():
			if(len(Movie_ID.get()) != 0):
				backend.delete_record(Movie_ID.get())
			if(len(Movie_ID.get()) != 0):
				backend.insert_record(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get())
				MovieList.delete(0,END)
				MovieList.insert(END,(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get()))
		
		def book_movie():
			if(len(Movie_ID.get()) != 0 or Movie_Name.get() != 0):
				a = backend.available_seats(Movie_ID.get(),Movie_Name.get())
				if a[0][0] !=  0:
					backend.book_movies(Movie_ID.get(),Movie_Name.get())
					display_data()
					tkinter.messagebox.showinfo("Booking Status", "Your Show is Booked.\nENJOY the show :)")
				else:
					tkinter.messagebox.showwarning("Booking Status", "Seats are NOT available.\nPlease Book Another Show.")

		def instructions_bulletin():	
			temp = Toplevel(root)
			temp.title("INSTRUCTIONS: ")
			temp.geometry('700x900')

			instr = "* ADDING ENTRY TO THE APPLICATION:\n\t1. All the fields are mandatory\n\t2. Click 'Add New' button to add entry.\n\n"
			instr +=  "* DISPLAY:\n\t1.'Display' button will enlist all the available entries."
			instr +=  "\n\n* MOVIES CAN BE SEARCHED USING:\n\t1. Movie ID\n\t2. Movie Name\n\t3. Release Date\n\t4. Duration\n\t5. Rating"
			instr +=  "\n\n* CLEAR:\n\t1. 'Clear' button will clear all entries in input field."
			instr +=  "\n\n* MOVIES CAN BE DELETED USING:\n\t1. Movie_ID\n\t2. Movie Name\n\t3. Release Date\n\t4. Rating"
			instr +=  "\n\n* UPDATE:\n\t1. All the fields need to be filled before updating a record.\n\t2. Movie will be updated on the basis of Movie_ID"
			instr +=  "\n\n* BOOK:\n\t1. Shows can be Booked by using Movie_ID or Movie Name.\n\t2. Warning will be displayed if Shows are Houseful."
			instr +=  "\n\n* Instruction: \n\tMore than 1 field used in 'Search' and 'Delete' will fetch \n\tthe result by using 'OR' condition.\n"
			instr +=  "\n\n\t ===============  THANK YOU =============== "

			frame = Frame(temp,width = 700,height = 900)
			frame.pack(expand = True, fill = BOTH)
			canvas1 = Canvas(frame, width = 700 , height =  900, bg = "gray13",scrollregion = (0,0,600,1000))
			vbar = Scrollbar(frame,orient = VERTICAL)
			vbar.pack(side = RIGHT,fill = Y)
			vbar.config(command = canvas1.yview)
			canvas1.config(yscrollcommand = vbar.set)
			canvas1.create_text(350, 450, text = instr, fill = "medium turquoise", font = ('Calibari', 14, 'bold'))
			canvas1.pack(side = LEFT)
			temp.mainloop()

		def exit_window():
			exit_window = tkinter.messagebox.askyesno("Online Movie Ticket Booking System", "DO YOU WISH TO EXIT THE APPLICATION ?", detail = 'After clicking "Yes", the application will be automatically closed.' )
			if exit_window>0:
				root.destroy()
			return


		#Frames
		MainFrame = Frame(self.root, bg = "black")
		MainFrame.grid()

		TFrame = Frame(MainFrame, bd = 5, padx = 54, pady = 8, bg = "black", relief = RIDGE)
		TFrame.pack(side = TOP,pady =  5)

		self.TFrame = Label(TFrame, font = ('Arial', 40, 'bold'), text = "MOVIE TICKET BOOKING SYSTEM", bg = "grey27", fg = "turquoise")
		self.TFrame.grid(padx = 60,pady = 3) 

		BFrame = Frame(MainFrame, width = 1350, height = 70, bd = 5, padx = 25, pady = 10, bg = "grey18", relief = RIDGE)
		BFrame.pack(side = BOTTOM,padx = 60, pady = 3)

		DFrame = Frame(MainFrame, bd = 2, width = 1000, height = 100, padx = 30, pady = 30, bg = "black", relief = RIDGE)
		DFrame.pack(side = BOTTOM, padx = 40, pady = 3)

		DFrameL = LabelFrame(DFrame, width = 300, height = 100, padx = 20, pady =  20, bg = "black", relief = RIDGE, font = ('Arial', 18, 'bold'), text = "Movie Details_\n", fg = "white")
		DFrameL.pack(side = LEFT,padx = 10)

		DFrameR = LabelFrame(DFrame, width = 900, height = 400, padx = 10, pady = 10, bg = "black", relief = RIDGE, font = ('Arial', 18, 'bold'), text = "Movie Information_\n", fg = "white")
		DFrameR.pack(side = RIGHT)


		#Labels & Entry Box
		self.lblMovie_ID = Label(DFrameR, font = ('Arial', 16, 'bold'), text = "Movie ID:", padx = 2, pady = 2, bg = "black", fg = "dark turquoise")
		self.lblMovie_ID.grid(row = 0, column = 0, sticky = W)
		self.txtMovie_ID = Entry(DFrameR, font = ('Arial', 16, 'bold'), textvariable = Movie_ID, width = 39, bg = "black", fg = "white")
		self.txtMovie_ID.grid(row = 0, column = 1) 

		self.lblMovie_Name = Label(DFrameR, font = ('Arial', 16, 'bold'), text = "Movie Name:", padx = 2, pady = 2, bg = "black", fg = "dark turquoise")
		self.lblMovie_Name.grid(row = 1, column = 0, sticky = W) 
		self.txtMovie_Name = Entry(DFrameR, font = ('Arial', 16, 'bold'), textvariable = Movie_Name, width = 39, bg = "black", fg = "white")
		self.txtMovie_Name.grid(row = 1, column = 1)

		self.lblRelease_Date = Label(DFrameR, font = ('Arial', 16, 'bold'), text = "Release Date:", padx = 2, pady = 2, bg = "black", fg = "dark turquoise")
		self.lblRelease_Date.grid(row = 2, column = 0, sticky = W) 
		self.txtRelease_Date = Entry(DFrameR, font = ('Arial', 16, 'bold'), textvariable = Release_Date, width = 39, bg = "black", fg = "white")
		self.txtRelease_Date.grid(row = 2, column = 1)

		self.lblDirector = Label(DFrameR, font = ('Arial', 16, 'bold'), text = "Director:", padx = 2, pady = 2, bg = "black", fg = "dark turquoise")
		self.lblDirector.grid(row = 3, column = 0, sticky = W) 
		self.txtDirector = Entry(DFrameR, font = ('Arial', 16, 'bold'), textvariable = Director, width = 39, bg = "black", fg = "white")
		self.txtDirector.grid(row = 3, column = 1)

		self.lblCast = Label(DFrameR, font = ('Arial', 16, 'bold'), text = "Cast:", padx = 2, pady = 2, bg = "black", fg = "dark turquoise")
		self.lblCast.grid(row = 4, column = 0, sticky = W) 
		self.txtCast = Entry(DFrameR, font = ('Arial', 16, 'bold'), textvariable = Cast, width = 39, bg = "black", fg = "white")
		self.txtCast.grid(row = 4, column = 1)

		self.lblBudget = Label(DFrameR, font = ('Arial', 16, 'bold'), text = "Budget (Crores INR):", padx = 2, pady = 2, bg = "black", fg = "dark turquoise")
		self.lblBudget.grid(row = 5, column = 0, sticky = W) 
		self.txtBudget = Entry(DFrameR, font = ('Arial', 16, 'bold'), textvariable = Budget, width = 39, bg = "black", fg = "white")
		self.txtBudget.grid(row = 5, column = 1)

		self.lblDuration = Label(DFrameR, font = ('Arial', 16, 'bold'), text = "Duration (Hrs):", padx = 2, pady = 2, bg = "black", fg = "dark turquoise")
		self.lblDuration.grid(row = 6, column = 0, sticky = W) 
		self.txtDuration = Entry(DFrameR, font = ('Arial', 16, 'bold'), textvariable = Duration, width = 39, bg = "black", fg = "white")
		self.txtDuration.grid(row = 6, column = 1)

		self.lblRating = Label(DFrameR, font = ('Arial', 16, 'bold'), text = "Rating (Out of 5):", padx = 2, pady = 2, bg = "black", fg = "dark turquoise")
		self.lblRating.grid(row = 7, column = 0, sticky = W) 
		self.txtRating = Entry(DFrameR, font = ('Arial', 16, 'bold'), textvariable = Rating, width = 39, bg = "black", fg = "white")
		self.txtRating.grid(row = 7, column = 1)

		#ListBox & ScrollBar
		scroll_bar = Scrollbar(DFrameL)
		scroll_bar.grid(row = 0, column = 1, sticky = 'ns')

		MovieList = Listbox(DFrameL, width = 41, height = 16, font = ('Helvetica', 12, 'bold'), bg = "grey27", fg = "cyan", yscrollcommand = scroll_bar.set)
		MovieList.grid(row = 0, column = 0, padx = 8)
		scroll_bar.config(command = MovieList.yview)

		#Buttons
		self.button_add = Button(BFrame, text = "Add New", font = ('Helvetica', 16, 'bold'), width = 8, height = 1, bd = 4, bg = "grey77", command = insert_data)
		self.button_add.grid(row = 0, column = 0, padx = 5)

		self.button_display = Button(BFrame, text = "Display", font = ('Helvetica', 16, 'bold'), width = 8, height = 1, bd = 4, bg = "grey77", command = display_data)
		self.button_display.grid(row = 0, column = 1, padx = 5)

		self.button_clear = Button(BFrame, text = "Clear", font = ('Helvetica', 16, 'bold'), width = 8, height = 1, bd = 4, bg = "grey77", command = clear_fields)
		self.button_clear.grid(row = 0, column = 2, padx = 5)

		self.button_search = Button(BFrame, text = "Search", font = ('Helvetica', 16, 'bold'), width = 8, height = 1, padx = 2, pady = 2, bd = 4, bg = "grey77", command = search_data)
		self.button_search.grid(row = 0, column = 3, padx = 5)

		self.button_delete = Button(BFrame, text = "Delete", font = ('Helvetica', 16, 'bold'), width = 8, height = 1, bd = 4, bg = "grey77", command = delete_data)
		self.button_delete.grid(row = 0, column = 4, padx = 5)

		self.button_update = Button(BFrame, text = "Update", font = ('Helvetica', 16, 'bold'), width = 8, height = 1, bd = 4, bg = "grey77", command = update_data)
		self.button_update.grid(row = 0, column = 5, padx = 5)

		self.button_info = Button(BFrame, text = "Instructions", font = ('Helvetica', 16, 'bold'), width = 11, height = 1, padx = 2, pady = 2, bd = 4, bg = "grey77", command = instructions_bulletin)
		self.button_info.grid(row = 0, column = 6, padx = 5)

		self.button_booking = Button(BFrame, text = "Book", font = ('Helvetica', 16, 'bold'), width = 8, height = 1, padx = 2, pady = 2, bd = 4, bg = "grey77", command = book_movie)
		self.button_booking.grid(row = 0, column = 7, padx = 5)

		self.button_exit = Button(BFrame, text = "Exit", font = ('Helvetica', 16, 'bold'), width = 8, height = 1, bd = 4, bg = "grey77", command = exit_window)
		self.button_exit.grid(row = 0, column = 8,  padx = 5)

if __name__ == '__main__':
	root = Tk()
	database = MovieBooker(root)
	root.mainloop()
