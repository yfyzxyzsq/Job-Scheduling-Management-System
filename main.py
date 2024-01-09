# coding=utf-8
import sys
import argparse
from monitoring.logger import Logger
from cli.cli import CLI
from job.job_scheduler import JobScheduler
from resource_manager.resource_manager import ResourceManager

# gloable varible
job_scheduler = None
resource_manager = None

def init():
    print("init system variable")
    job_scheduler = JobScheduler()
    resource_manager = ResourceManager()
    


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
    
    # 初始化日志
    # Logger.setup_logging()

    # 实例化CLI
    cli = CLI()
    # 启动CLI界面
    cli.start()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)