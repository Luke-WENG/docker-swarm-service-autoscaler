from ..errors import UknownMetricStoreTypeException
from .prometheus import PrometheusMetricStore
from .cadvisor import CadvisorMetricStore

class MetricStoreFactory(object):
    def get_metric_store(self, metric_store_config):
        metric_store_type = metric_store_config['type']
        if metric_store_type == 'prometheus':
            return PrometheusMetricStore(metric_store_config[metric_store_type])
        elif metric_store_type == 'cadvisor':
            return CadvisorMetricStore(metric_store_config[metric_store_type])
        else:
            raise UknownMetricStoreTypeException(metric_store_type)
