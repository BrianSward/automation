import re


def find_phone_numbers(text_file):
	with open(text_file, "r") as f:
		text_from_file = f.read()
	pattern = r"(?:\(\d{3}\)|\d{3})[-. ]?\d{3}[-. ]?\d{4}"
	phone_nums = re.findall(pattern, text_from_file)
	bucket = []
	for nums__ in phone_nums:
		if len(nums__) != 10:
			nums__ = nums__.replace("(", "")
			nums__ = nums__.replace(")", "-")
			nums__ = nums__.replace(".", "-")
			bucket.append(nums__)
	results = [*set(bucket)]
	sorted_results = sorted(results)
	with open("phone_numbers.txt", 'w') as fp:
		for item in sorted_results:
			fp.write("%s\n" % item)
	return


def find_email_address(text_file):
	with open(text_file, "r") as f:
		text_from_file = f.read()
	pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
	emails = re.findall(pattern, text_from_file)
	results = [*set(emails)]
	sorted_results = sorted(results)
	with open("emails.txt", 'w') as fp:
		for item in sorted_results:
			fp.write("%s\n" % item)
	return


if __name__ == "__main__":
	find_email_address("potential_contacts.txt")
	find_phone_numbers("potential_contacts.txt")
