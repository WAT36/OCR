import * as cdk from "aws-cdk-lib";
import * as s3 from "aws-cdk-lib/aws-s3";
import * as s3n from "aws-cdk-lib/aws-s3-notifications";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as lambda_nodejs from "aws-cdk-lib/aws-lambda-nodejs";
import * as lambdaLayer from "aws-cdk-lib/aws-lambda";
import * as ecr from "aws-cdk-lib/aws-ecr";
import { Construct } from "constructs";
import * as path from "path";
import { Duration } from "aws-cdk-lib";

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3
    const ocrFileBucket = new s3.Bucket(this, "OCRBuckets", {
      bucketName: "ocr-buckets",
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    // // ECR repository
    // const repository = new ecr.Repository(this, "OCRRepository", {
    //   repositoryName: "ocr-repo",
    // });

    // // Lambda
    // const ocrLambda = new lambda.Function(this, "OCRImageFunctions", {
    //   code: new lambda.EcrImageCode(repository, {}),
    //   handler: lambda.Handler.FROM_IMAGE,
    //   runtime: lambda.Runtime.FROM_IMAGE,
    //   timeout: Duration.minutes(15),
    //   memorySize: 1024,
    //   functionName: "OCRImageFunctions",
    //   // TODO parameter storeから取りたい
    //   environment: {},
    // });

    // // Lambda に S3 へのアクセス権を付与
    // ocrFileBucket.grantRead(ocrLambda);
    // ocrFileBucket.grantWrite(ocrLambda);

    // // S3 イベント通知を設定（画像がアップロードされたら Lambda をトリガー）
    // // ✅ S3 の特定フォルダ（prefix）に対してのみ Lambda を実行
    // const prefix = "input/"; // 🔹 S3 のフォルダ名（例: input-folder/）
    // ocrFileBucket.addEventNotification(
    //   s3.EventType.OBJECT_CREATED,
    //   new s3n.LambdaDestination(ocrLambda),
    //   { prefix } // 🔹 ここでプレフィックスを指定
    // );
  }
}
