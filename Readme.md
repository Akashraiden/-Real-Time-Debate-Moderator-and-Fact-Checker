# 🎤 Real-Time Debate Moderator & Fact-Checker Using LLM Model with Aws Deployment

This Streamlit application enables users to **transcribe**, **moderate**, **fact-check**, **analyze sentiment**, **summarize**, and **translate** audio content from live or recorded debates. It leverages **OpenAI's Whisper** for audio transcription and **Gemini 1.5 Pro** (Google Generative AI) for intelligent text-based tasks.

Whether you're analyzing a political debate, educational discussion, or any conversation involving critical dialogue, this tool helps streamline insight extraction in real time.

---

## 🚀 Features

- 🎙️ **Real-Time Transcription** – Convert audio debates into accurate text using OpenAI Whisper.
- 📌 **Debate Moderation** – Detect off-topic or disrespectful content and highlight moderation suggestions.
- ✅ **Fact-Checking** – Validate factual claims using Gemini AI's reasoning capabilities.
- 😃 **Sentiment Analysis** – Identify tone (positive, negative, or neutral) in multiple languages.
- 📝 **Summarization** – Get a concise summary of long conversations or discussions.
- 🌍 **Multilingual Translation** – Translate debate transcripts into supported languages.

- ## 🧩 Workflow

1. **Upload an audio file** (`.mp3`, `.wav`, `.ogg`)
2. **Transcribe** the audio using **Whisper**
3. **Perform AI tasks** with **Gemini 1.5 Pro**  
   - Debate Moderation  
   - Fact-Checking  
   - Sentiment Analysis (multiple languages)  
   - Text Summarization  
   - Translation
4. **View** all AI-generated outputs directly in the Streamlit UI

---
## 📌 Step-by-Step Implementation

### 1. Development Environment Setup
- Used **Visual Studio Code (VS Code)** as the primary IDE.
- Developed the application and created a `Dockerfile`.
- Built and tested the Docker image locally.

### 2. Version Control & GitHub
- Initialized a Git repository.
- Committed and pushed all project files to **GitHub** using Git.

### 3. AWS IAM Configuration
- Logged into the **AWS Console** and created a new **IAM User**.
- Assigned the following permissions:
  - `AmazonEC2FullAccess`
  - `AmazonECRFullAccess`
- Generated **AWS Access Key ID** and **Secret Access Key** for use in GitHub Secrets.

### 4. Elastic Container Registry (ECR) Setup
- Created a new **ECR Repository** to store Docker images.
- Logged into the ECR via command line using the AWS CLI.

### 5. EC2 Instance Setup
- Launched a new **EC2 instance** (Amazon Linux or Ubuntu).
- Connected to the instance via SSH.
- Installed and configured **Docker** using the following commands:

```bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo usermod -aG docker ec2-user


### 6. 🏃‍♂️ Self-Hosted GitHub Runner on EC2

- Downloaded and installed the **GitHub self-hosted runner** on the EC2 instance.
- Followed these steps to set it up:
  1. Navigated to your repository on GitHub.
  2. Go to **Settings → Actions → Runners → New self-hosted runner**.
  3. Selected the OS (Linux), and followed the setup commands provided:
     ```bash
     mkdir actions-runner && cd actions-runner
     curl -o actions-runner-linux-x64-2.309.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.309.0/actions-runner-linux-x64-2.309.0.tar.gz
     tar xzf ./actions-runner-linux-x64-2.309.0.tar.gz
     ./config.sh --url https://github.com/<your-username>/<your-repo> --token <generated-token>
     ./run.sh
     ```
  4. You can install it as a service (optional):
     ```bash
     sudo ./svc.sh install
     sudo ./svc.sh start
     ```

- The runner is now connected and listens for GitHub Actions workflows for that repository.

---

### 7. 🔐 GitHub Repository Secrets Configuration

Added the following secrets to the GitHub repository for secure CI/CD integration.  
Navigate to: **Repository → Settings → Secrets and variables → Actions → New repository secret**

| Secret Name              | Description                                              |
|--------------------------|----------------------------------------------------------|
| `AWS_ACCESS_KEY_ID`      | Access key ID from the IAM user                          |
| `AWS_SECRET_ACCESS_KEY`  | Secret access key from the IAM user                      |
| `AWS_ECR_LOGIN_URI`      | URI for ECR login, e.g., `123456789012.dkr.ecr.us-east-1.amazonaws.com` |
| `AWS_REGION`             | AWS region where ECR/EC2 is hosted (e.g., `us-east-1`)   |
| `ECR_REPOSITORY_NAME`    | Name of your ECR repository (e.g., `my-docker-app`)      |

These secrets are used in the GitHub Actions workflow to securely authenticate with AWS and manage Docker deployments.




## 🌍 Supported Languages

### Sentiment & Translation

- English  
- Spanish  
- French  
- German  
- Chinese  
- Japanese


---

## 🛠️ Tech Stack

| Component         | Library / Service             |
|------------------|-------------------------------|
| Frontend UI      | [Streamlit](https://streamlit.io) |
| Transcription    | [Whisper](https://github.com/openai/whisper) |
| AI Text Tasks    | [Gemini 1.5 Pro](https://ai.google.dev/) |
| Env Management   | `python-dotenv`               |
| Containerization | Docker                         |
| Cloud Hosting    | AWS EC2                        |

---

## 📦 Local Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/real-time-debate-moderator.git
cd real-time-debate-moderator



## 📬 Contact

If you have any questions or suggestions, feel free to reach out:

- **Name**: Akash
- **Email**: akasht2098@gmail.com 


