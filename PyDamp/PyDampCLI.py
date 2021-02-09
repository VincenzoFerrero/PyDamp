"""
This module is responsible for managing a CLI, allowing users
to input information through a guided process.
"""

import sys


class DB:
    def __init__(self, connection):
        self._connection = connection

    def fetch_lca_types(self):
        sql = "SELECT * from lca_type"
        cursor = self._connection.cursor()
        cursor.execute(sql)

        return cursor.fetchall()


class PyDampCLI:

    def __init__(self, product_dict, db):
        """Runs the CLI given a DB connection."""
        self._product_dict = product_dict
        self._db = db

        self.run()

    def run(self):
        LCAPrompt(self._product_dict, self._db)


class LCAPrompt:

    def __init__(self, product_dict, db):
        """
        Initializes the LCA Data Entry Prompt, using the product data from YAML parsing
        and a database wrapper instance (used for data retrieval ONLY).
        """
        self._product_dict = product_dict
        self._db = db

        self.run()

    
    def validate_response(self, response):
        """
        Checks a user-provided input for validity. User inputs must either
        be empty strings or floats.
        """
        if response == None or response.strip() == '':
            return (True, '')

        try:
            return (True, float(response))
        except:
            print("\nLCA Metrics must be numbers (or empty).")
            return False


    def run(self):
        """
        Runs the LCA Data entry CLI. This will only run if the value
        entered is `True`. Otherwise it will assume the user has entered
        all LCA information in YAML form.
        """
        try:
            if self._product_dict['LCA_Data'] != True:
                return

            print("Entering LCA Information. Press Ctrl+C to quit.\n")
            lca_types = self._db.fetch_lca_types()
            lca_names = [t[0] for t in lca_types]
            print("Existing LCA Types: %s\n" % lca_names)
            lca_type_entry = input("Please enter LCA type: ")

            lca_match = None
            for lca_type in lca_types:
                if lca_type[0] == lca_type_entry:
                    lca_match = lca_type

            if lca_match:
                results = {}

                for field in lca_match[1]:
                    response = None

                    while not response:
                        val = input('Please enter a value for field "%s": ' % field)
                        response = self.validate_response(val)

                    (_, val) = response
                    results[field] = val
                
                print(results)
            else:
                print('LCA Type "%s" not found. Create New LCA Type?' % lca_type_entry)

        except KeyboardInterrupt:
            print("\nExiting LCA Data Entry.")
