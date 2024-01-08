class ResourceManager:
    def __init__(self):
        self.k8s_connector = KubernetesAPIConnector()
        self.node_selector = NodeSelector()

    def get_cluster_resources(self):
        # Get cluster resources status
        return self.k8s_connector.get_cluster_resources()

    def get_node_resources(self, node_name):
        # Get resources status of a single node
        return self.k8s_connector.get_node_resources(node_name)

    # Other resource management methods