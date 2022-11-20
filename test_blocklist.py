from blocklist import BlockList
import unittest

class BlockListTests(unittest.TestCase):
    def test_block(self):
        blocklist = BlockList(file_path="tests/usernames.txt")
        usernames = blocklist.read()
        blocked = blocklist.block(usernames, unblock=True)        
        self.assertEqual(True, blocked)
    def test_search_in_followers(self):       
        blocklist = BlockList(
            	           filters=[
            	               "chatonildo",
            	           ]
            	       )           
        results = blocklist.find_followers() 
        returned = True if len(results) > 0 else False  
                                                
        self.assertEqual(True, returned)

