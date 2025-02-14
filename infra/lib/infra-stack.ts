import * as cdk from "aws-cdk-lib";
import * as s3 from "aws-cdk-lib/aws-s3";
import * as s3n from "aws-cdk-lib/aws-s3-notifications";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as lambda_nodejs from "aws-cdk-lib/aws-lambda-nodejs";
import * as iam from "aws-cdk-lib/aws-iam";
import { Construct } from "constructs";
import * as path from "path";

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3
    const ocrFileBucket = new s3.Bucket(this, "OCRFileBuckets", {
      bucketName: "ocr-file-buckets",
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

    // S3 イベント通知を設定（画像がアップロードされたら Lambda をトリガー）
    ocrFileBucket.addEventNotification(
      s3.EventType.OBJECT_CREATED,
      new s3n.LambdaDestination(lambdaFunction)
    );

    // スタックの出力
    new cdk.CfnOutput(this, "OCRBucketName", {
      value: ocrFileBucket.bucketName,
    });
    new cdk.CfnOutput(this, "LambdaFunctionName", {
      value: lambdaFunction.functionName,
    });
  }
}
