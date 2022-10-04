CHANNELS = ["BBC", "Discovery", "TV1000"]
 
class TVController:
    current_channel_num = 0
    
    def __init__(self, channels) -> None:
        self.channels = channels

    def first_channel(self):
        self.current_channel_num = 0
        return self.channels[self.current_channel_num]
    
    def last_channel(self):
        self.current_channel_num = len(self.channels) - 1
        return self.channels[self.current_channel_num]
    
    def turn_channel(self,channel_num):
        self.current_channel_num = channel_num - 1
        return self.channels[self.current_channel_num]
    
    def next_channel(self):
        self.current_channel_num = (self.current_channel_num + 1)%len(self.channels)
        return self.channels[self.current_channel_num]

    def previous_channel(self):
        self.current_channel_num = (self.current_channel_num - 1)%len(self.channels)
        return self.channels[self.current_channel_num]
    
    def current_channel(self):
        return self.channels[self.current_channel_num]
    
    def is_exist(self,channel):
        if type(channel) == int:
            if channel > 0 and channel < len(self.channels):
                return "Yes"
            else:
                return "No"
        else:
            if channel in self.channels:
                return "Yes"
            else:
                return "No"

        

        
 
controller = TVController(CHANNELS)
 
print(controller.first_channel() == "BBC")
print(controller.last_channel() == "TV1000")
print(controller.turn_channel(1) == "BBC")
print(controller.next_channel() == "Discovery")
print(controller.previous_channel() == "BBC")
print(controller.current_channel() == "BBC")
print(controller.is_exist(4) == "No")
print(controller.is_exist("BBC") == "Yes")