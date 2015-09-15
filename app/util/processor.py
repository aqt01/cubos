import sched, time
from threading import Timer


#Taked from http://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

class Color_Mixer:
   
    def __init__(self):
        self.red = 0
        self.blue = 0
        self.green = 0
        self.white = 0

        # Functions
        self.flash = 0
        self.strobe = 0
        self.fade = 0
        self.smooth = 0
        
        self.s = sched.scheduler(time.time,time.sleep)
        


    def color_processor(self, function):
               # Color count
        if function=="RED":
            self.red=self.red+1

        elif function=="GREEN":
            self.green=1+self.green

        elif function=="BLUE":
            self.blue=self.blue+1
    
        elif function=="WHITE":
            self.white=1+self.white
 
         # Function count
       
        elif function=="FLASH":
            self.flash=self.flash+1
        
        elif function=="STROBE":
            self.strobe=1+self.strobe

        elif function=="FADE":
            self.fade=self.fade+1
    
        elif function=="SMOOTH":
            self.smooth=1+self.smooth
        """
        print function
        print "Colors count"
        print self.red,self.blue,self.green,self.white
        print "Functions count"
        print self.flash, self.strobe, self.fade, self.smooth
        """

    # print the most clicked button
    def total_cal(self):
        list_functions = {0:self.red, 1:self.green, 2:self.blue, 3:self.white, 4:self.flash, 5:self.strobe, 6:self.fade, 7:self.smooth }
        print max(list_functions,key=list_functions.get)

        #Must reset value

    



