#!/usr/bin/env python3
"""
Project Check Script
This script checks if the Django project is ready to run and provides
instructions for fixing any issues.
"""

import os
import sys
import subprocess

def check_python():
    """Check Python version and availability."""
    print("Checking Python...")
    try:
        version = sys.version_info
        print(f"  Python {version.major}.{version.minor}.{version.micro} detected")
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False

def check_django():
    """Check if Django is installed."""
    print("Checking Django...")
    try:
        import django
        print(f"  Django {django.__version__} detected")
        return True
    except ImportError:
        print("  Django NOT installed")
        return False

def check_requirements():
    """Check if requirements.txt exists."""
    print("Checking requirements...")
    if os.path.exists("requirements.txt"):
        print("  requirements.txt found")
        with open("requirements.txt", "r") as f:
            content = f.read()
            print(f"  Requirements: {content.strip()}")
        return True
    else:
        print("  requirements.txt NOT found")
        return False

def check_project_structure():
    """Check if essential project files exist."""
    print("Checking project structure...")
    essential_files = [
        "manage.py",
        "blog_project/settings.py",
        "blog_project/urls.py",
        "blog/models.py",
        "blog/views.py",
        "users/views.py",
    ]
    
    all_exist = True
    for file in essential_files:
        if os.path.exists(file):
            print(f"  [OK] {file}")
        else:
            print(f"  [MISSING] {file}")
            all_exist = False
    
    return all_exist

def check_database():
    """Check if database file exists."""
    print("Checking database...")
    if os.path.exists("db.sqlite3"):
        print("  db.sqlite3 found")
        size = os.path.getsize("db.sqlite3")
        print(f"  Database size: {size} bytes")
        return True
    else:
        print("  db.sqlite3 NOT found (this is normal for new project)")
        return False

def main():
    print("=" * 60)
    print("DJANGO BLOG PROJECT CHECK")
    print("=" * 60)
    
    results = {
        "python": check_python(),
        "django": check_django(),
        "requirements": check_requirements(),
        "structure": check_project_structure(),
        "database": check_database(),
    }
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    all_good = all(results.values())
    
    if all_good:
        print("[OK] Project is ready to run!")
        print("\nTo run the project:")
        print("  1. Apply migrations: python manage.py migrate")
        print("  2. Run server: python manage.py runserver")
        print("  3. Open browser to: http://127.0.0.1:8000/")
    else:
        print("[ISSUES] Project has issues that need to be fixed.")
        
        if not results["django"]:
            print("\n[ERROR] Django is not installed.")
            print("   Fix: Install Django using:")
            print("     pip install Django")
            print("\n   If pip fails due to temp directory issues:")
            print("     1. Create temp directory: mkdir C:\\temp")
            print("     2. Set env vars: set TEMP=C:\\temp && set TMP=C:\\temp")
            print("     3. Try again: pip install Django")
        
        if not results["structure"]:
            print("\n[ERROR] Some project files are missing.")
            print("   Fix: Ensure all project files are present.")
        
    print("\n" + "=" * 60)
    print("PROJECT INFO")
    print("=" * 60)
    print("This is a Django blog application with:")
    print("  - User registration and authentication")
    print("  - Blog post creation, editing, deletion")
    print("  - User profiles")
    print("  - SQLite database")
    print("  - Bootstrap-styled templates")
    
    # Try to run a simple check on manage.py
    if results["django"]:
        print("\nTesting manage.py...")
        try:
            subprocess.run([sys.executable, "manage.py", "check"], 
                          capture_output=True, text=True, timeout=10)
            print("  manage.py check completed")
        except Exception as e:
            print(f"  Error running manage.py: {e}")

if __name__ == "__main__":
    main()