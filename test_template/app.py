import logging
from tomllib import load

import logging_loki

from .email_functions.email import EmailUsers
from .math_functions.basic_functions import add, div, mult, sub


class TestTemplate:

    @staticmethod
    def run():

        #***************************************#
        #*     SETUP ENVIRONMENT VARIABLES     *#
        #***************************************#

        with open("config.toml", "rb") as config:
            data = load(config)

        ADD_1 = data['ADD_1']
        ADD_2 = data['ADD_2']

        SUB_1 = data['SUB_1']
        SUB_2 = data['SUB_2']

        MULT_1 = data['MULT_1']
        MULT_2 = data['MULT_2']

        DIV_1 = data['DIV_1']
        DIV_2 = data['DIV_2']

        GRAFANA_URL = data['GRAFANA_URL']
        GRAFANA_USERNAME = data['GRAFANA_USERNAME']
        GRAFANA_PASSWORD = data['GRAFANA_PASSWORD']
        GRAFANA_VERSION = data['GRAFANA_VERSION']
        GRAFANA_TAGS = data['GRAFANA_TAGS']

        #***************************************#
        #*           SETUP LOGGING             *#
        #***************************************#

        handler = logging_loki.LokiHandler(
            url=GRAFANA_URL,
            tags=GRAFANA_TAGS,
            auth=(GRAFANA_USERNAME, GRAFANA_PASSWORD),
            version=GRAFANA_VERSION,
        )

        logger = logging.getLogger("test-template-logger")
        logger.addHandler(handler)
        logger.level=logging.INFO

        logger.info("Testing Our Template Repo",
                     extra={"tags": {"service": "main"}})

        #****************************************#
        #*            MATH OPERATIONS           *#
        #*****************************************

        add_result = add(ADD_1, ADD_2)
        sub_result = sub(SUB_1, SUB_2)
        mult_result = mult(MULT_1, MULT_2)

        try:
            div_result = div(DIV_1, DIV_2)
        except ZeroDivisionError:
            div_result = 'NaN'
            logger.error(f"Divide by zero error. Could not divide {DIV_1} by {DIV_2}.",
                         extra={"tags": {"service": "main"}})

        alert_email = EmailUsers('jared.paquette@baycollege.edu', 'test.repo@baycollege.edu')
        alert_email.create_subject("Test Template Repo")
        
        alert_message = f"""
        The results of our math operations.

        ADD: {add_result}
        SUB: {sub_result}
        MULT: {mult_result}
        DIV: {div_result}
        """
        
        alert_email.create_message(alert_message)
        alert_email.send_email()

        print(GRAFANA_TAGS)
