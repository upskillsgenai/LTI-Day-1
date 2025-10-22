# 🚀 Developing Multimodal AI Applications for Image Classification using Azure OpenAI GPT-4o

Launch the **Generative AI Chat App** lab from the LAB portal:  
[https://cloudthat.learnondemand.net/](https://cloudthat.learnondemand.net/)

---

## 🎯 Complete Exercise: Deploy a Model in Azure AI Foundry

Deploy a model in an **Azure AI Foundry project** to obtain the following:
- Model Key  
- Endpoint  
- Deployment Name  

### 🔍 How to Find Model Key, Endpoint, and Deployment Name
1. In the **Azure AI Foundry** portal, open the **Overview** page of your project.  
2. In the **Endpoints and Keys** section, make sure the **Azure AI Foundry** library is selected.  
3. View the **Project Endpoint** — you’ll use it to connect your model in a client application.  
4. To find the **Deployment Name**, go to **Model + Endpoint** in the left navigation pane.

---

## 🧭 Explore Azure AI Foundry UI

Familiarize yourself with the Azure AI Foundry interface.

---

## 💻 Set Up the Development Environment

1. Open **VS Code**.  
2. Create a folder named `Day-1`.  
3. Open **Terminal** (`View -> Terminal`) and create a virtual environment using the steps below.

```
# Create virtual environment
python -m venv .venv

# Activate it
# Windows PowerShell
.venv\Scripts\Activate

# macOS / Linux
source .venv/bin/activate
```

4. Install dependencies:

```
pip install openai
```

---

## 📂 Download and Run the Code

1. Download project files from GitHub and place them in your `Day-1` folder.  
2. Replace your **key**, **endpoint**, and **deployment name** in the configuration.  
3. Run the image classification script:

```
python image_classification.py images/car1.jpg
```

4. Change the image name in the above command to classify different images.
```

Would you like me to format this as a **step-by-step instruction list with checkboxes** (✅ markdown tasks) for interactive GitHub documentation?
