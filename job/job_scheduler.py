from selector.node_selector import NodeSelector
from k8s.k8s_adapter import KubernetesAPIAdapter
from utils.class_container import Registry

class JobScheduler:
    def __init__(self, registry:Registry):
        self.log_flag = f'[JobScheduler]'
        self.logger = registry.get_class('logger')
        self.logger.info(f'{self.log_flag} init JobScheduler')
        self.k8s_adapter = registry.get_class('k8s_adapter')
        self.node_selector = registry.get_class('node_selector')

    def deploy_job(self, image, job_type):
        # 部署在线或离线任务
        node = self.node_selector.select_node()
        self.k8s_adapter.deploy_to_node(image, node, job_type)

    def schedule_job(self, image, job_type):
        # 调度任务
        pass