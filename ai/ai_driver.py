'''
    The ai_driver main is the top level function used by the Wingspan AI.
    In it, a boardstate is configured, made modifiable, and mutated by an AI with realtime tunable parameters.
    The output is the AI's recommended single move or move sequence given the initial board state.
'''
def main():
    
    # program init
        #TODO: initalize everything to memory; birds, bird functions, etc.
    
    # make a boardstate
        #TODO: create and initialize a BoardState object
        
        
    # while Wingspan is being played
        
        # tune AI parameters
        #TODO: choose the ply, preference, and other generic weights the AI will use
        
        # run the AI
        #TODO: pass the boardstate to the parameterized AI, return a move or sequence of moves
        
        # update the boardstate
        #TODO: based on the player's move, update the boardstate accordingly 
    return

if __name__=="__main__":
    try:
        main()
    except:
        print("Failed main")