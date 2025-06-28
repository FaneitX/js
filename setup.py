from setuptools import setup, find_packages

setup(
    name="meal_planner",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pytest>=6.0.0',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Weekly meal planner application",
    license="MIT",
    python_requires=">=3.8",
)