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

class Color_Proc:
   
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
        
        
    # Reset all values
    def reset_values(self):
        self.red = 0
        self.blue = 0
        self.green = 0
        self.white = 0

        # Functions
        self.flash = 0
        self.strobe = 0
        self.fade = 0
        self.smooth = 0
        
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

    # Calculates the color mix of Red, Green, or Blue

    def color_mixer(self, color, max_color_clicked):
        """
        COLOR MAPPING
        0:  RED
        1:
        2:  PINK
        3:  
        4:  YELLOW
        5:  GREEN
        6:  LIGHT GREEN
        7:  
        8:
        9:
        10: BLUE
        11: 
        12: PURPLE
        13: 
        14: PINK
        15: WHITE
        """
 
        total = self.red + self.green + self.blue + self.white

# Gets the total color if the color clicked has 40% or more of the total clicks
        
        if ( max_color_clicked >= (0.4*total)):
            if (color=='RED'):
                return 0
            elif (color=='GREEN'):
                return 5
            elif (color=='BLUE'):
                return 10
            elif (color=='WHITE'):
                return 15

        elif ( ( max_color_clicked < (0.39*total) ) and (max_color_clicked) >= (0.32*total) ):
            if (color=='RED'):
                return 1
            elif (color=='GREEN'):
                return 6
            elif (color=='BLUE'):
                return 11
            elif (color=='WHITE'):
                return 15

        elif ( ( max_color_clicked < (0.32*total) ) and (max_color_clicked) >= (0.24*total) ):
            if (color=='RED'):
                return 2
            elif (color=='GREEN'):
                return 7
            elif (color=='BLUE'):
                return 12
            elif (color=='WHITE'):
                return 15


        elif ( ( max_color_clicked < (0.16*total) ) and (max_color_clicked) >= (0.8*total) ):
            if (color=='RED'):
                return 3
            elif (color=='GREEN'):
                return 8
            elif (color=='BLUE'):
                return 13
            elif (color=='WHITE'):
                return 15

        elif ( ( max_color_clicked <= (0.8*total)) ):
            if (color=='RED'):
                return 4
            elif (color=='GREEN'):
                return 9
            elif (color=='BLUE'):
                return 14
            elif (color=='WHITE'):
                return 15
        else:
            return 15


            
    def fn_to_snd(self,fn):
        if (fn is not 21):
            # We assume that the cube is always off
            # TURN ON CUBE WITH 20
            print 20
            print "FUNCTION:"
            print fn
        else:
            print "FUNCTION"
            print fn 
    
    # print the most clicked button
    def total_cal(self):
    
        """

        FUNCTION MAPPING
        16: FLASH
        17: STROBE
        18: FADE
        19: SMOOTH
        20: ON
        21: OFF

        """
        list_functions = {'RED':self.red, 'GREEN':self.green, 'BLUE':self.blue, 'WHITE':self.white, 'FLASH':self.flash, 'STROBE':self.strobe, 'FADE':self.fade, 'SMOOTH':self.smooth }

        # name of functino
        max_val_func = max(list_functions,key=list_functions.get)
        # value of times clicked
        value_time = max(list_functions.values() )
        print "--------------------"
        print "MAX VAL"
        print max_val_func
        print "TOTAL"
        print value_time


        # If there wasn't clicks, shutdowns the cube
        if (value_time==0):
            self.fn_to_snd(21)
            return


        # If its a color,detect the numbers of clicks and proccess it

        if ( max_val_func == 'RED' or max_val_func=='BLUE' or max_val_func=='GREEN' or max_val_func=='WHITE' ):
            self.fn_to_snd( self.color_mixer(max_val_func,value_time) )
        
        elif (max_val_func=='FLASH'):
            self.fn_to_snd(16)
        elif (max_val_func=='STROBE'):
            self.fn_to_snd(17)
        elif (max_val_func=='FADE'):
            self.fn_to_snd(18)
        elif (max_val_func=='SMOOTH'):
            self.fn_to_snd(19)

        

        #Must reset value
        self.reset_values()
    



