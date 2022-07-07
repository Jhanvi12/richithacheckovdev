resource "aws_s3_bucket" "s3_no_condition"{
    name="s3_bucket_name"
    policy={
        "Statement":[
            {
                "Action":"act",
                "Effect":"Allow",
                "Resource":"res",
                "Principal":"*",
                "Condition": {
                "aws:PrincipalAccount": "docs/"
                }
            }
        ]
    }
}
