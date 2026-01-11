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

## 💻 Set Up the Development Environment

1. Open **VS Code**.
2. Git Clone unsing Ctrl + Shift + P , then clone this GitHub Repo url ()
3. Create a folder named `Day-1`to store GitHub clone  
4. Open **Terminal** (`View -> Terminal`) .
5. Install dependencies:

```
pip install openai
```
 
6. Run the image classification script:

```
python image_classification.py images/unkonwn_1.jpg
```

7. Change the image name in the above command to classify different images.
```

