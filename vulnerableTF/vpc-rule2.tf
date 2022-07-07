


resource "aws_vpc_endpoint_policy" "bad-example" {
  vpc_endpoint_id = aws_vpc_endpoint.example.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "AllowAll",
        "Effect" : "Allow",
        "Principal" : {
          "AWS" : "*"
        },
        "Action" : [
          "s3:*"
        ],
        "Resource" : [
            "*"
        ]
      }
    ]
  })
}

resource "aws_vpc_endpoint_policy" "good-example" {
  vpc_endpoint_id =  aws_vpc_endpoint.example.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "AllowAll",
        "Effect" : "Allow",
        "Principal" : {
          "AWS" : "*"
        },
        "Action" : [
          "s3:*"
        ],
        "Resource" : [
            "*"
        ],
        "Condition":{
            "StringEquals":{
                "aws:SourceVPC" : "o-7800"
                
            }

        }
      }
    ]
  })
}

resource "aws_vpc_endpoint_policy" "bad-example1-" {
  vpc_endpoint_id =  aws_vpc_endpoint.example.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "AllowAll",
        "Effect" : "Allow",
        "Principal" : {
          "AWS" : "*"
        },
        "Action" : [
          "s3:*"
        ],
        "Resource" : [
            "*"
        ],
        "Condition":{
            "StringEquals":{
                "aws:SkypathOrgID" : "o-7800"
                
            }

        }
      }
    ]
  })
}


resource "aws_vpc_endpoint_policy" "bad-example2" {
  vpc_endpoint_id =  aws_vpc_endpoint.example.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "AllowAll",
        "Effect" : "Allow",
        "Principal" : {
          "AWS" : "*"
        },
        "Action" : [
          "s3:*"
        ],
        "Resource" : [
            "*"
        ],
        "Condition":{
            "StringEquals":{
                "aws:SourceVPC" : "*"
                
            }

        }
      }
    ]
  })
}

resource "aws_vpc_endpoint_policy" "bad-example3" {
  vpc_endpoint_id =  aws_vpc_endpoint.example.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "AllowAll",
        "Effect" : "Allow",
        "Principal" : {
          "AWS" : "*"
        },
        "Action" : [
          "s3:*"
        ],
        "Resource" : [
            "*"
        ],
        "Condition":{
            "StringEquals":"*"

        }
      }
    ]
  })
}

resource "aws_vpc_endpoint_policy" "bad-example4" {
  vpc_endpoint_id =  aws_vpc_endpoint.example.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "AllowAll",
        "Effect" : "Allow",
        "Principal" : {
          "AWS" : "*"
        },
        "Action" : [
          "s3:*"
        ],
        "Resource" : [
            "*"
        ],
        "Condition":"*"
      }
    ]
  })
}