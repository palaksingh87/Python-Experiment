class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Step 2: Sort characters by frequency (ascending), then by character
        sorted_items = sorted(freq.items(), key=lambda item: (item[1], item))

        # Step 3: Build the resulting string by repeating each character
        return "".join(char * count for char, count in sorted_items)