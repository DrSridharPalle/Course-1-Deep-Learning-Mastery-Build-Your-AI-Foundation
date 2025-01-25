# Deep Learning Mastery: Build Your AI Foundation

![Pallence AI](PallenceAI-Final.png)

Welcome to the course! This README file provides clear instructions on how to download the course material and run the code for all sections. You can complete the course using two methods: Google Colab (recommended) or a local Anaconda environment. Follow the instructions below to get started.

## Course Material
All the course materials, including code and notebooks, can be found in the following GitHub repository:

[Course GitHub Repository](https://github.com/DrSridharPalle/Course-1-Deep-Learning-Mastery-Build-Your-AI-Foundation)

### How to Download the Material
1. Visit the repository: [Course GitHub Repository](https://github.com/DrSridharPalle/Course-1-Deep-Learning-Mastery-Build-Your-AI-Foundation)
2. Click on the green **Code** button.
3. Select **Download ZIP** to download the repository to your local machine.
4. Extract the downloaded ZIP file to access the notebooks and code files.

## Two Ways to Complete the Course

### 1. Using Google Colab (Recommended)
Google Colab allows you to run the course notebooks directly in your browser without installing anything locally. This is the recommended approach for the best experience.

#### Steps to Run on Google Colab:
1. **Upload the Course Folder to Google Drive**:
   - Extract the ZIP file you downloaded from GitHub.
   - Open google drive on your machine and copy the unzipped course folder here.
   - Ensure the folder structure remains intact.

2. **Open the Notebook from Google Drive**:
   - Navigate to your Google Drive using a web browser.
   - Locate the specific notebook you want to run.
   - Right-click on the notebook file and select **Open with > Google Colaboratory**. This will directly open the notebook in Google Colab.

3. **Follow the Setup Instructions in the Notebook**:
   - Each notebook contains commented-out code cells to set up the environment in Colab. Uncomment and run these cells as instructed:

     **Mount Google Drive**:
     ```python
     # from google.colab import drive
     # drive.mount('/content/drive')
     ```

     **Set the Working Directory**:
     ```python
     # import os
     # os.chdir('/content/drive/My Drive/Deep_Learning_Course/Section4')  # Adjust the path as needed
     # print("Current Directory:", os.getcwd())
     ```

     **Install Required Libraries**:
     ```python
     # !pip install tensorflow numpy pandas matplotlib
     ```

4. **Run the Notebook**:
   - After completing the setup steps, run the notebook cells sequentially. The folder structure and paths (e.g., `./images` or `./data`) will work seamlessly.

#### Notes:
- Ensure the Google Drive folder structure matches the original course materials.
- Restart the Colab runtime and re-run the setup cells if you encounter any errors.

### 2. Using a Local Environment (Anaconda)
If you prefer to run the course locally, follow these steps to set up an environment using Anaconda.

#### Steps to Set Up the Local Environment:
1. Download and install [Anaconda](https://www.anaconda.com/).
2. Open the Anaconda Prompt and create a new environment:

   ```bash
   conda create -n dl_course_env python=3.8 -y
   ```

3. Activate the environment:

   ```bash
   conda activate dl_course_env
   ```

4. Navigate to the directory where you downloaded the course material.
5. Install the required packages using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

#### Known Issues:
- Some parts of the code (e.g., GPU operations) may not work locally on Windows due to compatibility issues with the latest TensorFlow and GPU drivers.
- To avoid errors and compatibility issues, it is highly recommended to use Google Colab for GPU support and the latest libraries.

## Final Notes
- If you encounter any issues, feel free to reach out through the Q&A section of the Udemy course.
- Happy learning and coding!
