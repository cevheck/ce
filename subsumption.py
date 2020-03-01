import _thread
import time

class Behavior(object):

    def __init__(self):
        pass

    def takeControl(self):
        raise NotImplementedError

    def action(self):
        raise NotImplementedError

    def suppress(self):
        raise NotImplementedError

class Controller():

    lock = _thread.allocate_lock()

    def __init__(self, return_when_inactive=None):

        if return_when_inactive is None:
            self.return_when_inactive = False
        else:
            self.return_when_inactive = return_when_inactive

        self.behaviors = []
        self.active = None
        self.highestPriority = None

        self.running = True

    def add(self, behavior):

        self.behaviors.append(behavior)


    def find_new_active_behavior(self):

        #iterate over all behaviors and return behavior with lowest index that has takeControl true

        for priority, behavior in enumerate(self.behaviors):

            if behavior.takeControl():
                return priority

        return None


    def find_and_set_new_active_behavior(self):

        #find the new behavior with highest priority

        self.highestPriority = self.find_new_active_behavior()
        
        if self.highestPriority is not None:

            if self.active is None or self.active > self.highestPriority:

                if self.active is not None:
                    self.behaviors[self.active].suppress()

    
    def monitor(self):

        while self.running:

            with self.lock:
                
                self.find_and_set_new_active_behavior()

            #time.sleep(0.05)

    def start(self):
        
        self.running = True
        self.find_and_set_new_active_behavior()

        _thread.start_new_thread(self.monitor, ())

        while self.running:
            
            with self.lock:

                if self.highestPriority is not None:
                    self.active = self.highestPriority
                elif self.return_when_inactive:
                    self.running = False
                    break

            if (self.active is not None):

                self.behaviors[self.active].action()
                self.active = None
