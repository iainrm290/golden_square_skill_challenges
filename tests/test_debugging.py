# # Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# # Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
# #   Actual: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL

# from lib.pair_debugging import *

# def test_debugging_encode():
#     result = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
#     assert result == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"


# #  Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# # Expected: theswiftfoxjumpedoverthelazydog
# #   Actual: theswiftfoxjumpedoverthelazydog

# def test_debugging_decode():
#     result = decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
#     assert result == "theswiftfoxjumpedoverthelazydog"