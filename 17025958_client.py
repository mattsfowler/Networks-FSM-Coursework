# ------------- COMMON STATE CODE ------------- #

class State:
    
    CurrentContext = None
    
    def __init__(self, Context):
        self.CurrentContext = Context

    def trigger(self):
        return True


class StateContext:

    state = None
    CurrentState = None
    availableStates = {}

    def setState(self, newstate):
        try:
            self.CurrentState = self.availableStates[newstate]
            self.state = newState
            self.CurrentState.trigger()
            return True
        except KeyError:    #incorrect state key specified
            return False

    def getStateIndex(self):
        return self.state


# ------------- END OF COMMON CODE ------------- #


class Transition:

    def activeOpen(self):
        print("ERROR: no transition")
        return False

    def rts(self):
        print("ERROR: no transition")
        return False

    def timeout(self):
        print("ERROR: no transition")
        return False

    def synAck(self):
        print("ERROR: no transition")
        return False

    def close(self):
        print("ERROR: no transition")
        return False

    def ack(self):
        print("ERROR: no transition")
        return False

    def fin(self):
        print("ERROR: no transition")
        return False


class ClosedState(State, Transition):
    pass


class SynSentState(State, Transition):
    pass


class EstablishedState(State, Transition):
    pass


class FinWaitOneState(State, Transition):
    pass


class FinWaitTwoState(State, Transition):
    pass


class TimedWaitState(State, Transition):
    pass




