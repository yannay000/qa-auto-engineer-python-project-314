import os

IMPLEMENTATION = os.getenv("IMPLEMENTATION")
print(f"IMPLEMENTATION: {IMPLEMENTATION}")
if IMPLEMENTATION: 
	os.environ['APP_BASE_URL'] = f"http://{IMPLEMENTATION}.test" 
LOGIN = os.getenv("LOGIN", "test")
PASSWORD = os.getenv("PASSWORD", "test")