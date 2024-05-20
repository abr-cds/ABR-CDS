# Importing necessary packages to be used
from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog as tkFileDialog
import cv2
from tkinter import messagebox
# This func is called whenever the 'Select an image' button is clicked
def select_image():
    # grab a reference to the image canvas and the path variable
    global canvas
    global path
    
    canvas.delete("all")
    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkFileDialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0 and path[-4:] == '.jpg':
        # load the image from disk
        image = cv2.imread(path)
        original_image = image.copy()

        #  represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (675, 300))

        # convert the images to PIL format...
        image = Image.fromarray(image)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)

        canvas.image = image
        canvas.create_image(0, 0, anchor=NW, image=image) 
    else:
        messagebox.showinfo("Warning","Please choose an image! (It should be a .jpg file)")
                
# Submit the image for preprocessing if the image path is valid and the currency type is chosen
def submit():
    global path
    global selectedImage
    if len(path) <= 0:
        messagebox.showinfo("Warning","Please choose an image!")
    else:
        print(path)
        selectedImage = True
        messagebox.showinfo("Info","Image sent for processing!")
        root.destroy()

# Exit window
def exit_window():
    root.destroy()

    
# Main function
# Declaring root window
root = Tk() 
root.title("ABR Counterfeit Detection System")

# Declaring the attributes of the GUI window
root.resizable(False, False)  # This code helps to disable windows from resizing

window_height = 600
window_width = 1100

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# Declaring variables
path = ""                      # Stores path of image selected
selectedImage = False

# create all of the main containers
top_frame = Frame(root, width=1090, height=50, pady=3)
frame1 = Frame(root, width=1090, height=80, padx=3, pady=3)
frame2 = Frame(root, bg='red', width=1090, height=400, pady=5, padx = 5)
frame3 = Frame(root, width=1090, height=50, pady=3)
frame4 = Frame(root, width=1090, height=50, pady=3)
frame5 = Frame(root, width=1090, height=20, pady=3)

# Assigning all frames in a grid layout on the root window
top_frame.grid(row = 1, column = 1, padx = 5, pady = 5)
frame1.grid(row = 2, column = 1, padx = 5, pady = 5)
frame2.grid(row = 3, column = 1, padx = 5, pady = 5)
frame3.grid(row = 4, column = 1, padx = 5, pady = 5)
frame4.grid(row = 5, column = 1, padx = 5, pady = 5)
frame5.grid(row = 6, column = 1, padx = 5, pady = 5)

# Title label
title = Label(master=top_frame, text="ABR Counterfeit Detection System", fg = 'white', font = "audiowide 28 bold")
title.pack() # Put the label into the window

# Text label
text1 = Label(master=frame1, text="Please browse your image file to get started!", fg='white', font="audiowide 10")
text1.pack() 

# Creating a canvas to display the image
canvas = Canvas(master=frame2, width = 675, height = 300)  
canvas.pack()  

# Text label
# text1 = Label(master=frame3, text="Select currency type: ", fg = 'white', font = "audiowide 12")
# text1.pack(side = 'left') 

# R2 = Radiobutton(master=frame3, text="1000", font = "audiowide 15")
# R2.pack(anchor =  W)

# Button to browse the image
btn = Button(master = frame4, text="SELECT AN IMAGE", command=select_image, font = "audiowide 15 bold", fg='white')
btn.pack(side = 'left', padx=10, pady=10)

# Button to submit the image
btn = Button(master = frame4, text="SUBMIT", command=submit, font = "audiowide 15 bold", fg='white')
btn.pack(side = 'left', padx=10, pady=10)

# Button to exit window
btn = Button(master = frame4, text="EXIT", command=exit_window, font = "audiowide 15 bold", fg='white')
btn.pack(side = 'left', padx=10, pady=10)

# Open the root window
root.mainloop()