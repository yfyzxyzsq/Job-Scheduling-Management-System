# coding=utf-8
import sys
import argparse
from monitoring.logger import Logger
from cli.cli import CLI
from job.job_scheduler import JobScheduler
from resource_manager.resource_manager import ResourceManager
from utils.class_container import Registry
from k8s.k8s_adapter import KubernetesAPIAdapter
from selector.node_selector import NodeSelector
from command.command_parser import CommandParser
# gloable varible

main_log_flag = f'[main]'

def init():
    print("init system variable")
    logger_wrapper = Logger()
    logger = logger_wrapper.logger
    registry = Registry(logger)
    
    registry.add_class('logger', logger)
    # 1 
    k8s_adapter = KubernetesAPIAdapter(registry)
    registry.add_class('k8s_adapter', k8s_adapter)
    # 2
    node_selector = NodeSelector(registry)
    registry.add_class('node_selector', node_selector)
    # 3
    job_scheduler = JobScheduler(registry)
    registry.add_class('job_scheduler', job_scheduler)
    # 4
    resource_manager = ResourceManager(registry)
    registry.add_class('resource_manager', resource_manager)
    
    # 5
    command_parser = CommandParser(registry)
    registry.add_class('command_parser', command_parser)
    
    logger.info(f'{main_log_flag} init system success')
    return registry


# 配置命令行参数
def parse_arguments():
    parser = argparse.ArgumentParser(description="Kubernetes Job Management System")
    parser.add_argument('--run', help='Start the job scheduler', action='store_true')
    # 可以根据需要添加更多的命令行参数
    return parser.parse_args()

# 主函数
def main():
    # 解析命令行参数
    # args = parse_arguments()
    
    registry = init()

    # 实例化CLI
    cli = CLI(registry)
    # 启动CLI界面
    cli.start()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)