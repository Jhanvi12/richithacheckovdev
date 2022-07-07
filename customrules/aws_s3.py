from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.common.util.type_forcers import force_list, extract_policy_dict
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from typing import List
import pprint

class S3BucketUnrestrictedPolicy(BaseResourceCheck):

    def __init__(self):
        name = "S3 Bucket Policies with Unrestricted Access"
        id = "CKV_AWS_GS_5"
        supported_resources = ['aws_s3_bucket']
        
        categories = [CheckCategories.IAM]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        try:
            if 'policy' not in conf.keys():
                pprint.pprint('got policy block')
                return CheckResult.FAILED

            # pprint.pprint(conf.get('policy'))
            
            policies = force_list(conf.get('policy'))
            for policy in policies:
                if 'Statement' not in policy:
                    pprint.pprint('got policy block 1')
                    return CheckResult.FAILED

                statement = policy.get('Statement')
                for statement in force_list(statement):

                    principal = statement.get('Principal', '') 
                    condition = statement.get('Condition', '')
                    if not principal:
                        pprint.pprint('not principal')
                        return CheckResult.FAILED
                    conditions == ["aws:PrincipalAccount","aws:PrincipalArn","aws:PrincipalIsAWSService","aws:SourceArn","aws:VpcSourceIp","aws:username","aws:userid","aws:SourceVpc","aws:SourceVpce","aws:SourceIp","aws:SourceIdentity","aws:SourceAccount","aws:SourceOwner","kms:CallerAccount"]
                    cntn = force_list(conf.get('Condition'))
                    if principal == '*' and not condition:
                        pprint.pprint("line 48")
                        pprint.pprint('no condition')
                        return CheckResult.FAILED
                    if principal == "*" or ("condition" not in conditions):
                        pprint.pprint("not in condition")
                        return CheckResult.FAILED
                    
                    return CheckResult.PASSED

        except Exception:
            pass    
        return CheckResult.FAILED

    def get_evaluated_keys(self) -> List[str]:
        return ['policy', 'inline_policy']

check=S3BucketUnrestrictedPolicy()


                        
        
