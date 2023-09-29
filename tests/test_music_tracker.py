# from lib.music_tracker import *
# import pytest

# # track_list_is_updated_given_track_name
# def test_track_list_is_updated_given_track_name():
#     music_tracker = MusicTracker()
#     music_tracker.add("Held")
#     result = music_tracker.track_list
#     assert result == ["Held"]


# # track_list_is_displayed_given_at_least_one_track
# def test_track_list_is_displayed_given_at_least_one_track():
#     music_tracker = MusicTracker()
#     music_tracker.add("Held")
#     result = music_tracker.view_tracks()
#     assert result == "You have listened to: Held."

# # raises_error_if_track_list_is_empty_when_viewed
# def test_raises_error_if_track_list_is_empty_when_viewed():
#     music_tracker = MusicTracker()
#     with pytest.raises(Exception) as e:
#         music_tracker.view_tracks()
#     error_message = str(e.value)
#     assert error_message == "You haven't listened to anything."


# # raises_error_given_empty_track_name
# def test_raises_error_given_empty_track_name():
#     music_tracker = MusicTracker()
#     with pytest.raises(Exception) as e:
#         music_tracker.add("")
#     error_message = str(e.value)
#     assert error_message == "You give a track name to add it to the list."