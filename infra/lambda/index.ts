import { S3Event, S3Handler } from "aws-lambda";
import AWS from "aws-sdk";

const s3 = new AWS.S3();
const textract = new AWS.Textract();

export const handler: S3Handler = async (event: S3Event) => {
  console.log("Received event:", JSON.stringify(event, null, 2));

  // event.Records が存在するかチェック
  if (!event.Records || event.Records.length === 0) {
    console.error("No records found in the event.");
    return;
  }

  for (const record of event.Records) {
    const bucketName = record.s3.bucket.name;
    const fileKey = decodeURIComponent(
      record.s3.object.key.replace(/\+/g, " ")
    );

    console.log(`Processing file: ${fileKey} from bucket: ${bucketName}`);

    try {
      // AWS Textract で OCR を実行
      const textractResponse = await textract
        .detectDocumentText({
          Document: {
            S3Object: {
              Bucket: bucketName,
              Name: fileKey,
            },
          },
        })
        .promise();

      let extractedText = "";
      if (textractResponse.Blocks) {
        for (const block of textractResponse.Blocks) {
          if (block.BlockType === "LINE" && block.Text) {
            extractedText += block.Text + "\n";
          }
        }
      }

      // S3 にテキストファイルとして保存
      const outputFileKey = fileKey
        .replace(/input\//i, "output/")
        .replace(/\.(jpg|jpeg|png)$/i, ".txt");
      await s3
        .putObject({
          Bucket: bucketName,
          Key: outputFileKey,
          Body: extractedText,
          ContentType: "text/plain",
        })
        .promise();

      console.log(
        `Processed and saved text to: s3://${bucketName}/output/${outputFileKey}`
      );
    } catch (error) {
      console.error(`Error processing ${fileKey}:`, error);
      throw error;
    }
  }
};
