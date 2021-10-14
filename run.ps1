if (!(Test-Path .\.venv\)) {
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
}
else {
    .\.venv\Scripts\Activate.ps1
}
python main.py