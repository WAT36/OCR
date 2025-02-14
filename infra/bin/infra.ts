#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { InfraStack } from "../lib/infra-stack";
import * as dotenv from "dotenv";

dotenv.config();
const app = new cdk.App();
new InfraStack(app, "OCRInfraStack", {
  env: { region: process.env.REGION || "" },
});
