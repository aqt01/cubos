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
        
        print function
        print "Colors count"
        print self.red,self.blue,self.green,self.white
        print "Functions count"
        print self.flash, self.strobe, self.fade, self.smooth
