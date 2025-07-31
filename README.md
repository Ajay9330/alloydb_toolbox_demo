# Hotel Management API

This is a FastAPI application for managing a hotel, using an AlloyDB database.

## Setup

1.  **Clone the repository:**

    Using HTTPS:
    ```bash
    git clone https://github.com/Ajay9330/alloydb_toolbox_demo.git
    cd alloydb_toolbox_demo
    ```

    Using SSH:
    ```bash
    git clone git@github.com:Ajay9330/alloydb_toolbox_demo.git
    cd alloydb_toolbox_demo
    ```

2.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your AlloyDB database:**

    *   Make sure you have an AlloyDB cluster and instance running.
    *   Create a `.env` file in the root of the project with the following content:

        ```
        ALLOYDB_CONNECTION_NAME=projects/<your-project>/locations/<your-location>/clusters/<your-cluster>/instances/<your-instance>
        ALLOYDB_USER=<your-user>
        ALLOYDB_PASSWORD=<your-password>
        ALLOYDB_DB=<your-db>
        ```
    *   The application is configured to connect to your AlloyDB instance using a public IP address. This is set in `app/core/database.py`.

5.  **GCA+AlloyDB MCP Setup :**

    This setup is for using the AlloyDB MCP with Gemini Code Assist.

    **GCP:**
    Create a GCP project and give permission to your account as the Alloydb admin.

    **LOCAL SETUP:**
    Install MCP toolbox for databases

    ```bash
    # see releases page for other versions
    export VERSION=0.9.0
    curl -O https://storage.googleapis.com/genai-toolbox/v$VERSION/linux/amd64/toolbox
    chmod +x toolbox
    ```

    Install gcloud cli on your local machine and login. Verify using below command

    ```bash
    #cmd to install gcloud cli
    curl https://sdk.cloud.google.com | bash

    #cmd to login
    gcloud auth login

    #cmd to verify login
    gcloud config list
    ```

    Install gemini code assist extension into the VS code and login into that using a project.
    Activate Agent mode in GCA via following
    Open the Command palette (Cmd + Shift + P) and then select Open User Settings JSON.
    Add the following line to your user settings JSON:
    `"geminicodeassist.updateChannel": "Insiders",`

    Open a folder in VS code and add a file .gemini/setting.json having MCP configuration as follows for the AlloyDB-database and AlloyDB-admin.

    ```json
    {
      "theme": "GitHub",
        "mcpServers": {
          "alloydb": {
          "command": "path/to/toolbox",
          "args": ["--prebuilt","alloydb-postgres","--stdio"],
          "env": {
              "ALLOYDB_POSTGRES_PROJECT": "project_id",
              "ALLOYDB_POSTGRES_REGION": "location",
              "ALLOYDB_POSTGRES_CLUSTER": "cluster_name",
              "ALLOYDB_POSTGRES_INSTANCE": "instance_name",
              "ALLOYDB_POSTGRES_DATABASE": "database_name",
              "ALLOYDB_POSTGRES_USER": "database_user",
              "ALLOYDB_POSTGRES_PASSWORD": "database_password"
            }
          },
    "alloydb-admin": {
         "command": "./PATH/TO/toolbox",
         "args": ["--prebuilt", "alloydb-postgres-admin", "--stdio"],
         "env": {
           "API_KEY": "your-api-key"
         }
       }
        }
      
    }
    ```

    To verify MCP configuration you can run the bellow command in the GCA in VS code

    `/mcp`

## Running the Application

1.  **Start the FastAPI server:**

    ```bash
    uvicorn main:app --reload
    ```

2.  **Access the API documentation:**

    Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation (Swagger UI).
