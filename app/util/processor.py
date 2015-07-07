class Color_Mixer:
   
    def __init__(self):
        self.red = 0
        self.blue = 0
        self.green = 0
        self.white = 0
    def color_processor(self, color):
        if color=="RED":
            self.red=self.red+1

        elif color=="GREEN":
            self.green=1+self.green

        elif color=="BLUE":
            self.blue=self.blue+1
    
        elif color=="WHITE":
            self.white=1+self.white
        
        print color
        print self.red,self.blue,self.green,self.white

        




#$("button").click(function(){
#        $.post("demo_test_post.asp",
#                {
#                            name: "Donald Duck",
#                                    city: "Duckburg"
#                                        },
#                    function(data, status){
#                                alert("Data: " + data + "\nStatus: " + status);
#                                    });
#                    });i
        
