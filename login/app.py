import customtkinter as ctk
import frame
#create a window
class Open_window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x750")
        self.title("Authentication System")
        #create a frame
        self.Main_frame=frame.mainframe(self)
        self.Main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.frames={}

    def Main(self):
        self.destroy_all_frames()
        self.title("Login")
        self.Main_frame=frame.mainframe(self)
        self.Main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.frames["main"]=self.Main_frame

    def Login(self):
        self.Main_frame.destroy()
        self.title("Logging in")
        self.log_frame=frame.loginframe(self)
        self.log_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.frames["login"]=self.log_frame

    def Forgot_p(self):
        self.Main_frame.destroy()
        self.title("Forgot Password")
        self.data={}
        self.forgot_p_frames=[frame.forgotframe_1(self, self.data), frame.forgotframe_2(self, self.data), frame.forgotframe_3(self, self.data)]
        self.forgot_p_frames[1].forget()
        self.forgot_p_frames[2].forget()
        self.frame_index=0
        self.forgot_p_frames[self.frame_index].place(relx=0, rely=0, relheight=1, relwidth=1)

    def Signup(self):
        self.Main_frame.destroy()
        self.title("Register")
        self.data={}
        self.signin_frames=[frame.signupframe_1(self, self.data), frame.signupframe_2(self, self.data)]
        self.signin_frames[1].forget()
        self.frame_index=0
        self.signin_frames[self.frame_index].place(relx=0, rely=0, relheight=1, relwidth=1)


    def destroy_all_frames(self):
        for frame_name, frame in self.frames.items():
            frame.destroy()
        self.frames={}