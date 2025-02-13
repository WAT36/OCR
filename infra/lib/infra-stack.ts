import * as cdk from "aws-cdk-lib";
import * as s3 from "aws-cdk-lib/aws-s3";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as lambda_nodejs from "aws-cdk-lib/aws-lambda-nodejs";
import * as iam from "aws-cdk-lib/aws-iam";
import * as events from "aws-cdk-lib/aws-events";
import * as targets from "aws-cdk-lib/aws-events-targets";
import { Construct } from "constructs";
import * as path from "path";

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3
    const ocrFileBucket = new s3.Bucket(this, "OCRFileUploadsBuckets", {
      bucketName: "ocr-file-uploads-buckets",
      eventBridgeEnabled: true,
    });

    // Lambda 関数の作成
    const lambdaFunction = new lambda_nodejs.NodejsFunction(
      this,
      "ImageTextExtractLambda",
      {
        entry: path.join(__dirname, "../lambda/index.ts"),
        handler: "handler",
        runtime: lambda.Runtime.NODEJS_18_X,
        timeout: cdk.Duration.seconds(120),
      }
    );

    // Lambda に S3 へのアクセス権を付与
    ocrFileBucket.grantRead(lambdaFunction);
    ocrFileBucket.grantWrite(lambdaFunction);

    // Lambda に Textract へのアクセス権を付与
    lambdaFunction.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["textract:DetectDocumentText"],
        resources: ["*"],
      })
    );

    // EventBridge
    const ocrFileUploadedEvent = new events.Rule(this, "OCRrFileUploaded", {
      ruleName: "OCRFileUploaded",
      eventPattern: {
        source: ["aws.s3"],
        detailType: ["Object Created"],
        detail: {
          bucket: {
            name: [ocrFileBucket.bucketName],
          },
          object: {
            key: [
              {
                prefix: "input/",
              },
            ],
          },
        },
      },
    });
    ocrFileUploadedEvent.addTarget(
      new targets.LambdaFunction(lambdaFunction, {})
    );
  }
}
