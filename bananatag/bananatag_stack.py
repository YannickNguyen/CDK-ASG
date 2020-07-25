from aws_cdk import (
    aws_s3 as s3,
    aws_ec2 as ec2,
    aws_autoscaling as asg,
    aws_elasticloadbalancingv2 as alb,
    core
)

class BananatagStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        #Creating vpc
        vpc = ec2.Vpc(self,"test_vpc_id")

        #Creating a basic web application to view
        data = open("./httpd.sh", "rb").read()
        httpd=ec2.UserData.for_linux()
        httpd.add_commands(str(data,'utf-8'))


        # Auto-scaling group and instance creation
        asginstances = asg.AutoScalingGroup(self, "ASG",
                                            vpc=vpc,
                                            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
                                            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
                                            desired_capacity=2,
                                            max_capacity=2,
                                            min_capacity=0,
                                            user_data=httpd)

        #Creating ALB and allowing internet access
        lb = alb.ApplicationLoadBalancer(self, 'LB', vpc=vpc, internet_facing=True)

        #ALB listening on port 80
        listener = lb.add_listener("Listener", port=80)
        #Add the ASG as targets for the ALB
        listener.add_targets("Target", port=80, targets=[asginstances])
        listener.connections.allow_default_port_from_any_ipv4("Forwarding port 80 to the ASG")

        #Print out the ALB url to show web instance application
        core.CfnOutput(self,"LoadBalancer",export_name="Bananatag",value=lb.load_balancer_dns_name)
