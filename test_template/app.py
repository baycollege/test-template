import logging
import os

import logging_loki
from dotenv import find_dotenv, load_dotenv

from .email_functions.email import EmailUsers
from .math_functions.basic_functions import add, div, mult, sub


class TestTemplate:

    @staticmethod
    def run():

        # *************************************** #
        # *     SETUP ENVIRONMENT VARIABLES     * #
        # *************************************** #

        load_dotenv(find_dotenv("config.env"))

        ADD_1 = int(os.environ.get('ADD_1'))
        ADD_2 = int(os.environ.get('ADD_2'))

        SUB_1 = int(os.environ.get('SUB_1'))
        SUB_2 = int(os.environ.get('SUB_2'))

        MULT_1 = int(os.environ.get('MULT_1'))
        MULT_2 = int(os.environ.get('MULT_2'))

        DIV_1 = int(os.environ.get('DIV_1'))
        DIV_2 = int(os.environ.get('DIV_2'))

        GRAFANA_URL = os.environ.get('GRAFANA_URL')
        GRAFANA_USERNAME = os.environ.get('GRAFANA_USERNAME')
        GRAFANA_PASSWORD = os.environ.get('GRAFANA_PASSWORD')

        # *************************************** #
        # *           SETUP LOGGING             * #
        # *************************************** #

        handler = logging_loki.LokiHandler(
            url=GRAFANA_URL,
            tags={"application": "test_template"},
            auth=(GRAFANA_USERNAME, GRAFANA_PASSWORD),
            version="1",
        )

        logger = logging.getLogger("test-template-logger")
        logger.addHandler(handler)
        logger.level = logging.INFO

        logger.info("Testing Our Template Repo",
                    extra={"tags": {"service": "main"}})

        # **************************************** #
        # *            MATH OPERATIONS           * #
        # **************************************** #

        add_result = add(ADD_1, ADD_2)
        sub_result = sub(SUB_1, SUB_2)
        mult_result = mult(MULT_1, MULT_2)

        try:
            div_result = div(DIV_1, DIV_2)
        except ZeroDivisionError:
            div_result = 'NaN'
            logger.error("Divide by zero error. Could not divide %d by %d.", DIV_1, DIV_2,
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

        print("Hello World!")
