# Function to group anagrams together from given
# list of words
def groupAnagrams(words):

	# sort each word in the list
	A = [''.join(sorted(word)) for word in words]

	# construct a dictionary where key is each sorted word
	# and value is list of indices where it is present
	dict = {}
	for i, e in enumerate(A):
		dict.setdefault(e, []).append(i)

	# traverse the dictionary and read indices for each sorted key.
	# The anagrams are present in actual list at those indices
	for index in dict.values():
		print([words[i] for i in index])


# Group anagrams together from given list of words
if __name__ == '__main__':

	# list of words
	words = [
		"CARS", "REPAID", "DUES", "NOSE", "SIGNED", "LANE",
		"PAIRED", "ARCS", "GRAB", "USED", "ONES", "BRAG",
		"SUED", "LEAN", "SCAR", "DESIGN"]

	groupAnagrams(words)
