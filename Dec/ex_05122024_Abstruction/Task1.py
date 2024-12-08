from abc import ABC, abstractmethod

# Create a Program,# Class - PC,# Class - MotherBoard,# ab → start MotherBoard
# Class - RAM,# abstractMethod → start ram,# Class - Processor,# abstractMethod → start processor
# Class - Storage# abstractMethod → storage data,# static method-->  loadOS
# non static -->  startMouse# UseHeadPhone

class PC:
    def __init__(self):
        print("Start PC")

class MotherBoard(PC):
     @abstractmethod
     def motherboard(self):
         pass

class RAM(MotherBoard):
    @abstractmethod
    def start_ram(self):
        pass

class Processor(MotherBoard):
    @abstractmethod
    def start_processor(self):
        pass
# Class - Storage# abstractMethod → storage data,# static method-->  loadOS
# non static -->  startMouse# UseHeadPhone

class Storage:
    @abstractmethod
    def storage_data(self):
        pass

    @staticmethod
    def load_Os():
        pass

    def Start_Mouse(self):
        print("Mouse connected")

    def UseHeadPhone(self):
        print("headphone connected")


