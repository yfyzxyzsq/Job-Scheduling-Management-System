from kubernetes import client, config
from utils.class_container import Registry

class KubernetesAPIAdapter:
    def __init__(self, registry:Registry):
        self.log_flag = f'[KubernetesAPIAdapter]'
        self.logger = registry.get_class('logger')
        self.logger.info(f'{self.log_flag} init KubernetesAPIAdapter')
        
        config.load_kube_config()
        self.core_api = client.CoreV1Api()

    def deploy_to_node(self, image, node, job_type):
        # 在指定节点部署服务
        pass

    def get_node_resources(self, node_name):
        # 获取节点资源信息
        pass

    def get_cluster_resources(self):
        # 获取集群资源信息
        pass