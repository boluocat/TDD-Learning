'''
Using Mocking to test the create_table_in_db function
'''

import unittest
from unittest.mock import MagicMock

CONTENT = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )'''


def create_table(conn):
    """
    This function is used to create a table in the database
    """
    cursor = conn.cursor()
    cursor.execute(CONTENT)
    conn.commit()


class TestDatabase(unittest.TestCase):
    """
    This class is used to test the create_table function
    """

    def setUp(self):
        """Set up the mock database connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor

    def test_table_creation(self):
        """Test if a table creation query is executed"""
        create_table(self.mock_conn)

        # Verify that the correct SQL query was executed
        self.mock_cursor.execute.assert_called_with(CONTENT)

    def tearDown(self):
        """Clean up"""
        pass

if __name__ == '__main__':
    unittest.main()
