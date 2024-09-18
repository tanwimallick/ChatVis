# ChatVis

We develop an iterative assistant we call ``ChatVis'' that can synthetically generate Python scripts for data analysis and visualization using a large language model (LLM). The assistant allows a user to specify the operations in natural language, attempting to generate a Python script for the desired operations, prompting the LLM to revise the script as needed until it executes correctly. The iterations include an error detection and correction mechanism that extracts error messages from the execution of the script and subsequently prompts LLM to correct the error. Our method demonstrates correct execution on five canonical visualization scenarios, comparing results with ground truth. 


# Running a Specific Notebook

To run the notebook, follow these steps:

1. **Install Jupyter (if not installed already):**

    ```bash
    pip install jupyter
    pip install openai
    ```

2. **Launch Jupyter Notebook:**

    Navigate to the directory where the notebook is located and launch the Jupyter notebook server:

    ```bash
    jupyter notebook
    ```

3. **Open the Notebook:**

    In the Jupyter interface that opens in your web browser, navigate to the notebook (e.g., `ml-dvr.ipynb`) and click on it to open.

4. **Run Cells:**

    - Once the notebook is open, you can run cells one by one using `Shift + Enter`.
    - You can also run all cells at once by selecting "Run All" from the `Cell` menu.

5. **Insert OpenAI API Key (if applicable):**

    In the designated cell, insert your OpenAI API key like this:

    ```python
    client = OpenAI(api_key="") # provide you OpenAI API key here
    ```

6. **Save Your Work:**

    - After running all the necessary cells, it will generate the screenshot.
