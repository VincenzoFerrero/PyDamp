"""
This module is responsible for managing a CLI, allowing users
to input information through a guided process.
"""

import sys
from prompt_toolkit.validation import Validator, ValidationError
from PyInquirer import prompt


class DB:
    """
    Wrapper around a Postgres connection, can be used for dependency injection
    for testing purposes.
    """
    def __init__(self, connection):
        self._connection = connection

    def fetch_lca_types(self):
        """Fetches all LCA Type data."""
        sql = "SELECT * from lca_type"
        cursor = self._connection.cursor()
        cursor.execute(sql)

        return cursor.fetchall()


class PyDampCLI:
    """Runs the CLI given a DB connection."""

    def __init__(self, product_dict, db):
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


class LCAFieldValidator(Validator):
    """Validates LCA metric names."""
    def validate(self, document):
        if document.text.strip() == "":
            raise ValidationError(
                message='Cannot be empty',
                cursor_position=len(document.text))
        return True


class LCAPrompt:
    """
    LCA Data Entry Prompt, uses product data from YAML parsing
    and a database wrapper instance (used for data retrieval ONLY).
    """
    def __init__(self, product_dict, db):
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
            # handles difficult field names like $
            field = '"%s"' % field
            if metric.strip() != "":
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


    def ask_new_lca_type(self):
        """Prompts the User to enter a new LCA Type."""
        lca_type_prompt = {
            'type': 'input',
            'name': 'lca_type',
            'message': 'Enter the new LCA Type name',
            'validate': LCAFieldValidator
        }
        answer = prompt(lca_type_prompt)
        return answer['lca_type']


    def ask_new_field(self):
        """Prompts the User to enter a new LCA metric."""
        lca_field_prompt = {
            'type': 'input',
            'name': 'lca_field',
            'message': 'Enter the new LCA metric name',
            'validate': LCAFieldValidator
        }
        answer = prompt(lca_field_prompt)
        return answer['lca_field']


    def ask_continue_new_fields(self):
        """
        Prompts the User to confirm whether they want to add another field.
        """
        continue_prompt = {
            'type': 'confirm',
            'message': 'Add another field?',
            'name': 'continue',
            'default': True
        }
        answer = prompt(continue_prompt)

        return answer['continue']

    
    def ask_lifespan(self):
        """
        Prompts the User to enter a lifespan for the product.
        """
        lca_field_prompt = {
            'type': 'input',
            'name': 'lifespan',
            'message': 'Enter the product lifespan',
            'validate': LCAMetricValidator
        }
        answer = prompt(lca_field_prompt)
        return answer['lifespan']

    
    def input_lca_data(self, lca_names, lca_types):
        """Handles input of data for new/existing LCA types."""
        lca_type_entry = self.ask_lca_type(lca_names)

        if lca_type_entry != 'Other':
            lca_match = None
            for lca_type in lca_types:
                if lca_type[0] == lca_type_entry:
                    lca_match = lca_type
            
            entry = self.ask_lca_metrics(lca_match)
            # NOTE: we may want to add a check here to ensure that at least
            # one metric isn't empty
            return {lca_match[0]: entry}
        else:
            if self.ask_new_lca():
                new_lca_type = self.ask_new_lca_type()

                # TODO: handle duplicates

                is_adding_fields = True
                entry = {}

                while is_adding_fields:
                    field = self.ask_new_field()
                    value = self.ask_lca_metric(field)
                    entry['"%s"' % field] = value

                    is_adding_fields = self.ask_continue_new_fields()
            
                return {new_lca_type: entry}


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

        # ask for lifespan once, then apply to all entries
        lifespan = self.ask_lifespan()

        while is_running:
            print("Entering LCA Information. Press Ctrl+C to quit.\n")

            lca_types = self._db.fetch_lca_types()
            lca_names = [t[0] for t in lca_types]

            entry = self.input_lca_data(lca_names, lca_types)
            if lifespan:
                for _, metrics in entry.items():
                    metrics['lifespan'] = lifespan
            results.append(entry)
            
            is_running = self.ask_continue()

        if self.ask_commit(results):
            self._product_dict['LCA_Data'] = results
        else:
            if self.ask_start_over():
                self.run()
            else:
                print("Exiting PyDamp.")
                sys.exit()
