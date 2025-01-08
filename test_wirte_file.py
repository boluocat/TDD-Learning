import unittest
import os

# Function to be tested
def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

class TestFileWriting(unittest.TestCase):

    def setUp(self):
        """Set up test environment (e.g., create temp files)"""
        self.filename = 'test_file.txt'
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_to_file(self):
        """Test if a file is written correctly"""
        content = "Hello, world!"
        write_to_file(self.filename, content)
        
        # Check if the file was created
        self.assertTrue(os.path.exists(self.filename), "File was not created.")
        
        # Check if the content written to the file is correct
        with open(self.filename, 'r') as f:
            file_content = f.read()
            self.assertEqual(file_content, content, "File content does not match.")

    def tearDown(self):
        """Clean up after test (e.g., remove files)"""
        if os.path.exists(self.filename):
            os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()
