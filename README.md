# 🚀 Launch LAB: Create a Generative AI Chat App

Launch the **Generative AI Chat App** lab from the LAB portal:  
[https://cloudthat.learnondemand.net/](https://cloudthat.learnondemand.net/)

---

## ✅ Step-by-Step Task List

### 🧩 **1. Launch and Prepare the Lab**
- [ ] Launch the LAB from the [CloudThat portal](https://cloudthat.learnondemand.net/)
- [ ] Access your lab environment for Generative AI Chat App development

---

### 🧠 **2. Deploy Model in Azure AI Foundry**
- [ ] Open your Azure AI Foundry project
- [ ] Navigate to the **Overview** page
- [ ] Locate **Endpoints and Keys** section
- [ ] Ensure the **Azure AI Foundry** library is selected
- [ ] View and copy the **Project Endpoint**
- [ ] Go to **Model + Endpoint** in left pane to find **Deployment Name**

---

### ⚙️ **3. Explore the Azure AI Foundry UI**
- [ ] Explore Azure AI Foundry interface
- [ ] Understand where to manage models and keys

---

### 💻 **4. Set Up Local Development Environment**
- [ ] Open **VS Code**
- [ ] Create a folder named `Day-1`
- [ ] Open the terminal (`View -> Terminal`)
- [ ] Run the following commands to create & activate virtual environment:

```
# Create virtual environment
python -m venv .venv

# Activate it
# Windows PowerShell
.venv\Scripts\Activate

# macOS / Linux
source .venv/bin/activate
```

- [ ] Install dependencies:

```
pip install openai
```

---

### 📦 **5. Download, Configure, and Run the Code**
- [ ] Download required files from GitHub and place them in the `Day-1` folder
- [ ] Update your **key**, **endpoint**, and **deployment name** in the code
- [ ] Run the image classification script:

```
python image_classification.py images/car1.jpg
```

- [ ] Test classification with different image files by changing the image name in the command

---

🧩 **End of Lab** — You’ve successfully completed the setup and tested image classification using your Azure AI Foundry model.
```

