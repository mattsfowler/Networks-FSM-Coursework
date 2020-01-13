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

    def passiveOpen(self):
        print("ERROR: no transition")
        return False

    def syn(self):
        print("ERROR: no transition")
        return False

    def ack(self):
        print("ERROR: no transition")
        return False

    def fin(self):
        print("ERROR: no transition")
        return False

    def close(self):
        print("ERROR: no transition")
        return False

    def timeout(self):
        print("ERROR: no transition")
        return False


class ClosedState(State, Transition):
    pass


class ListenState(State, Transition):
    pass


class SynRecievedState(State, Transition):
    pass


class EstablishedState(State, Transition):
    pass


class CloseWaitState(State, Transition):
    pass


class LastAckState(State, Transition):
    pass



