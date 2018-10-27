import boto3
import click

session = boto3.Session(profile_name='snappy')
ec2 = session.resource('ec2')

def filter_instances(project):
    instances = []

    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances

@click.group()
def instances():
    """Commands for instances"""

@instances.command('list')
@click.option('--project', default=None,
    help='Only instances for project (tag Project:<name>)')
def list_instances(project):
    "List EC2 instances"
    instances = []

    instances = filter_instances(project)

    for instance in instances:
        tags = { t['Key']:t['Value'] for t in instance.tags or [] }
        print(', '.join((
        instance.id,
        instance.instance_type,
        instance.placement['AvailabilityZone'],
        instance.state['Name'],
        instance.public_dns_name,
        tags.get('Project', '<no project>')
        )))

    return

@instances.command('stop')
@click.option('--project', default=None,
    help='Only instances for project')
def stop_instances(project):
    "Stop EC2 instances"

    instances = filter_instances(project)

    for instance in instances:
        print("Stopping {0}...".format(instance.id))
        instance.stop()

    return

@instances.command('start')
@click.option('--project', default=None,
    help='Only instances for project')
def start_instances(project):
    "Start EC2 instances"

    instances = filter_instances(project)

    for instance in instances:
        print("Starting {0}...".format(instance.id))
        instance.start()

    return

if __name__ == '__main__':
    instances()
