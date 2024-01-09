from k8s.k8s_adapter import KubernetesAPIAdapter
from selector.node_selector import NodeSelector

class ResourceManager:
    def __init__(self):
        self.k8s_api_adapter = KubernetesAPIAdapter()
        self.node_selector = NodeSelector()

    def get_cluster_resources(self):
        # Get cluster resources status
        return self.k8s_api_adapter.get_cluster_resources()

    def get_node_resources(self, node_name):
        # Get resources status of a single node
        return self.k8s_api_adapter.get_node_resources(node_name)

    # Other resource management methods