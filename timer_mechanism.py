

class TimerMechanism:
	def __init__(self):
		self.state = "off"
		self.checkmark = "✔"
		self.text_of_checkmarks = ""
		self.nr_of_checkmarks = 0

	def change_state(self):
		if self.state == "working" and self.nr_of_checkmarks < 3:
			self.nr_of_checkmarks += 1
			self.text_of_checkmarks += self.checkmark
			self.state = "resting"
		elif self.state == "working" and self.nr_of_checkmarks == 3:
			self.nr_of_checkmarks += 1
			self.text_of_checkmarks += self.checkmark
			self.state = "long resting"
		elif self.state == "resting":
			self.state = "working"
		elif self.state == "long resting":
			self.state = "working"
			self.nr_of_checkmarks = 0
			self.text_of_checkmarks = ""
		else:
			print("it is off")
		return self.state

	def reset_mechanism(self):
		self.state = "off"
		self.nr_of_checkmarks = 0
		self.text_of_checkmarks = ""
