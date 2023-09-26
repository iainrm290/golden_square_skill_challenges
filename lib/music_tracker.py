'''
Problem:

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them

'''
# Class design:
    # Name: MusicTracker


    # Methods: 
        # __init__(self):
            # tracks held in a list []
    
        # add(self, track):
            # returns nothing
            # updates track list as a side effect
        
        # view_tracks():
            # returns list of tracks
            # no side effects


class MusicTracker:
    def __init__(self) -> None:
        self.track_list = []

    def add(self, track):
        if track == "":
            raise Exception("You give a track name to add it to the list.")
        self.track_list.append(track)
    
    def view_tracks(self):
        if self.track_list == []:
            raise Exception("You haven't listened to anything.")
        return f"You have listened to: {','.join(self.track_list).rstrip(',')}."