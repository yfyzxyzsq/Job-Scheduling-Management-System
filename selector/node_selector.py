from k8s.k8s_adapter import KubernetesAPIAdapter
from utils.class_container import Registry

class NodeSelector:
    def __init__(self, registry:Registry):
        self.log_flag = f'[NodeSelector]'
        self.logger = registry.get_class('logger')
        self.logger.info(f'{self.log_flag} init NodeSelector')
        self.k8s_adapter = registry.get_class('k8s_adapter')

    def select_node(self):
        # 使用自研算法选择最优节点
        # 可以考虑节点的资源使用率、响应时间、网络拥塞等因素
        pass