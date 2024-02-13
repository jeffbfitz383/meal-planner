
###############class init

class <class_name>:
    def __init__(self, <>):
        self.<> = <>                    ######example <> = title or username

 ######################property with validation##########################
 def get_<>(self):
        return self._<>
    def set_<>(self, value):
        # print(value)
        if type(value) is str and 0<len(value) and not hasattr(self,"<>")
        #if type(value) is str and 2<=len(value)<=16:
        #if type(value) is int and 1<=value<=5000 and not hasattr(self,"score"):
            self._<> = value
        else:
            print("NOT VALID TITLE")
    <> = property(get_<>,set_<>)
    

################################# property that returns type

ie result property player

   def get_<>(self):
        return self._<>
    def set_<>(self, value):
        if type(value) is <C>:
            self._<> = value
        else:
            print("NOT VALID <>")
    <> = property(get_<>,set_<>)

    ############return a list of all results ie player results ###############

Player results()

Returns a list of all results for that player
Results must be of type Result
  
    def results(self):
        # [Result(),Result()]
        # Loop through every result in existance
        # print(Result.all)
        return_list = []
        for r in Result.all:
            if r.player is self:
                return_list.append(r)
        return return_list



        ######################
        returns a list of all games played for that players

           def games_played(self):
        return_list = []
        # Loop through all the results attatched to this player
        for my_r in self.results():
            #Check if game is in our list, if not add it
            if my_r.game not in return_list:
                return_list.append(my_r.game)
        return return_list



        ##################################################finding average###############
            def average_score(self, player):
        # Loop through all results of the player
        sum = 0
        count = 0
        for r in player.results():
            # Check if game is self 
            if r.game is self:
            # Calculate sum
                sum = sum + r.score 
                count += 1
            # Divide by amount of results
        return sum/len(player.results())
        # return sum/player.num_times_played(self)
        pass