"""
This module is responsible for managing a CLI, allowing users
to input information through a guided process.
"""

import sys
from prompt_toolkit.validation import Validator, ValidationError
from PyInquirer import prompt


class DB:
    """Wrapper around a Postgres connection, used for dependency injection."""
    def __init__(self, connection):
        self._connection = connection

    def fetch_lca_types(self):
        """Fetches all LCA Type data."""
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


class LCAMetricValidator(Validator):
    """
    Validates LCA Metrics. Currently, all metrics must either
    be floats or null values.
    """
    def validate(self, document):
        if document.text.strip() == "":
            return True

        try:
            float(document.text)
        except ValueError:
            raise ValidationError(
                message='LCA Metrics must be numbers (or empty)',
                cursor_position=len(document.text))


class LCAPrompt:

    def __init__(self, product_dict, db):
        """
        Initializes the LCA Data Entry Prompt, using the product data from YAML parsing
        and a database wrapper instance (used for data retrieval ONLY).
        """
        self._product_dict = product_dict
        self._db = db

        self.run()

    
    def ask_lca_type(self, lca_names):
        """Prompts the User for an LCA type, or "Other"."""
        lca_names.append('Other')
        lca_prompt = {
            'type': 'list',
            'name': 'lca_type',
            'message': 'Choose an LCA Type',
            'choices': lca_names
        }
        answer = prompt(lca_prompt)
        return answer['lca_type']

    
    def ask_lca_metric(self, field):
        """Prompts the User to enter a value for a given LCA Metric."""
        metric_prompt = {
            'type': 'input',
            'name': 'metric',
            'message': 'Enter a value for field %s' % field,
            'validate': LCAMetricValidator
        }
        answer = prompt(metric_prompt)
        return answer['metric']


    def ask_lca_metrics(self, lca_type):
        """
        Iterates through LCA metric fields, prompting the User to enter 
        information for each.
        """
        (name, fields, _) = lca_type

        results = {}
        for field in fields:
            metric = self.ask_lca_metric(field)
            if metric.strip() == "":
                results[field] = metric
            else:
                results[field] = float(metric)
        
        return results

    
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

    
    def ask_new_lca(self):
        """
        Prompts the User to confirm whether they want to create a new LCA type.
        """
        new_lca_prompt = {
            'type': 'confirm',
            'message': 'Create new LCA type?',
            'name': 'new_lca',
            'default': True
        }
        answer = prompt(new_lca_prompt)

        return answer['new_lca']

    
    def ask_continue(self):
        """
        Prompts the User to confirm whether they want to add another entry.
        """
        continue_prompt = {
            'type': 'confirm',
            'message': 'Add another LCA entry?',
            'name': 'continue',
            'default': True
        }
        answer = prompt(continue_prompt)

        return answer['continue']


    def ask_commit(self, results):
        """Prompts the User to confirm LCA Data entries."""
        print('Results:\n%s' % results)
        commit_prompt = {
            'type': 'confirm',
            'message': 'Would you like to commit this data?',
            'name': 'commit',
            'default': True
        }
        answer = prompt(commit_prompt)

        return answer['commit']

    
    def ask_start_over(self):
        """Prompts the User to start over or exit the program."""
        start_over_prompt = {
            'type': 'confirm',
            'message': 'Would you like to start over?',
            'name': 'start_over',
            'default': True
        }
        answer = prompt(start_over_prompt)

        return answer['start_over']
    

    def run(self):
        """
        Runs the LCA Data entry CLI. This will only run if the value
        entered is `True`. Otherwise it will assume the user has entered
        all LCA information in YAML form.
        """
        if self._product_dict['LCA_Data'] != True:
            return

        results = []
        is_running = True

        while is_running:
            print("Entering LCA Information. Press Ctrl+C to quit.\n")
            lca_types = self._db.fetch_lca_types()
            lca_names = [t[0] for t in lca_types]
            lca_type_entry = self.ask_lca_type(lca_names)

            if lca_type_entry != 'Other':
                lca_match = None
                for lca_type in lca_types:
                    if lca_type[0] == lca_type_entry:
                        lca_match = lca_type
                
                entry = self.ask_lca_metrics(lca_match)
                # we may want to add a check here to ensure that at least
                # one metric isn't empty
                results.append({lca_match[0]: entry})
            else:
                if self.ask_new_lca():
                    pass
            
            is_running = self.ask_continue()

        if self.ask_commit(results):
            self._product_dict['LCA_Data'] = results
        else:
            if self.ask_start_over():
                self.run()
            else:
                print("Exiting PyDamp.")
                sys.exit()
