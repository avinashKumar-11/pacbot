from core.terraform.resources.aws import iam
from resources.iam.ecs_role import ECSRole


class LambdaPolicyDocument(iam.IAMPolicyDocumentData):
    statement = [
        {
            'actions': ["sts:AssumeRole"],
            'principals': [
                {
                    'type': "Service",
                    'identifiers': ["lambda.amazonaws.com"]
                }
            ],
            'effect': "Allow"
        }
    ]


class AllReadRole(iam.IAMRoleResource):
    name = ""  # Empty string will take prefix as the name
    assume_role_policy = LambdaPolicyDocument.get_output_attr('json')
    force_detach_policies = True


class AllReadOnlyAccessPolicyAttach(iam.IAMRolePolicyAttachmentResource):
    role = AllReadRole.get_output_attr('name')
    policy_arn = "arn:aws:iam::aws:policy/ReadOnlyAccess"


class AllReadLambdaFullAccessPolicyAttach(iam.IAMRolePolicyAttachmentResource):
    role = AllReadRole.get_output_attr('name')
    policy_arn = "arn:aws:iam::aws:policy/AWSLambdaFullAccess"


class AllReadIAMFullAccessPolicyAttach(iam.IAMRolePolicyAttachmentResource):
    role = AllReadRole.get_output_attr('name')
    policy_arn = "arn:aws:iam::aws:policy/IAMFullAccess"


class AllReadConfigRolePolicyAttach(iam.IAMRolePolicyAttachmentResource):
    role = AllReadRole.get_output_attr('name')
    policy_arn = "arn:aws:iam::aws:policy/service-role/AWSConfigRole"


class AllReadSupportAccessPolicyAttach(iam.IAMRolePolicyAttachmentResource):
    role = AllReadRole.get_output_attr('name')
    policy_arn = "arn:aws:iam::aws:policy/AWSSupportAccess"


class AllReadSupportAccessPolicyAttach(iam.IAMRolePolicyAttachmentResource):
    role = AllReadRole.get_output_attr('name')
    policy_arn = "arn:aws:iam::aws:policy/AWSSupportAccess"


class AllReadRoleAutoFixPolicyDocument(iam.IAMPolicyDocumentData):
    statement = [
        {
            'actions': [
                "s3:GetBucketTagging",
                "s3:ListBucketByTags",
                "s3:PutBucketTagging",
                "s3:ListBucket",
                "s3:GetObjectAcl",
                "s3:PutBucketAcl",
                "s3:PutBucketPolicy",
                "s3:GetBucketAcl",
                "s3:GetBucketPolicy",
                "s3:DeleteBucketPolicy",
                "iam:UpdateAccountPasswordPolicy",
                "ec2:CreateTags",
                "ec2:DescribeTags",
                "ec2:StopInstances",
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:UpdateSecurityGroupRuleDescriptionsEgress",
                "ec2:CreateSecurityGroup",
                "ec2:ModifyInstanceAttribute",
                "ec2:UpdateSecurityGroupRuleDescriptionsIngress",
                "redshift:CreateTags",
                "redshift:CreateClusterSecurityGroup",
                "redshift:ModifyCluster",
                "redshift:AuthorizeClusterSecurityGroupIngress",
                "rds:AddTagsToResource",
                "rds:CreateDBSecurityGroup",
                "rds:ModifyDBInstance",
                "es:AddTags",
                "es:ListTags",
                "es:UpdateElasticsearchDomainConfig",
                "elasticfilesystem:CreateTags",
                "elasticfilesystem:DescribeTags",
                "dynamodb:TagResource",
                "dax:ListTags",
                "dax:TagResource",
                "elasticache:AddTagsToResource",
                "elasticache:ListTagsForResource",
                "elasticloadbalancing:ApplySecurityGroupsToLoadBalancer",
                "elasticloadbalancing:ModifyLoadBalancerAttributes",
                "elasticloadbalancing:SetSecurityGroups",
                "ec2:CreateFlowLogs"
            ],
            'resources': ["*"],
            'effect': "Allow"
        },
        {
            'actions': [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams"
            ],
            'resources': ["*"],
            'effect': "Allow"
        },
    ]


class AllReadRoleAutoFixPolicy(iam.IAMRolePolicyResource):
    name = "pacbot-autofix"
    path = '/'
    policy = AllReadRoleAutoFixPolicyDocument.get_output_attr('json')


class AllReadRoleAutoFixPolicyAttach(iam.IAMRolePolicyAttachmentResource):
    role = AllReadRole.get_output_attr('name')
    policy_arn = AllReadRoleAutoFixPolicy.get_output_attr('arn')


class AllReadRolePolicyDocument(iam.IAMPolicyDocumentData):
    statement = [
        {
            'actions': ["sts:AssumeRole"],
            'resources': [AllReadRole.get_output_attr('arn')]
        }
    ]


class AllReadRolePolicy(iam.IAMRolePolicyResource):
    name = ""
    path = '/'
    policy = AllReadRolePolicyDocument.get_output_attr('json')


class AllReadRoleLambdaPolicyAttach(iam.IAMRolePolicyAttachmentResource):
    role = ECSRole.get_output_attr('name')
    policy_arn = AllReadRolePolicy.get_output_attr('arn')
