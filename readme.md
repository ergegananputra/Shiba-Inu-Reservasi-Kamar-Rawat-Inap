## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or higher (Recomendation 3.12)
- pip
- venv (comes with Python 3.3 and above)
- XAMPP

### Setting Up

1. Clone the repository:
    ```bash
    git clone https://github.com/ergegananputra/Shiba-Inu-Reservasi-Kamar-Rawat-Inap.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Shiba-Inu-Reservasi-Kamar-Rawat-Inap
    ```

3. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\.venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source .venv/bin/activate
        ```

5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the application:
    Turn on XAMPP

    ```bash
    uvicorn main:app --reload
    ```
    or
    ```bash
    fastapi dev main.py
    ```

Now, you should be able to access the API at `http://localhost:8000`.

## How To Run
1. Make sure the venv activated, then run this script
    ```bash
    fastapi dev main.py
    ```

## See Also 
Fast API Documentation:
https://fastapi.tiangolo.com/
https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_3_1
https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra
