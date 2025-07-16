class LCG_Pseudo_Random_Generator:
  def __init__(self, seed=None):
    # Borland C/C++ Preset
    self.a = 22695477
    self.c = 1

    self.m = 2**31
    self.x0 = seed

    self.x_prev = (self.a * self.x0 + self.c) % self.m

  def Generate_Number(self, num_range=None):
    self.x_prev = (self.a * self.x_prev + self.c) % self.m
    
    if not num_range:
      return self.x_prev
    else:
      return int((self.x_prev / (self.m - 1)) * (num_range[1] + 1 - num_range[0]) + num_range[0])