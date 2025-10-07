
import unittest
 # from src.utils imports count_vowels not working
class testCount(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("abigail", "mahlodi"), "zilla", "samson" , "bilgates")
        
def get_max(numbers):
    if not numbers:
        return None
    return max(numbers)

def count_vowels(word):
    vowels = 'aeiou'
    return sum(1 for ch in word.lower() if ch in vowels)

if __name__ == "__main__":
    unittest.main

