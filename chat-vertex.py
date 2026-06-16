#!/bin/env python3
# File: chat-vertex.py
# Author: Steven Lee
# Date: 03/18/2026
# Description: Instead of a GOOGLE_API_KEY, this accesses Vertex AI
#   using a Google Application Default Credentials (ADC) file.

# Prerequisites:
# 1. Environment variables
# ANTHROPIC_VERTEX_PROJECT_ID - project ID; must be set
# CLOUD_ML_REGION - location; defaults to "global"
#
# 2. Installation
# pip install langchain-google-vertexai

import os
from langchain_google_vertexai.model_garden import ChatAnthropicVertex

# Anthropic provides a specific wrapper for Vertex
project = os.environ.get("ANTHROPIC_VERTEX_PROJECT_ID")
location = os.environ.get("CLOUD_ML_REGION", "global")

llm = ChatAnthropicVertex(
    model_name="claude-sonnet-4-6",
    project=project,
    location=location
)

response = llm.invoke(input("Ask a question: "))
print(response.content)
