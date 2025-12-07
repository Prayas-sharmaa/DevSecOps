

resource "aws_elastic_beanstalk_application" "store_app" {
  name        = "store-management-app"
  description = "Store management web app"
}



resource "aws_elastic_beanstalk_environment" "store_env" {
  name                = "store-management-env"
  cname_prefix        = "storewebapp" 
  application         = aws_elastic_beanstalk_application.store_app.name
  solution_stack_name = "64bit Amazon Linux 2023 v4.8.0 running Python 3.14"
    setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "IamInstanceProfile"
    value     = "LabInstanceProfile"
  }
  

  # Service role
  setting {
    namespace = "aws:elasticbeanstalk:environment"
    name      = "ServiceRole"
    value     = "LabRole"
  }

  # EC2 key pair
  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "EC2KeyName"
    value     = "vockey"
  }
}