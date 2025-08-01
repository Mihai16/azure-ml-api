# Azure ML API
A minimal FastAPI-based machine learning service designed for deployment on Azure App Service.  
This project demonstrates a real-world workflow from data sourcing to model deployment and API exposure, with automation and cloud integration in mind.

---

## 📦 Project Structure
```text
azure-ml-api/
├── app/ # Application code (API, logic)
├── scripts/ # Utility scripts (data ingestion, etc.)
├── tests/ # Unit and integration tests
├── data/raw/ # Downloaded datasets (not tracked by Git)
├── reports/ # Profiling reports, outputs
├── .venv/ # Virtual environment (excluded)
├── Dockerfile # Containerization config (to be added)
└── README.md
```
---

## 📥 Dataset Setup
This project uses the **Seoul Bike Sharing Demand** dataset, originally provided via Kaggle:
- [Seoul Bike Sharing Demand Prediction – Kaggle](https://www.kaggle.com/datasets/saurabhshahane/seoul-bike-sharing-demand-prediction)

### 1. Configure Kaggle API Credentials
To enable CLI-based dataset downloads:
1. Go to [Kaggle Account Settings](https://www.kaggle.com/account)
2. Scroll to **API** and click **"Create New API Token"**
3. Move the downloaded `kaggle.json` file to your `.kaggle` directory:
```bash
mkdir ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```
### 2. Dataset Download
To download the dataset, use:
```bash
 kaggle datasets download -d saurabhshahane/seoul-bike-sharing-demand-prediction -p data/raw --unzip
```
## License
This dataset is made available under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.  
Please cite the original author if reusing this data.