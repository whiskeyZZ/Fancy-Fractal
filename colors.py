class Color:
    frac_color = [1, "green"]
    speed = 5
    
    def get_color(self):
        return self.frac_color

    def set_color(self, new_color):
        self.frac_color = new_color

    def get_speed(self):
        return self.speed
    
    def set_speed(self, new_speed):
        self.speed = new_speed
    