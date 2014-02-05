class integer(object):
	def __init__(self,num, positive):
	    self.number=num
	    self.p= positive 

	def display(self):
		print self.p + str(self.num)
class negativeinteger(integer):
	def __init__(self, num):
		super(negativeinteger, self).__init(num, "-")
if __name__=="__main__":
	test=integer(12, "-")
  	test.display()




