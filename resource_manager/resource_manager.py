from k8s.k8s_adapter import KubernetesAPIAdapter
from selector.node_selector import NodeSelector
from utils.class_container import Registry

class ResourceManager:
    def __init__(self, registry:Registry):
        self.log_flag = f'[ResourceManager]'
        self.logger = registry.get_class('logger')
        self.logger.info(f'{self.log_flag} init ResourceManager')
        self.k8s_adapter = registry.get_class('k8s_adapter')
        self.node_selector = registry.get_class('node_selector')

    def get_cluster_resources(self):
        # Get cluster resources status
        return self.k8s_api_adapter.get_cluster_resources()

    def get_node_resources(self, node_name):
        # Get resources status of a single node
        return self.k8s_api_adapter.get_node_resources(node_name)

    # Other resource management methods