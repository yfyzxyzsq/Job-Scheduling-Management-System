from node_selector import NodeSelector
from k8s_adapter import KubernetesAPIAdapter

class JobScheduler:
    def __init__(self, k8s_adapter, node_selector):
        self.k8s_adapter = k8s_adapter
        self.node_selector = node_selector

    def deploy_job(self, image, job_type):
        # 部署在线或离线任务
        node = self.node_selector.select_node()
        self.k8s_adapter.deploy_to_node(image, node, job_type)

    def schedule_job(self, image, job_type):
        # 调度任务