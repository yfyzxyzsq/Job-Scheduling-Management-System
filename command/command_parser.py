from job.job_scheduler import JobScheduler
# from resource.resource_manager import ResourceManager
from resource_manager.resource_manager import ResourceManager

class CommandParser:
    def __init__(self, job_scheduler, resource_manager):
        self.job_scheduler = job_scheduler
        self.resource_manager = resource_manager

    def parse_execute(self, command_input):
        # 解析用户输入的命令
        # 确定执行哪个操作，例如 deploy, schedule, view resources 等
        # 调用相应的方法
        # 分割命令输入为命令和参数
        parts = command_input.strip().split()
        
        # 获取命令和后续的参数
        command, args = parts[0], parts[1:]
        
        if not parts:
            raise ValueError("No command entered.")
         # 匹配命令并执行对应的方法
        if command == 'deploy':
            self.deploy_job(args)
        elif command == 'schedule':
            self.schedule_job(args)
        elif command == 'view_resources':
            self.view_resources(args)
        elif command == 'view_jobs':
            self.view_jobs(args)
        elif command == 'delete':
            self.delete_job(args)
        else:
            print("Unknown command.")
            
    def deploy_job(self, args):
        if len(args) != 1:
            print("Usage: deploy <job_id>")
            return
        job_id = args[0]
        self.job_scheduler.deploy(job_id)
        print(f"Job {job_id} deployed.")
        
    def schedule_job(self, args):
        if len(args) != 2:
            print("Usage: schedule <job_id> <node_id>")
            return
        job_id, node_id = args
        self.job_scheduler.schedule(job_id, node_id)
        print(f"Job {job_id} scheduled to node {node_id}.")
    
    def view_resources(self, args):
        if len(args) != 1:
            print("Usage: view_resources <node_id>")
            return
        node_id = args[0]
        resources = self.resource_manager.get_resources(node_id)
        print(f"Resources for node {node_id}: {resources}")

    def view_jobs(self, args):
        if args:
            print("Usage: view_jobs")
            return
        jobs = self.job_scheduler.get_all_jobs()
        for job in jobs:
            print(f"Job ID: {job.id}, Status: {job.status}")

    def delete_job(self, args):
        if len(args) != 1:
            print("Usage: delete <job_id>")
            return
        job_id = args[0]
        self.job_scheduler.delete(job_id)
        print(f"Job {job_id} deleted.")