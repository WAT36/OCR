import * as cdk from "aws-cdk-lib";
import * as s3 from "aws-cdk-lib/aws-s3";
import { Construct } from "constructs";
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3
    const ocrFileBucket = new s3.Bucket(this, "OCRFileUploadsBuckets", {
      bucketName: "ocr-file-uploads-buckets",
      //eventBridgeEnabled: true,
    });
  }
}
