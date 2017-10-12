from calvin.actor.actor import Actor, manage, condition, calvinsys, stateguard


class List_to_file(Actor):

    """
    Store data in a list then sends to a file after a number of data is stored in the list
  
    Input:
      token : data to write
    """
    @manage(["numbers"])
    def init(self):
        self.numbers=[]
        
    def write_to_file(self, x):

        wf=open("input.txt","w")
        for line in x:
            wf.write(str(line))
            wf.write("\n")
        wf.write("--------------------------------------------------")
        wf.write("\n")
        wf.close()

    @condition(action_input=['token'])
    def add_to_a_list(self, token):
        self.numbers.append(token)
        if (len(self.numbers) == 500):
            self.write_to_file(self.numbers)
            #del self.numbers[:]
            self.numbers=[]
    
    action_priority = (add_to_a_list, )
