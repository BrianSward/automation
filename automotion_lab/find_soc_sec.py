import re

# example of a context manager
with open("test_text.txt", "r") as f:  # open as read
	# do logic and atuff with file f, this auto closes due to with
	text_from_file = f.read()

# print(text_from_file)

# same method we used in validater
pattern = r"(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}"

# we use findall() here because search() returns just the first and
# match() only returns it if it starts with it
soc_sec_nums = re.findall(pattern, text_from_file)

print(f"there are {len(soc_sec_nums)} ssn found")
print("Here is the list:" + "\n", soc_sec_nums)