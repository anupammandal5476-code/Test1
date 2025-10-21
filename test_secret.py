import os

# Get the secret from environment
secret = os.getenv('MY_SECRET')

print("Testing GitHub Secret...")

if secret:
    print("✅ SUCCESS: Secret is available!")
    print(f"Secret length: {len(secret)} characters")
    
    # Check if it matches our expected secret
    if secret == "my-test-secret-123":
        print("✅ Secret value is correct!")
    else:
        print("⚠️  Secret value doesn't match expected")
else:
    print("❌ FAIL: Secret is empty or not available")