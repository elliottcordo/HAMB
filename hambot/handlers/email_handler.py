"""
email handler
"""

import json, os
import pandas as pd
from datetime import datetime
from cocore.config import Config
from coutils.email_tools import Email

CONF = Config()


class Handler(object):
    """

    """
    @staticmethod
    def run(result, conf):
        """

        :param result:
        :param conf:
        :return:
        """
        recipients = conf.split(' ')
        environment = CONF['hambot']['environment']
        if environment == 'dev':
            print(f'environment: {environment}')
            return
        aws_conf = CONF['aws']
        level = result['summary']['status']
        manifest = result['summary']['manifest']
        subject = str(environment).upper() + str(' Hambot %s: %s' % (level, manifest)).title()

        with_attachment = os.path.exists('diagnostic_query_results.csv')

        if level == 'success' or not with_attachment:
            json_msg = json.dumps(result, indent=4, default=json_serial)
            Email.send_mail(aws_access_key=aws_conf['aws_id'], aws_secret_key=aws_conf['aws_key'], aws_sender=aws_conf['ses_def_sender'],
                            aws_region=aws_conf['ses_region'], to_addr=recipients,
                        subject=subject, text_msg=json_msg)
        
        else:
            json_msg = json.dumps(result, indent=4, default=json_serial).replace(' ', '&nbsp;').replace('\n', '<br>')
            Email.send_email_with_attachment(aws_access_key=aws_conf['aws_id'], aws_secret_key=aws_conf['aws_key'], 
                        aws_sender=aws_conf['ses_def_sender'], aws_region=aws_conf['ses_region'], to_addr=recipients,
                        subject=subject, body_msg=json_msg, filename='diagnostic_query_results.csv')
            os.remove('diagnostic_query_results.csv')


def render_html(result):
        """
        builds html message
        :return:
        """
        html = """<table border="1" cellpadding="0" cellspacing="0" bordercolor=#BLACK>"""
        html += "<tr> <td> Jobs     Status </td> </tr>"
            # Make <tr>-pairs, then join them.
        #html += "\n".join(
            # map(lambda x: """<td style="width: 175px;">""" + str(result) + "</td>", 1))
        html += "<tr> <td>"
        html += str(result)
        html += "</td> </tr>"
        html += "</table> <br><br><i>]</i>"
        return html


def json_serial(data):
    """
    JSON serializer for objects not serializable by default json code"
    :param obj:
    :return:
    """

    if isinstance(data, pd.DataFrame):
        table = data.to_json(orient='split')
        table = table.replace('\"' , '')
        x= table.split('data', 1)
        return x[1]
    elif isinstance(data, datetime):
        serial = data.isoformat()
        return serial
    raise TypeError("Type not serializable")

