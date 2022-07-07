from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.common.util.type_forcers import force_list, extract_policy_dict
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from typing import List
import pprint


class VPCCustomRule2(BaseResourceCheck):
     def __init__(self):
        name = "Ensure S3,KMS,SECRETS MANAGER SECRETS policies leverage Resource via VPC"
        id = "CKV_AWS_JHANVI_4"
        supported_resources = ['aws_kms_policy', 'aws_s3_bucket', 'aws_vpc_endpoint_policy', 'aws_vpc','aws_secretsmanager_secret']
        
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

     def scan_resource_conf(self,conf):


        try:
            policy_block = None
            if 'policy' in conf.keys():
                policy_block = extract_policy_dict(conf['policy'][0])
                
            elif 'inline_policy' in conf.keys():
                policy_block = extract_policy_dict(conf['inline_policy'][0])
            if policy_block and 'Statement' in policy_block.keys():
                 for statement in force_list(policy_block['Statement']):    
                   
                    if not statement.get('Condition')  or statement.get('Condition') == "*" in force_list(statement['Condition']):
                         
                         return CheckResult.FAILED
                    elif statement and 'Condition' in statement.keys():
                        if 'StringEquals' in statement['Condition'].keys():
                           
                            Check_dict = statement['Condition']['StringEquals']
                            pprint.pprint(Check_dict.values())
                            val = statement['Condition']['StringEquals'].keys()
                            pprint.pprint('type of val is')
                            pprint.pprint(statement['Condition']['StringEquals'].values())
                            APPROVED_IDs = ["o-1406","o-3010","o-8900","o-7800"]

                            if ("aws:SourceVPC" in val) or ("aws:SourceVPCe" in val):
                                pprint.pprint('inside first if loop')
                            
                                for k,v in Check_dict.items():
                                    pprint.pprint(v)
                                    for i in APPROVED_IDs:
                                        pprint.pprint(i)
                                        if i==v:
                                            pprint.pprint('in it')
                                            return CheckResult.PASSED
                                        else:
                                            CheckResult.FAILED

                            
                                
        except Exception:  # nosec
            pass    
        return CheckResult.FAILED
    
    

     def get_evaluated_keys(self) -> List[str]:
        return ['policy', 'inline_policy']


check = VPCCustomRule2()
        