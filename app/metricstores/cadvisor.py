import requests


class CadvisorMetricStore(object):
    def __init__(self, config):
        self.config = config

    def get_metric_value(self, metric_query):
        cadvisor_url = self.config['url']
        cadvisor_query_url = "{}/api/v1/query".format(cadvisor_url)
        response = requests.get(cadvisor_query_url, params=dict(query=metric_query))
        response_json = response.json()
        return float(response_json['data']['result'][1])
