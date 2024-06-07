# Create Stack with existing resource's configuration
aws cloudformation create-change-set    
    --stack-name TargetStack 
    --change-set-name ImportChangeSet    
    --change-set-type IMPORT    
    --resources-to-import file://resources_to_import.txt    
    --template-body file://template.yaml

# To Check if it the change set creation succeeded or failed.
aws cloudformation describe-change-set 
    --change-set-name ImportChangeSet 
    --stack-name TargetStack

# To execute the change set
aws cloudformation execute-change-set 
    --change-set-name ImportChangeSet 
    --stack-name TargetStack

# To update the stack with new configurations, you can add anything with all cloudformation options.
aws cloudformation update-stack     
    --stack-name TargetStack     
    --template-body file://new-template.yaml    
    --capabilities CAPABILITY_NAMED_IAM