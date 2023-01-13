import re

# 123-11-0033
# valid ssn format, how would computer know?
# that is to say how to validate

goodies = ["111-22-3333", "234-56-7890"]
baddies = ["666-22-1111", "000-22-3333", "900-12-1212"]


def validate(ssn):
	"""
	takes in a ssn as a string and then uses regex to validate the ssn
	"""

	# first pattern attempt
	# pattern = r"[0-9]{3}-[0-9]{2}-[0-9]{4}"  # a regex pattern
	# but this pattern is more robust
	pattern = r"(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}"
	match_obj = re.match(pattern, ssn)  # envoking .group() will show what it matched
	if match_obj:
		return True
		# return match_obj.group() since we want bool above line is good, but this is a way to see matches
	else:
		return False


if __name__ == "__main__":
	validate(goodies[0])
	validate(baddies[0])
	for ssn in goodies:
		assert validate(ssn)

	for ssn in baddies:
		assert not validate(ssn)

	print("Tests Passes!")